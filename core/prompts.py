from langchain_core.messages import SystemMessage


def get_system_prompt(mode):
    prompts = {
        "chat": "You are a helpful assistant.",
        "code": "You are an expert programmer.",
        "academic": "You are a tutor explaining concepts clearly.",
        "prompt": "You generate high-quality prompts.",
        "translate": "You translate languages accurately."
    }
    return SystemMessage(content=prompts.get(mode, "You are helpful."))