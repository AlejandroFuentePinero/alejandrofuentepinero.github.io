---
title: "LLM Engineering Lab"
excerpt: "A lab of 11 projects across retrieval, fine-tuning and agents. The flagship prices Amazon products from their descriptions to within $29.95 on average."
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

This lab is where I learned the language model stack by building it. Its 11 Python systems move from prompting and retrieval through tool use and fine-tuning to autonomous agents and deployment. The flagship predicts the price of an Amazon product from its text description alone. Its final ensemble lands within $29.95 of the true price on average and explains 86.3% of price variation across 10,000 products it never saw in training.

The projects escalate on purpose. The early ones isolate one pattern each. The flagship then joins those patterns into a single system: data curation, fine-tuning, retrieval, a fleet of agents and a live dashboard. Every model faces the same held-out test, so the comparison between them stays fair.

## Links

- **Source:** [llm-engineering-lab on GitHub](https://github.com/AlejandroFuentePinero/llm-engineering-lab)

<p align="center">
  <picture>
    <source type="image/webp" srcset="/files/llm-engineering-cartoon.webp">
    <img src="/files/llm-engineering-cartoon.png" alt="Cartoon of a programmer and a robot, both in cowboy hats, at a desk beside a screen that reads LLM Tools" width="900" height="600" loading="lazy">
  </picture>
</p>

## The flagship: a price predictor

The raw material is 820,000 Amazon products. A curation pipeline filters and deduplicates them, then resamples with quadratic weighting so that cheap items stop dominating the price distribution. Before any model sees the data, a batch job on Groq writes a clean structured summary for each product. Each summary becomes a prompt-completion pair, cut at 110 tokens with the Llama-3.2-3B tokeniser. Both the full dataset and a 23,000-item lite version live on Hugging Face Hub.

The open-source model is fine-tuned with QLoRA, a technique that shrinks the model to 4-bit precision and trains only small adapter layers. That is how a 3-billion-parameter model fits on a free T4 GPU. The adapters attach to the attention layers in lite mode and to the feed-forward layers as well in full mode. Long batch jobs save their state to disk, so a 24-hour run survives a restart. The retrieval path embeds all 800,000 training products into ChromaDB, a vector database, and hands the 5 most similar products to GPT-5.1 as context for each prediction.

The ensemble blends GPT-5.1 with retrieval at 80%, the fine-tuned specialist at 10% and the deep network at 10%. On top sits an agent fleet: a scanner agent filters deal feeds, an ensemble agent prices each deal, and a messaging agent sends a push notification through Pushover. GPT-5.1 plans the loop itself with 3 registered tools.

A Gradio dashboard runs the deal finder on load and refreshes every 5 minutes. It streams the agent logs live and draws the 800,000-vector store as a 3-dimensional t-SNE plot, a projection that places similar products near each other.

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

The hard design problem was a fair benchmark across model families. A random forest, a fine-tuned open-source model and a frontier model with retrieval do not naturally share inputs or outputs. It is easy to flatter one family by feeding it better data. The resolution has 3 parts. Every model consumes the same cleaned summaries, faces the same held-out split, and reports through one shared Tester class.

The Tester pulls a number out of whatever text a model returns, so generative models can be compared with regressors without hand-tuning per family.

## What was measured

Every model runs the same 200-item evaluation on the shared split, and the training curves log to Weights & Biases. The ensemble finishes at a $29.95 mean absolute error and 86.3% R² across the 10,000 test products.

Two supporting projects carry their own measurements. The code benchmark compares hosted and local models on translating Python to C++. It separates compile errors from runtime errors from success and attributes each failure to the model that caused it. The retrieval assistant scores its retrieval with mean reciprocal rank and keyword coverage, and its answers with a judge model.

## What did not work

The raw price distribution nearly broke the benchmark. It skews so far toward cheap items that a model could score well by always guessing low. Quadratic resampling at curation time flattened the distribution and closed that exploit. The lesson stuck: a model can pass a benchmark by exploiting its shape rather than by learning the task.

Multi-agent systems fail in quiet ways: stale context, agents drifting out of their roles, state updated twice, turns taken out of order. One project, the 3-agent review panel, exists to expose exactly those failures on a shared transcript.

## The supporting projects

- **Expert Knowledge Worker.** A retrieval assistant over a Markdown knowledge base that shows its source chunks beside every answer. Its evaluation dashboard scores both retrieval and answers.
- **Multi-Agent Conversation.** A 3-agent review panel sharing one transcript, built to expose state and role drift.
- **Flight Booking Agentic Tool.** A chat agent that makes real tool calls against a SQLite backend, speaks its replies and generates destination images.
- **Code Performance Benchmark.** Hosted against local models on Python-to-C++ translation, with failure modes attributed per model.
- **Company Brochure Generator.** A planning call picks which pages of a company site to read, and a second call writes the brief.
- **Meeting Minute Generator.** Whisper transcription turned into minutes under a strict contract, with guardrails against invented metadata.
- **Sales Intake Copilot.** A lead-qualification chat that hands a structured note to a human rep.
- **Synthetic A/B Dataset Generator.** A schema-as-contract prompt that produces a conversion dataset and its dataset card.
- **Web Summary Tool.** A page-to-brief summariser that runs on hosted or local models.
- **Tech Tutor.** A streaming question answerer that explains concepts through movie analogies so they stick.

## Stack

Python · Groq · OpenAI · Llama-3.2-3B · QLoRA · ChromaDB · Modal · Gradio · Weights & Biases · Hugging Face Hub
