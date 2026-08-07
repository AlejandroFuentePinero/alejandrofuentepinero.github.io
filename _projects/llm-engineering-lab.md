---
title: "LLM Engineering Lab"
excerpt: "11 projects spanning retrieval, fine-tuning and autonomous agents. The flagship ensemble predicts product prices with a mean absolute error of $29.95."
date: 2026-03-25
type: engineering
stack:
  - Python
  - QLoRA
  - ChromaDB
  - Modal
redirect_from:
  - /datascience/projects/llm-engineering-lab/
---

This lab holds 11 Python systems across the language model stack: prompting, retrieval, tool use, fine-tuning, agents and deployment. The flagship predicts Amazon product prices from text descriptions. Its final ensemble reaches a mean absolute error of $29.95 and R² of 86.3% on 10,000 held-out products.

The projects escalate. Early ones isolate one pattern each. The flagship joins them into one system: data curation, fine-tuning, retrieval, an agent fleet and a live dashboard. Every model faces the same held-out test, so the comparison stays fair.

## Links

- **Source:** [llm-engineering-lab on GitHub](https://github.com/AlejandroFuentePinero/llm-engineering-lab)

<p align="center">
  <picture>
    <source type="image/webp" srcset="/files/llm-engineering-cartoon.webp">
    <img src="/files/llm-engineering-cartoon.png" alt="Cartoon of a programmer and a robot, both in cowboy hats, at a desk beside a screen that reads LLM Tools" width="900" height="600" loading="lazy">
  </picture>
</p>

## The flagship: a price predictor

820,000 Amazon products enter a curation pipeline: filtered, deduplicated and resampled with quadratic weighting to flatten price skew. A batch job on Groq generates a clean structured summary per product before any model sees the data. Prompt-completion pairs use the Llama-3.2-3B tokeniser with a 110-token cap. Both the full and a 23,000-item lite dataset land on Hugging Face Hub.

Open-source fine-tuning uses QLoRA: 4-bit NF4 quantisation on a T4 GPU. Adapters train on attention layers in lite mode, adding feed-forward layers in full mode. Batch jobs persist state to disk, so a 24-hour run survives restarts. The retrieval path embeds all 800,000 training products into ChromaDB and passes the 5 most similar to GPT-5.1 as context.

The ensemble blends GPT-5.1 with retrieval at 80%, the fine-tuned specialist at 10%, the deep network at 10%. On top sits an agent fleet. A scanner agent filters deal feeds, an ensemble agent prices each deal, and a messaging agent pushes notifications through Pushover. GPT-5.1 plans the loop itself with 3 registered tools.

A Gradio dashboard runs the deal finder on load and refreshes every 5 minutes. It streams agent logs live and renders the 800,000-vector store as a 3-dimensional t-SNE plot.

### Models benchmarked

| Model | Type |
|---|---|
| Constant / Linear / Random Forest / XGBoost | Traditional baselines |
| 8-layer neural network | Deep learning |
| 10-layer deep network (residual, log-space) | Deep learning |
| GPT-4.1 Nano (zero-shot) | Frontier model, pre-trained |
| GPT-4.1 Nano (fine-tuned) | Frontier model, fine-tuned |
| Llama-3.2-3B (base) | Open-source model, pre-trained |
| Llama-3.2-3B (fine-tuned, QLoRA) | Open-source model, fine-tuned |
| GPT-5.1 with retrieval | Frontier model with retrieval |
| Ensemble (GPT-5.1 with retrieval, specialist, deep network) | Multi-model ensemble |

## The decision that was hard

A fair benchmark across model families was the hard design problem. Traditional regressors, fine-tuned open-source models and frontier models with retrieval do not naturally share inputs or outputs. The resolution has 3 parts. Every model consumes the same cleaned summaries, faces the same held-out split, and reports through one shared Tester class.

The Tester extracts a number from each model's raw text output. That keeps generative models comparable with regressors without hand-tuning per family.

## What was measured

Every model runs the same 200-item evaluation on the shared split. The ensemble finishes at a $29.95 mean absolute error and 86.3% R² across 10,000 test products. Training curves log to Weights & Biases.

A separate benchmark compares hosted and local models on Python-to-C++ translation. It distinguishes compile errors, runtime errors and success, and attributes each failure to the model output. The retrieval assistant scores retrieval with mean reciprocal rank and keyword coverage, and answers with a judge model.

## What did not work

The raw price distribution nearly broke the benchmark. It skews so far toward cheap items that a model can score well by always guessing low. Quadratic resampling at curation time flattened the distribution and closed that exploit. A model can pass a benchmark by exploiting its shape, not by learning the task.

Multi-agent systems fail in quiet ways: stale context, role drift, duplicated state and inconsistent turn-taking. One project, the 3-agent review panel, exists to expose exactly those failures on a shared transcript.

## The supporting projects

- **Expert Knowledge Worker.** A retrieval assistant over a Markdown knowledge base, with source chunks shown beside every answer. Its evaluation dashboard scores retrieval and answers.
- **Multi-Agent Conversation.** A 3-agent review panel sharing one transcript, built to expose state and role drift.
- **Flight Booking Agentic Tool.** A chat agent with real tool calls against a SQLite backend, plus spoken replies and generated destination images.
- **Code Performance Benchmark.** Hosted against local models on Python-to-C++ translation, with failure modes attributed per model.
- **Company Brochure Generator.** A planning call picks which pages to read, and a second call writes the brief.
- **Meeting Minute Generator.** Whisper transcription into contract-driven minutes, with guardrails against invented metadata.
- **Sales Intake Copilot.** A lead-qualification chat that hands a structured note to a human rep.
- **Synthetic A/B Dataset Generator.** A schema-as-contract prompt that produces a conversion dataset and its dataset card.
- **Web Summary Tool.** A page-to-brief summariser that runs on hosted or local models.
- **Tech Tutor.** A streaming question answerer with a movie-analogy backbone for memorability.

## Stack

Python · Groq · OpenAI · Llama-3.2-3B · QLoRA · ChromaDB · Modal · Gradio · Weights & Biases · Hugging Face Hub
