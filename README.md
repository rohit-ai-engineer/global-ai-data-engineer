## Related Vision Repo

This repo is my **hands-on tactical build path** — daily code, experiments, and incremental progress toward reliable AI data systems.

For the **long-term architectural vision** (trust boundaries, explicit evaluation layers, observability-first design, domain-agnostic principles), see:

**Vision📐**
👉 [ai-systems-learning-lab](https://github.com/rjrohitj/ai-systems-learning-lab)  
   (My original manifesto repo — where high-level ideas and phase planning live) 

# Global AI Data Engineer Journey

My 12-month mentor-guided project to go from beginner (SQL basics, zero Python/cloud) to building production AI data systems — the foundation that makes LLMs reliable at scale.

**Goal**: Land a remote/global role ($90k–$130k+) building RAG pipelines, agentic data flows, real-time embeddings, quality monitoring, and cost-optimized ingestion for AI companies.

**Current Phase**: Phase 0 – Setup & First Ingestion (Feb 2026)

**Mentor Style**: Top-down, 100% hands-on. We write code together, break it, fix it, commit, and explain every decision.

## Progress Tracker

| Date       | Milestone                                      | Status | Key Learnings / Files                          | Notes                          |
|------------|------------------------------------------------|--------|------------------------------------------------|--------------------------------|
| 2026-02-14 | Repo setup + first ingestion script            | Done   | `01_ingest_and_chunk.py`, README.md            | First push successful          |
| 2026-02-14 | Improved chunking (sentence-aware + overlap)   | Done   | `02_better_chunking.py`                        | Overlap works; size controlled |
| 2026-02-14 | Added link to vision repo + progress update    | Done   | README.md                                      | Connecting tactical & strategic|
| 2026-02-14 | First embeddings generated (384-dim)           | Done   | `03_generate_embeddings.py`,`my_knowledge_embeddings.npy` | Loop bug fixed; CPU mode works; vectors previewed |

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