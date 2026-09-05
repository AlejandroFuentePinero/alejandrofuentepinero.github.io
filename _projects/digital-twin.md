---
title: "Digital Twin"
excerpt: "An agent answers questions about my work. A second model checks every answer before you see it. Accuracy scores 4.56 of 5 on 149 questions."
date: 2026-05-07
type: engineering
stack:
  - Python
  - ChromaDB
  - LiteLLM
  - Gradio
redirect_from:
  - /datascience/projects/digital-twin/
---

Ask the digital twin about my work and it answers on my behalf: which projects I have built, what my papers found, how I approach a problem. Before you see the reply, a second model from a different provider checks it against the same facts and either accepts it or sends it back. On the frozen evaluation baseline the retriever scores 0.866 mean reciprocal rank, so the right passage usually sits at the top, and answers score 4.56 of 5 for accuracy.

Each turn passes through a classifier, a prompt built for that kind of question, retrieval, generation and the guardrail. A rejected draft gets feedback and another try. Persistent failures end in a polite invitation to email me.

## Links

- **Try it:** [Digital twin chat](/digital-twin/)
- **Source:** [digital-twin on GitHub](https://github.com/AlejandroFuentePinero/digital-twin)

## Architecture

<figure>
  <picture>
    <source type="image/webp" srcset="/files/digital_twin_runtime.webp">
    <img src="/files/digital_twin_runtime.png" alt="Digital Twin runtime pipeline" width="438" height="1772" loading="lazy" style="width:100%; max-width:520px; display:block; margin: 0 auto;">
  </picture>
</figure>

A small classifier (gpt-4.1-nano) reads each question and sends it down one of 5 branches: technical, behavioural, logistical, generic or gap. A gap question asks about something I have not done. Each branch loads only the profile sections, rules and tools its kind of question needs. The generator (gpt-4.1) drafts the answer, and on technical branches it can fetch a project's full documentation through a registered tool. The guardrail (claude-sonnet-4-6) then judges the draft against the same ground truth the generator saw.

When the guardrail rejects a draft, its structured feedback goes back to the generator, up to 3 times. Both models read their rules from the same shared constants, so the rule the generator follows and the rule the judge enforces cannot drift apart.

The twin's knowledge is split in 2. A small always-on profile of about 2,000 tokens, roughly 1,500 words, carries identity and rules and is present in every turn. The larger knowledge base sits in a vector store, a database that finds passages by meaning rather than by exact words, and is retrieved only when a question needs it.

Every turn writes one line to a log: the branch, the classifier's confidence, the chunks retrieved, any tool calls, the retries and the latency. A local operator dashboard called Sentinel reads that log to detect drift and to find the questions the knowledge base cannot yet answer.

## The decision that was hard

The first design used one big prompt: the full profile, every rule and all the retrieved chunks, in every turn. That put 6,000 to 7,000 tokens in front of the model each time and diluted its attention, a failure I had already met on earlier projects. Trimming sections would have been a bandage, and letting the model choose its own context was out, because cheap models pick tools unreliably.

The answer was to classify first and route second. A thin classifier picks the branch, and the branch assembles only what its kind of question needs. The cost is one small extra call per turn. The gain is a short, relevant prompt every time.

## What was measured

The evaluation set holds 149 questions across 7 types: direct fact, temporal, comparative, numerical, relationship, spanning and holistic. Retrieval is scored with mean reciprocal rank (MRR), which rewards putting the right passage near the top, with nDCG, which rewards a well-ordered list, and with keyword coverage. A judge model scores each answer for accuracy, completeness and relevance on a 1 to 5 scale. The frozen baseline stands at 0.866 MRR and 4.56 for accuracy.

Drift is watched with a canary corpus, 50 probe questions replayed against the live system between releases. Canary records carry a flag and share the live log file, so drift shows up in the same dashboard the real traffic flows through. The flag count is a trip-wire rather than a gate. The latest run raised 14 flags, and triage found that 6 of the 9 major ones came from 2 questions whose answers had improved.

## What did not work

At first the guardrail saw only the retrieved chunks, not the documentation the generator had fetched through its tool. So it read correct, tool-grounded answers as fabrication and rejected them. The fix hands the guardrail every surface the generator could have drawn on. Whatever context the generator used, the judge now sees too.

The first drift detector also compared mechanisms instead of outcomes. After a routine re-ingest of the knowledge base it raised 52 flags against a healthy system, and 33 of them came from storage that had merely been re-chunked. I removed the 2 mechanism-level checks, and the same data produced 12 flags, most of them real signal. The detector now watches what a visitor would see, not how the system got there.

## Privacy

The system logs conversations to a private Hugging Face dataset so I can improve it. Email me at [alejandrofuentepinero@gmail.com](mailto:alejandrofuentepinero@gmail.com) to request deletion.

## Stack

Python · Gradio · ChromaDB · LiteLLM · OpenAI (gpt-4.1, gpt-4.1-nano, text-embedding-3-large) · Anthropic (claude-sonnet-4-6) · Pydantic · Tenacity · Hugging Face Spaces and Datasets
