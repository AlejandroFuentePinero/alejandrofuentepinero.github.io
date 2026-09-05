---
title: "AI-JIE: Extraction and Evaluation Pipeline"
excerpt: "The extraction layer of the Job Intelligence Engine tells a genuine requirement from a nice-to-have. Human review scored the final prompt at 4.11 of 5."
date: 2026-04-09
type: engineering
stack:
  - Python
  - OpenAI API
  - Pydantic
  - asyncio
redirect_from:
  - /datascience/projects/ai-jie/
---

A job posting mixes what the employer needs, what they would like and what the job involves, and rarely labels which is which. AI-JIE reads raw postings and turns each one into a validated record with the skills sorted by intent: required, preferred or soft. Human review scored the final prompt 4.11 of 5, with structural fields such as seniority at 5.00. The published dataset covers 3,892 data scientist postings.

Extracting skills was never the hard part. The hard part was telling a genuine requirement from a nice-to-have, and a skill from a responsibility described as one. It took 33 prompt versions and one architecture change.

AI-JIE is the extraction layer of the [Job Intelligence Engine](/projects/job-intelligence-engine/), its host system.

## Links

- **Source:** [AI-JIE on GitHub](https://github.com/AlejandroFuentePinero/ai-jie)
- **Technical report:** [Architecture and evaluation method](https://github.com/AlejandroFuentePinero/ai-jie/blob/main/docs/technical_report.md)
- **Published datasets:** [preprocessed](https://huggingface.co/datasets/Alejandrofupi/ai-jie-jobs-lite-preprocessed) · [postprocessed](https://huggingface.co/datasets/Alejandrofupi/ai-jie-jobs-lite-postprocessed) on Hugging Face Hub
- **Host system:** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)

## Architecture

An asynchronous pipeline sends each posting to the model and gets back a `Job` object that Pydantic has already validated, through the instructor library. The skills arrive partitioned by intent, and the role metadata covers seniority, job family, years of experience, education and responsibilities. Both the extractor and the judge run at temperature 0, which removes the model's randomness, so the same posting always produces the same record.

A semaphore caps the pipeline at 20 requests in flight, and every result is written to a checkpoint file as it lands. An interrupted batch resumes from the checkpoint instead of paying for the same postings twice.

After the model comes a deterministic clean-up layer: it drops skills that were really responsibilities and filters a blocklist of known noise. The model extracts broadly on purpose, and the rules remove what broad extraction lets through, the same way every time.

Extraction started on gpt-4o-mini and moved to gpt-5.4-mini for the final batch, which ran about 3 times faster. The upgrade needed its own prompt pass, because the newer model followed the rules too literally and pulled whole responsibility phrases into the required skills.

## The decision that was hard

The early prompts asked the model to sort skills straight into required, preferred or soft. Accuracy on preferred skills stayed poor, the model kept mistaking responsibilities for requirements, and no amount of rule tweaking moved it.

The fix was structural. I added 3 intermediate fields to the schema that force the model to think before it classifies. It first lists the skills it found inside responsibility statements, then the phrases that signal something is optional, then every technical skill anywhere in the posting. Only after that does it classify. Schema design turned out to be the biggest lever across all 33 versions, and this extract-then-classify scaffold is the heart of it.

## What was measured

A judge model scores every extraction on 12 dimensions, each from 1 to 3. Before it scores anything, the judge fills in its own ground-truth fields, so it cannot lean on the extractor's reasoning. Runs on 3 different random samples checked that a gain was real and not a lucky draw.

The final gate was a human evaluation of 28 postings, scored 1 to 5. Seniority and responsibilities reached 5.00. The weakest dimension was required skills at 4.00, because discipline labels such as field names were leaking out of the responsibility scan. Version 33 closed that leak with a guard for postings that lack clear section headers, and the full batch ran on it. The overall human score was 4.11 of 5, and trend plots track every dimension across all 33 versions.

## What did not work

The first judge scored a suspicious 2.96 of 3. The cause was circular: the extraction it was judging still carried the full posting text, so checking it was trivial. The fix strips those passthrough fields before judging, and the scores fell to honest levels.

The judge also enforced its own conventions instead of the extraction rules, punishing the extractor for breaking instructions it had never seen. The rewritten judge prompt now contains the extraction rules word for word.

One promising experiment died on measurement. Feeding the model the posting's industry label raised the accuracy of the industry field from 36% to 78%. But it also diluted the model's attention and regressed the skill fields, whichever way it entered the prompt, so I reverted it in full.

## Stack

Python · OpenAI API (gpt-5.4-mini, upgraded from gpt-4o-mini) · instructor · Pydantic · asyncio · Hugging Face Hub · pytest
