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

AI-JIE reads raw job postings and produces validated job records with skills split by intent: required, preferred or soft. A human evaluation of the final prompt scored 4.11 of 5, with structural fields at 5.00. The published dataset covers 3,892 data scientist postings.

The hard part was never extracting skills. It was telling a genuine requirement from a nice-to-have, and a skill from a responsibility described as one. The fix took 33 prompt versions and one architecture change: chain-of-thought scaffolding.

AI-JIE is the extraction layer of the [Job Intelligence Engine](/projects/job-intelligence-engine/), its host system.

## Links

- **Source:** [AI-JIE on GitHub](https://github.com/AlejandroFuentePinero/ai-jie)
- **Technical report:** [Architecture and evaluation method](https://github.com/AlejandroFuentePinero/ai-jie/blob/main/docs/technical_report.md)
- **Published datasets:** [preprocessed](https://huggingface.co/datasets/Alejandrofupi/ai-jie-jobs-lite-preprocessed) · [postprocessed](https://huggingface.co/datasets/Alejandrofupi/ai-jie-jobs-lite-postprocessed) on Hugging Face Hub
- **Host system:** [Job Intelligence Engine](https://github.com/AlejandroFuentePinero/job-intelligence-engine)

## Architecture

An async pipeline reads each posting and returns a Pydantic-validated `Job` object through the instructor library. Skills arrive partitioned by intent. Role metadata covers seniority, job family, experience, education and responsibilities. Both the extractor and the judge run at temperature 0, so the same posting always produces the same record.

A semaphore caps concurrency at 20 requests. The pipeline writes each result to a JSONL checkpoint as it lands. An interrupted batch resumes from the checkpoint instead of paying the spend again.

A deterministic postprocessing layer runs after the model: responsibility exclusion and a blocklist for known noise. The model extracts broadly on purpose. The rules remove what broad extraction lets through, reproducibly.

Extraction started on gpt-4o-mini and moved to gpt-5.4-mini for the final batch, about 3 times faster. The upgrade needed its own prompt pass, because the newer model followed the rules too literally.

## The decision that was hard

Early prompts asked the model to classify skills directly into required, preferred or soft. Accuracy on preferred skills stayed poor. The model kept conflating responsibilities with requirements. Rule tweaks alone moved nothing.

The fix was structural: 3 intermediate schema fields that force the model to reason before it classifies. The model first lists skills found inside responsibility statements, the optionality phrases it detected, and every technical skill anywhere. Only then does it classify. This extract-then-classify scaffold was the largest accuracy gain across all 33 versions.

## What was measured

A judge model scores every extraction on 12 dimensions, each from 1 to 3. The judge fills its own ground-truth fields before scoring, so it cannot anchor on the extractor's reasoning. Cross-seed runs on 3 random samples checked that a gain was real and not a lucky draw.

A human evaluation of 28 postings, scored 1 to 5, was the final gate. Seniority and responsibilities reached 5.00. The weakest dimension was required skills at 4.00, from discipline labels leaking out of responsibility scanning. Version 33 fixed that leak with a section-boundary guard, and the full batch ran on it.

Overall human score: 4.11 of 5. Cohen's kappa tracked agreement between judge and human, and trend plots tracked every dimension across versions.

## What did not work

The first judge scored a suspicious 2.96 of 3. The cause was circular: the extraction it judged still contained the full posting text, so verification was trivial. The fix strips passthrough fields before judging, and scores fell to honest levels.

The judge also enforced its own conventions instead of the extraction rules. It punished the extractor for following instructions it never saw. The rewritten judge prompt now contains the extraction rules verbatim.

One promising experiment died on measurement. An injected industry hint raised ground-truth accuracy from 36% to 78%. It also diluted the model's attention and regressed the skill fields, whichever way it entered the prompt. I reverted the hint in full.

## Stack

Python · OpenAI API (gpt-5.4-mini, upgraded from gpt-4o-mini) · instructor · Pydantic · asyncio · Hugging Face Hub · pytest
