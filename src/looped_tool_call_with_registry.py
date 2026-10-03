from src.tools.paper_search import (search_research_papers)
from src.llm.groq import create_chat_groq
from langchain_core.messages import HumanMessage, AIMessage,ToolMessage, BaseMessage

TOOL_REGISTRY = {
    "search_research_papers": search_research_papers
}

def main():
    llm = create_chat_groq()
    tools = list(TOOL_REGISTRY.values())
    llm_with_tools = llm.bind_tools(tools)
    messages:list[BaseMessage] = [
       HumanMessage(content="find three research papers on AI")
    ]
    response = llm_with_tools.invoke(messages)
    messages.append(response)
    while response.tool_calls:
        for tool_call in response.tool_calls:
            tool = TOOL_REGISTRY.get(tool_call["name"])
            if tool:
                result = tool.invoke(tool_call["args"])
                messages.append(ToolMessage(content=str(result), tool_call_id = tool_call["id"]))
        response = llm_with_tools.invoke(messages)
        messages.append(response)
    print(response)

if __name__ == "__main__":
    main()
