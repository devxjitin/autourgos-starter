"""
autourgos-starter — Beginner-friendly starter bundle for the Autourgos framework.

Bundles the recommended default stack (autourgos-agent +
autourgos-openaichat + autourgos-buffer-memory) as real pip dependencies
and gives you one function to build a working agent in two lines::

    from autourgos_starter import create_starter_agent

    agent = create_starter_agent()
    result = agent.invoke("hello")
    print(result)

This package is optional scaffolding, not a requirement to use the
Autourgos framework. Everything here is a thin wrapper around the three
underlying packages — swap any piece out by using them directly.
"""

import logging
from typing import Optional

from autourgos_agent import Agent, tool
from autourgos_openaichat import OpenAIChatModel
from autourgos_buffer_memory import ConversationBufferMemory

logger = logging.getLogger(__name__)

from autourgos_core import package_version

__version__ = package_version("autourgos-starter", fallback="1.0.8", logger=logger)

# Deprecated alias, kept for backward compat with code written against the
# pre-rename autourgos-react-agent-based version of this package.
ReactAgent = Agent

__all__ = [
    "create_starter_agent",
    "Agent",
    "ReactAgent",
    "tool",
    "OpenAIChatModel",
    "ConversationBufferMemory",
]


def create_starter_agent(
    api_key: Optional[str] = None,
    model: str = "gpt-4o-mini",
    system_prompt: Optional[str] = None,
    **kwargs: object,
) -> Agent:
    """Build a ready-to-use Agent wired to OpenAIChatModel + ConversationBufferMemory.

    This is the recommended default stack for newcomers: the Autourgos
    agent loop (autourgos-agent), talking to the OpenAI Chat Completions
    API or any OpenAI-compatible endpoint (autourgos-openaichat), with an
    unbounded in-memory conversation buffer (autourgos-buffer-memory).

    Args:
        api_key: OpenAI API key. Falls back to the OPENAI_API_KEY env var
            if not given (see OpenAIChatModel).
        model: OpenAI model name, e.g. "gpt-4o-mini", "gpt-4o".
        system_prompt: Optional system instruction passed through to the
            underlying OpenAIChatModel.
        **kwargs: Forwarded to Agent (e.g. verbose=True, memory=...,
            max_iterations=..., middleware=...). Pass memory= to override
            the default ConversationBufferMemory.

    Returns:
        An Agent instance, ready for .invoke()/.ainvoke(). Add tools
        with agent.add_tools(...) before calling it.

    Example::

        from autourgos_starter import create_starter_agent, tool

        @tool
        def add(a: float, b: float) -> float:
            \"\"\"Add two numbers together.\"\"\"
            return a + b

        agent = create_starter_agent()
        agent.add_tools(add)
        print(agent.invoke("What is 2 + 2?"))
    """
    llm = OpenAIChatModel(model=model, api_key=api_key, system_prompt=system_prompt)
    memory = kwargs.pop("memory", None) or ConversationBufferMemory()
    return Agent(llm=llm, memory=memory, **kwargs)
