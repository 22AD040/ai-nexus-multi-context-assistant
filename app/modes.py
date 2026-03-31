from langchain_core.messages import HumanMessage, AIMessage
from app.llm import llm
from core.prompts import get_system_prompt
from app.memory import save_memory, retrieve_memory


def run_mode(mode, user_input, chat_history):
    system = get_system_prompt(mode)
    memory_context = retrieve_memory(user_input)

    messages = [system]
    messages += chat_history
    messages.append(HumanMessage(content=user_input + "\nContext:" + memory_context))

    response = llm.invoke(messages)

    save_memory(user_input)
    save_memory(response.content)

    return AIMessage(content=response.content)