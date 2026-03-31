import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.messages import HumanMessage, AIMessage
from app.modes import run_mode

st.set_page_config(page_title="AI Nexus", layout="wide")

st.title("🧠 AI Nexus Assistant")

with st.sidebar:
    st.header("⚙️ Controls")

    mode = st.selectbox("Select Mode", [
        "chat", "code", "academic", "prompt", "translate"
    ])

    if st.button("🆕 New Chat"):
        st.session_state.history = []
        st.success("New chat started!")

if "history" not in st.session_state:
    st.session_state.history = []

if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:
    st.session_state.history = []
    st.session_state.current_mode = mode

for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

def get_spinner(mode):
    return {
        "chat": "💬 Thinking...",
        "code": "💻 Writing code...",
        "academic": "📚 Explaining concept...",
        "prompt": "✨ Generating prompt...",
        "translate": "🌍 Translating..."
    }.get(mode, "Thinking...")


user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    st.session_state.history.append(HumanMessage(content=user_input))

    with st.chat_message("assistant"):
        with st.spinner(get_spinner(mode)):
            try:
                response = run_mode(mode, user_input, st.session_state.history)

               
                if response and hasattr(response, "content"):
                    st.session_state.history.append(response)
                    st.write(response.content)
                else:
                    st.error("Empty response from model")

            except Exception as e:
                st.error(f"Error: {e}")