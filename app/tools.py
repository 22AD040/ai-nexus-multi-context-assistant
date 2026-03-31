from langchain_core.messages import ToolMessage


def calculator_tool(query):
    try:
        return ToolMessage(content=str(eval(query)))
    except:
        return ToolMessage(content="Calculation Error")