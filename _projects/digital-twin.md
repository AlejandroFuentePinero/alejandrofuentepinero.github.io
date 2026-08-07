---
title: "Digital Twin"
excerpt: "A conversational agent answers questions about my work, grounded in a curated knowledge base. A second model reviews every answer before a visitor sees it."
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

The digital twin is a conversational agent that answers questions about my work on my behalf. A second model from a different family reviews every answer before a visitor sees it. On the frozen evaluation baseline, retrieval scores 0.866 mean reciprocal rank and answers score 4.56 on the judge's scale.

Each turn passes through a classifier, a branch-specific prompt, retrieval over a vector store, generation and the guardrail. Failed attempts retry with structured feedback. Persistent failures fall back to a polite contact line. The chat lives on the home page and runs as a Hugging Face Space.

## Links

- **Try it on the home page:** [Digital twin chat](/#digital-twin)
- **Live demo:** [alejandrofupi-digital-twin.hf.space](https://alejandrofupi-digital-twin.hf.space)
- **Hugging Face Space:** [Alejandrofupi/digital-twin](https://huggingface.co/spaces/Alejandrofupi/digital-twin)
- **Source:** [digital-twin on GitHub](https://github.com/AlejandroFuentePinero/digital-twin)

## Architecture

<figure>
  <img src="/files/digital_twin_runtime.png" alt="Digital Twin runtime pipeline" style="width:100%; max-width:520px; display:block; margin: 0 auto;">
</figure>

A small classifier (gpt-4.1-nano) labels each question and routes it to a branch: technical, behavioural, logistical, generic or gap. Each branch loads only the profile sections, rules and tools its question type needs. The generator (gpt-4.1) drafts the answer, fetching full project documentation through a registered tool on technical branches. The guardrail (claude-sonnet-4-6) accepts or rejects the draft against the same ground truth the generator saw.

Rejections carry structured feedback back into the generator, up to 3 times. Shared rule constants feed both the generator and the guardrail, so their rules cannot drift apart.

Knowledge splits in 2. A small always-on profile of about 2,000 tokens supplies identity and rules. The system retrieves the larger knowledge base on demand from a vector store.

Every turn writes one JSONL record: branch, classifier confidence, retrieved chunks, tool calls, retries and latency. A local operator dashboard, Sentinel, reads that log for drift detection and gap discovery.

## The decision that was hard

The first design loaded one monolithic prompt: full profile, all rules, retrieved chunks. That put 6,000 to 7,000 tokens into every turn and diluted the model's attention. I had hit that failure mode on earlier projects. Section trimming was a band-aid, and cheap models pick tools unreliably, so model-chosen context was out.

The resolution was classify-then-route. A thin classifier picks the branch, and the branch composes only what its question type needs. The cost is a small classifier call per turn. The gain is a short, relevant prompt on every branch.

## What was measured

A 149-question evaluation set covers 7 question types. The types are direct fact, temporal, comparative, numerical, relationship, spanning and holistic. Retrieval scoring uses mean reciprocal rank (MRR), nDCG and keyword coverage. A judge model scores answers on accuracy, completeness and relevance.

The frozen baseline stands at 0.866 MRR and 4.56 accuracy on the judge's scale.

A canary corpus of 50 probe questions replays periodically against the live system. Canary records carry an `is_canary` flag and share the live log file. Drift therefore appears in the same dashboard the traffic flows through. Major drift flags fell across the last 3 points: 12, then 9, then 6.

## What did not work

The guardrail at first saw only the retrieved chunks, not the content the generator fetched through tools. It judged tool-grounded answers as fabrication and rejected them. The fix shares every grounding surface with the guardrail. Whatever context the generator used, the judge now sees.

The first drift detector compared mechanisms, not outcomes. After a routine re-ingest it raised 52 flags against a healthy system, 33 of them from re-chunked storage. I removed the 2 mechanism-level checks, and the same data produced 12 signal-dominated flags. The detector now watches what visitors would see, not how the system got there.

## Privacy

The system logs conversations to a private Hugging Face dataset so I can improve it. Email me at [alejandrofuentepinero@gmail.com](mailto:alejandrofuentepinero@gmail.com) to request deletion.

## Stack

Python · Gradio · ChromaDB · LiteLLM · OpenAI (gpt-4.1, gpt-4.1-nano, text-embedding-3-small) · Anthropic (claude-sonnet-4-6) · Pydantic · Tenacity · Hugging Face Spaces and Datasets
