# research-intelligence-agent
Building a production-ready AI research agent from first principles — search, analysis, planning, tools, skills, evaluation, and agent orchestration.

## Start With
1) basic_tool_call_without_loop
2) looped_tool_call
3) looped_tool_call_with_registry

exposing how tool call and messaging works

### Learning Progress — Building an Agent from First Principles

So far, this project has built the basic agent execution flow without using a pre-built agent or orchestration framework.

#### What We Built

- Connected to **arXiv** to search research papers.
- Wrapped the arXiv search capability as a LangChain `@tool`.
- Connected an LLM using **ChatGroq**.
- Used `bind_tools()` to expose available tools to the LLM.
- Learned that `bind_tools()` only tells the LLM which tools are available — it does **not execute them**.
- Inspected `response.tool_calls` to understand which tool the LLM wants to execute and with what arguments.
- Executed the selected tool using `tool.invoke(tool_call["args"])`.
- Returned tool results to the LLM using `ToolMessage`.
- Maintained conversation state using `HumanMessage`, `AIMessage`, and `ToolMessage`.
- Built a manual agent loop that continues until the LLM no longer requests a tool.

### Core Mental Model

```text
User
  ↓
LLM
  ↓
Tool needed?
  ├── No → Final Answer
  │
  └── Yes
       ↓
    ToolCall
       ↓
    Execute Tool
       ↓
    ToolMessage
       ↓
      LLM
       ↓
    Repeat...
```

This is the fundamental agent cycle:

**Reason → Act → Observe → Reason**

The LLM decides **what should happen**, while the application runtime is responsible for **actually executing tools and controlling the loop**.

This manual implementation gives us the foundation for understanding why agent orchestration frameworks such as LangGraph exist.
