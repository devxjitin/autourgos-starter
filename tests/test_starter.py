"""
Tests for autourgos_starter.create_starter_agent().

No real network calls are made: OpenAIChatModel builds its HTTP client
lazily, so constructing it (and the ReactAgent around it) never touches
the network. We pass a fake API key and never call .invoke()/.ainvoke().
"""

from autourgos_react_agent import ReactAgent
from autourgos_openaichat import OpenAIChatModel
from autourgos_buffer_memory import ConversationBufferMemory

from autourgos_starter import (
    create_starter_agent,
    ReactAgent as ReExportedReactAgent,
    tool as re_exported_tool,
    OpenAIChatModel as ReExportedOpenAIChatModel,
    ConversationBufferMemory as ReExportedConversationBufferMemory,
)


def test_create_starter_agent_returns_react_agent():
    agent = create_starter_agent(api_key="sk-fake-test-key")
    assert isinstance(agent, ReactAgent)


def test_create_starter_agent_wires_openai_chat_model():
    agent = create_starter_agent(api_key="sk-fake-test-key")
    assert isinstance(agent.llm, OpenAIChatModel)
    assert agent.llm.model == "gpt-4o-mini"


def test_create_starter_agent_wires_conversation_buffer_memory():
    agent = create_starter_agent(api_key="sk-fake-test-key")
    assert isinstance(agent.memory, ConversationBufferMemory)


def test_create_starter_agent_respects_model_override():
    agent = create_starter_agent(api_key="sk-fake-test-key", model="gpt-4o")
    assert agent.llm.model == "gpt-4o"


def test_create_starter_agent_forwards_kwargs_to_react_agent():
    agent = create_starter_agent(api_key="sk-fake-test-key", verbose=True, max_iterations=5)
    assert agent.verbose is True
    assert agent.max_iterations == 5


def test_create_starter_agent_allows_memory_override():
    custom_memory = ConversationBufferMemory(name="custom")
    agent = create_starter_agent(api_key="sk-fake-test-key", memory=custom_memory)
    assert agent.memory is custom_memory


def test_reexports_match_underlying_classes():
    assert ReExportedReactAgent is ReactAgent
    assert ReExportedOpenAIChatModel is OpenAIChatModel
    assert ReExportedConversationBufferMemory is ConversationBufferMemory
    assert callable(re_exported_tool)


def test_add_tools_registers_tool_on_agent():
    """Confirms the add_tools() wiring works end-to-end at the tool-registry
    level (no LLM call involved, so no network and no dependency on the
    LLM-loop internals)."""
    agent = create_starter_agent(api_key="sk-fake-test-key")

    @re_exported_tool
    def add(a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b

    agent.add_tools(add)
    tool_names = [t["name"] if isinstance(t, dict) else t.name for t in agent.tools]
    assert "add" in tool_names
