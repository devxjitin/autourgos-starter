# autourgos-starter — Features

A thin convenience wrapper, not a code-generator or project scaffold in the cookiecutter/create-react-app sense. `autourgos-starter` bundles three independently-installable, independently-maintained Autourgos packages (`autourgos-agent`, `autourgos-openaichat`, `autourgos-buffer-memory`) behind one function, `create_starter_agent()`, that wires them together with sensible defaults. Nothing is vendored or copied — it is a real pip dependency on the other three packages, and the whole "starter" surface is a single function plus some re-exports.

## Full Feature List

### Core
- `create_starter_agent(api_key=None, model="gpt-4o-mini", system_prompt=None, **kwargs)` — one function that constructs an `OpenAIChatModel` + `ConversationBufferMemory` + `Agent` with working defaults
- `**kwargs` forwarded straight to `Agent` (e.g. `verbose=True`, `max_iterations=10`, a custom `memory=`, `middleware=[...]`) — no special-casing, so anything `Agent` accepts is reachable without leaving this package
- `api_key` falls back to the `OPENAI_API_KEY` env var if not passed

### Composition, not vendoring
- Every piece (`autourgos-agent`, `autourgos-openaichat`, `autourgos-buffer-memory`) is a real, separately-versioned package — this wrapper is glue code, not a fork or copy
- Explicitly documented as optional: swapping to a different memory backend (e.g. `autourgos-summary-memory`, `autourgos-token-memory`) or LLM backend (e.g. `autourgos-responses`) means skipping this package and wiring `Agent` up directly — the README frames this as "exactly what this package does under the hood, just with sensible defaults picked for you"

### Convenience re-exports
- `Agent`, `tool`, `OpenAIChatModel`, `ConversationBufferMemory` all importable straight from `autourgos_starter`, so callers don't need to know which sub-package each class actually lives in
- `ReactAgent` re-exported as a deprecated alias for `Agent`, for backward compatibility with code written against the pre-rename `autourgos-react-agent`-based version

## Honesty note on "competitors"

This package is not a code generator, CLI scaffolding tool, or template repository — it produces no files, no directory structure, and no project layout. It is a runtime convenience function. As a result it has **no real product competitors** doing the same thing for the same framework (there is no other "one-function starter" for Autourgos). The comparison below is therefore against the closest analogous patterns in *other* ecosystems: framework-provided one-call agent constructors (the honest peer group) and, separately, true file-generating scaffolds (cookiecutter/CRA-style), included specifically to make clear that autourgos-starter is **not** that kind of tool.

---

## Competitor Comparison

| Capability | **autourgos-starter** | [LangChain `create_react_agent` (LangGraph)](https://reference.langchain.com/python/langgraph.prebuilt/chat_agent_executor/create_react_agent) | [LangChain `react-agent` starter template](https://github.com/langchain-ai/react-agent-js) | [Cookiecutter](https://cookiecutter.readthedocs.io/) (file-generating scaffold) | [Create React App](https://www.freecodecamp.org/news/how-to-build-a-react-project-with-create-react-app-in-10-steps/) (file-generating scaffold) |
|---|---|---|---|---|---|
| What it produces | An in-memory `Agent` instance, at runtime | An in-memory compiled agent graph, at runtime | An actual git repository/directory of starter files | An actual directory of files from a template, with variable substitution | An actual project directory with build tooling, dev server, test setup |
| Mechanism | One function call composing 3 real packages | One function call composing model + tools + prompt | Clone/copy a repo template, then edit | CLI walks a `cookiecutter.json` prompt, renders Jinja2 templates into new files | CLI runs `react-scripts` to generate a full project skeleton |
| Vendoring | None — pure runtime dependency on 3 separate packages | None — part of the LangGraph/LangChain package itself | The template repo is yours to edit; not "vendored" from an upstream dependency either | Templates are copied and become fully yours (no residual dependency on cookiecutter itself) | Historically bundled `react-scripts`, i.e. more vendored/opinionated tooling than a plain template |
| Swappable components | Explicitly yes — memory or LLM backend swap documented as "skip this package, wire `Agent` directly" | Model/tools/prompt are constructor args, swappable | Whatever you choose to change after cloning | Whatever you choose to change after generation | Ejecting is possible but historically discouraged/one-way |
| Ongoing maintenance model | Each of the 3 wrapped packages maintained independently; this wrapper stays tiny | Maintained as part of LangGraph's own release cycle | A template repo, updated (or not) independently of LangChain core | Templates are community-maintained, independently of the cookiecutter tool | react-scripts saw maintenance slow down industry-wide in recent years, pushing users toward Vite-based alternatives |
| Scope | Minimal: one agent + one LLM + one memory, nothing else | Minimal: one agent-construction call, framework handles the rest | Broader: a runnable app skeleton (routes, config, etc.) | Broader: an entire project structure, potentially many files | Broadest: a full toolchain (bundler, dev server, test runner) |

### How to read this

- **vs. `create_react_agent`-style one-call constructors (LangGraph)**: this is the fairest, most direct comparison — both are "wire the pieces together with defaults" runtime functions, not file generators. LangGraph's version is deeper into that ecosystem's own agent/tool/graph model; autourgos-starter is narrower (LLM + memory + agent, nothing about graphs/planning) but arguably even simpler to read end-to-end since it wraps only three small packages.
- **vs. a starter-template *repository*** (e.g. `react-agent-js`): a cloned repo gives you routing, config files, and a runnable app skeleton to edit in place — a materially bigger head start, but also more to understand and more that can drift from upstream over time. autourgos-starter gives you zero files to maintain; you still write your own application code around the function call.
- **vs. cookiecutter/CRA-style scaffolds**: these generate real files onto disk and are the right comparison for "starter template" in the traditional sense — but that's a different problem (project structure, build tooling) than what autourgos-starter solves (wiring three already-installed runtime objects together). Calling autourgos-starter a competitor to cookiecutter or CRA would be misleading; it doesn't scaffold a project at all.

Sources:
- [create_react_agent | langgraph.prebuilt | LangChain Reference](https://reference.langchain.com/python/langgraph.prebuilt/chat_agent_executor/create_react_agent)
- [Quickstart - Docs by LangChain](https://docs.langchain.com/oss/python/langchain/quickstart)
- [GitHub - langchain-ai/react-agent-js](https://github.com/langchain-ai/react-agent-js)
- [Getting to Know Cookiecutter — cookiecutter docs](https://cookiecutter.readthedocs.io/en/1.7.2/tutorial1.html)
- [GitHub - konstantint/cookiecutter-python-boilerplate](https://github.com/konstantint/cookiecutter-python-boilerplate)
- [How to Build a React Project with Create React App in 10 Steps](https://www.freecodecamp.org/news/how-to-build-a-react-project-with-create-react-app-in-10-steps/)
- [Alternative To create-react-app: A Minimal Solution with Smaller Size](https://medium.com/@afiiyahsarief_/alternative-to-create-react-app-a-minimal-solution-with-smaller-size-d91d077df4a4)
