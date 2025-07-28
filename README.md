# Agno Agents Documentation

---

## Overview

**Agno Agents** is a UV-powered project containing two specialized agents:

1. **Web Agent**

   - Uses the Groq LLM to answer general web‐based queries.
   - Falls back to DuckDuckGo for real‑time information.

2. **Finance Agent**

   - Primarily answers from a local PDF knowledge base (Amazon’s 2023 Shareholder Letter).
   - If a query falls outside the PDF contents, it automatically performs a web search.

---

## Prerequisites

- **Python** ≥ 3.9
- **UV CLI** installed
- **Ollama** (for local Llama models)
- **GROQ API Key** (for Groq model usage) in a `.env` file:

  ```dotenv
  GROQ_API_KEY=your_actual_groq_api_key_here
  ```

---

## Setup

### 1. Initialize UV project

```bash
uv init agno_test_agents
```

### 2. Switch to project directory

```bash
cd agno_test_agents
```

### 3. Install or add packages

- **Single package**

  ```bash
  uv add pandas
  ```

- **Multiple packages & generate `requirements.txt`**

  ```bash
  uv add -r requirements.txt
  ```

### 4. Install Ollama for Finance Agent

```bash
# Example: install Llama 3.2 locally
ollama install llama-3.2
```

---

## Web Agent

The **Web Agent** handles general-purpose queries by leveraging a local Groq model and DuckDuckGo tools for web searches.

- **Model**: Groq (Llama‑3.1‑8b‑instant)
- **Tools**: DuckDuckGo search
- **Behavior**: Answers from model; for up‑to‑date facts, uses DuckDuckGo fallback.

**Running the Web Agent**

```bash
uv run web.py
```

---

## Finance Agent

The **Finance Agent** specializes in Amazon company analysis, prioritizing data from the 2023 Shareholder Letter PDF and falling back to web search when needed.

- **Model**: Llama‑3.2 (via Ollama)
- **Embeddings**: FastEmbed (BAAI/bge-small-en-v1.5)
- **Knowledge Base**: Amazon 2023 PDF loaded via `PDFUrlKnowledgeBase`
- **Vector DB**: LanceDB for local document search
- **Tools**: DuckDuckGo search for out‑of‑scope queries
- **Behavior**:

  1. Search PDF KB for answers.
  2. If no relevant PDF content, perform web search.
  3. Prefer PDF‐sourced info; cite web only as needed.

**Running the Finance Agent**

```bash
uv run finance-agent.py
```

---

## Workflow Summary

1. **Setup** your environment and install dependencies.
2. **Initialize** your UV project and add packages.
3. **Configure** `~/.env` with your GROQ API key.
4. **Run** either agent:

   - `web.py` for web‐centric Q\&A
   - `finance-agent.py` for Amazon financial insights (with PDF first, web fallback)

### Finance Agent Output

<img width="896" height="829" alt="finance agent output" src="finance agent output.png" />

_Sample: The Finance Agent provides a detailed breakdown of Amazon's 2023 revenue distribution, citing the PDF knowledge base and supplementing with web data if needed._

---

### Web Agent Output

<img width="896" height="829" alt="web agent output" src="web agent out.png" />

_Sample: The Web Agent answers a general query using the Groq model and, when necessary, retrieves up-to-date information from the web._

Enjoy building with Agno Agents!
