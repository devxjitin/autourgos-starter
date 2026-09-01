# autourgos-starter

[![Framework: Autourgos](https://img.shields.io/badge/Framework-Autourgos-orange.svg)](https://github.com/devxjitin)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://pypi.org/project/autourgos-starter/)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green.svg)](https://github.com/devxjitin/autourgos-starter/blob/main/LICENSE)
[![Author](https://img.shields.io/badge/Author-Jitin%20Kumar%20Sengar-blue.svg)](https://github.com/devxjitin)
![Contributor](https://img.shields.io/badge/Contributor-Sonia-blueviolet.svg)
![Contributor](https://img.shields.io/badge/Contributor-Vishwanil%20Suman-blueviolet.svg)

The fastest way to get a working [Autourgos](https://github.com/devxjitin) agent running. Bundles the
recommended default stack as real pip dependencies (nothing vendored or copied) and gives you one function
that wires them together.

```python
from autourgos_starter import create_starter_agent, tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

agent = create_starter_agent()
agent.add_tools(add)

result = agent.invoke("What is 12 + 30?")
print(result)
```

---

## Features

- **One function, one working agent** — `create_starter_agent()` wires `autourgos-agent` +
  `autourgos-openaichat` + `autourgos-buffer-memory` together with sensible defaults
- **Nothing vendored** — every dependency is a real, independently-installable, independently-maintained
  package
- **Optional scaffolding, not a requirement** — swap in a different memory or LLM backend any time by using
  `autourgos-agent` directly

---

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What's Actually Happening](#whats-actually-happening)
- [create_starter_agent() Reference](#create_starter_agent-reference)
- [Also Re-Exported](#also-re-exported)
- [License](#license)

---

## Install

```bash
pip install autourgos-starter
```

Set your API key:

```bash
export OPENAI_API_KEY="sk-..."
```

---

## Quick Start

This whole block is copy-pasteable — no placeholder variables to fill in.

```python
from autourgos_starter import create_starter_agent, tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

agent = create_starter_agent()
agent.add_tools(add)

result = agent.invoke("What is 12 + 30?")
print(result)
```

That's it — two lines to build the agent (`create_starter_agent()` and `agent.add_tools(add)`), one line to
run it (`agent.invoke(...)`).

---

## What's Actually Happening

`autourgos-starter` is just a convenience wrapper. `create_starter_agent()` does this:

```python
from autourgos_agent import Agent
from autourgos_openaichat import OpenAIChatModel
from autourgos_buffer_memory import ConversationBufferMemory

llm = OpenAIChatModel(model="gpt-4o-mini", api_key=None, system_instruction=None)
memory = ConversationBufferMemory()
agent = Agent(llm=llm, memory=memory)
```

Three real, independently-installable packages, each maintained on its own:

- [`autourgos-agent`](https://github.com/devxjitin/autourgos-agent) — the agent loop itself (`Agent`, `tool`).
- [`autourgos-openaichat`](https://github.com/devxjitin/autourgos-openaichat) — the LLM backend
  (`OpenAIChatModel`), talks to the OpenAI Chat Completions API or any OpenAI-compatible endpoint (set
  `base_url` to point at a local server such as Ollama, LM Studio, or vLLM).
- [`autourgos-buffer-memory`](https://github.com/devxjitin/autourgos-buffer-memory) — the memory backend
  (`ConversationBufferMemory`), an unbounded in-memory conversation buffer.

This package is optional scaffolding, not a requirement to use the Autourgos framework. If you want a
different memory backend (e.g. `autourgos-summary-memory`, `autourgos-token-memory`) or a different LLM
backend (e.g. `autourgos-responses`), skip `autourgos-starter` and wire `Agent` up to those packages directly
— that's exactly what this package does under the hood, just with sensible defaults picked for you.

---

## create_starter_agent() Reference

```python
def create_starter_agent(
    api_key: str | None = None,
    model: str = "gpt-4o-mini",
    system_prompt: str | None = None,
    **kwargs,
) -> Agent
```

| Argument | Default | Meaning |
|---|---|---|
| `api_key` | `None` | OpenAI API key. Falls back to the `OPENAI_API_KEY` env var if not given. |
| `model` | `"gpt-4o-mini"` | OpenAI model name, e.g. `"gpt-4o"`, `"gpt-4o-mini"`. |
| `system_prompt` | `None` | Optional system instruction, forwarded to `OpenAIChatModel`. |
| `**kwargs` | — | Forwarded to `Agent` — e.g. `verbose=True`, `max_iterations=10`, `memory=...` to override the default `ConversationBufferMemory`, `middleware=[...]`. |

Returns an `Agent` instance. Call `agent.add_tools(...)` before `agent.invoke(...)` / `agent.ainvoke(...)`.

---

## Also Re-Exported

So you don't need to know which sub-package a class lives in:

```python
from autourgos_starter import Agent, tool, OpenAIChatModel, ConversationBufferMemory
```

`ReactAgent` is also re-exported as a deprecated alias for `Agent`, for code written against the pre-rename
`autourgos-react-agent`-based version of this package.

---

## License

Apache License 2.0, Copyright (c) 2026 Jitin Kumar Sengar
