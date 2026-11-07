# MCP + LangChain + Groq Agent Demo

A working example of a **ReAct agent** that talks to multiple **MCP (Model Context Protocol)** servers through LangChain, powered by **Groq** LLMs.

The agent can:
- 🧮 **Do math** using tools from a local `stdio` MCP server (`add`, `multiply`)
- 🌤️ **Check weather** using tools from a remote `streamable-http` MCP server

It demonstrates multi-server MCP orchestration, tool binding, and multi-turn tool-calling loops in a real, runnable project.

---

## ✨ Features

- **Multi-server MCP client** — connects to a `stdio` server and an `HTTP` server in one session
- **ReAct agent** via `langgraph.prebuilt.create_react_agent`
- **Tool-calling loop** — the agent chains multiple tool calls (e.g. `add(3,5)` → `multiply(8,12)`)
- **Groq-powered** — uses fast, tool-capable models like `qwen/qwen3.6-27b` and `openai/gpt-oss-120b`
- **Debug script** — isolates MCP, API key, and model problems in one run
- **Clean shutdown / error handling** — timeouts prevent silent hangs

