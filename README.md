# Global AI Data Engineer Journey

My 12-month mentor-guided project to go from beginner (SQL basics, zero Python/cloud) to building production AI data systems — the foundation that makes LLMs reliable at scale.

**Goal**: Land a remote/global role ($90k–$130k+) building RAG pipelines, agentic data flows, real-time embeddings, quality monitoring, and cost-optimized ingestion for AI companies.

**Current Phase**: Phase 0 – Setup & First Ingestion (Feb 2026)

**Mentor Style**: Top-down, 100% hands-on. We write code together, break it, fix it, commit, and explain every decision.

## Progress Tracker

| Date       | Milestone                          | Status     | Key Learnings / Files                  | Notes |
|------------|------------------------------------|------------|----------------------------------------|-------|
| 2026-02-XX | Repo setup + first ingestion script| In Progress| `01_ingest_and_chunk.py`              | Starting today |
|            |                                    |            |                                        |       |
|            |                                    |            |                                        |       |

(We will fill this table after every session.)

## Project Vision (End Goal – Month 12)

A deployable, production-ish AI knowledge assistant:
- Ingests real sources (PDFs, APIs, databases)
- Chunks intelligently
- Generates embeddings (local + cloud)
- Stores in vector DB (PGVector / Pinecone free)
- Orchestrates with Prefect
- RAG + simple agent logic (LangGraph)
- Quality checks & monitoring
- Deployed (Streamlit / FastAPI on HuggingFace / Render)

## Tech Stack (Evolving)

- Python (core)
- LangChain / LlamaIndex (RAG wrappers)
- Ollama (local LLMs)
- HuggingFace embeddings
- PostgreSQL + PGVector
- Prefect 2 (orchestration)
- Docker basics
- GCP/AWS free tiers
- GitHub Actions (CI)

## How to Follow Along

1. Clone: `git clone https://github.com/rohit-ai-engineer/global-ai-data-engineer.git`
2. `cd global-ai-data-engineer`
3. `pip install -r requirements.txt` (we'll create this file soon)
4. Run scripts in order: `python 01_ingest_and_chunk.py`

Last updated: February 14, 2026

Built live with my mentor.