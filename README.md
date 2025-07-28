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
# (example)
ollama install llama-3.2
```

---

## Finance Agent AI Stack

- 🖥️ **LLM**: Llama 3.2 (via Ollama) — No API keys needed!
- 🔍 **Embeddings**: FastEmbed (BAAI/bge-small-en-v1.5) — Completely local
- 📊 **Knowledge Base**: Amazon’s 2023 PDF processed and searchable
- 🗄️ **Vector Database**: LanceDB — Local storage
- 🔧 **Tool Calling**: Fully integrated with knowledge search
- 🌐 **Web Search**: DuckDuckGo fallback available
