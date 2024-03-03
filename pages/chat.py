import streamlit as st
from streamlit_chatbox import *
import time
import simplejson as json

# Initialize chat_box and FakeLLM
llm = FakeLLM()
chat_box = ChatBox()

# Sidebar configuration
with st.sidebar:
    st.subheader('Start chatting using Streamlit')
    streaming = st.checkbox('Streaming', True)
    in_expander = st.checkbox('Show messages in expander', True)
    show_history = st.checkbox('Show history', False)
    st.divider()
    btns = st.container()
    file = st.file_uploader("Chat history JSON", type=["json"])

# Initialize chat_history in session state if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Load chat history from JSON file if available
if btns.button("Load JSON") and file:
    data = json.load(file)
    st.session_state['chat_history'] = data

# Use chat_box to output messages and handle user input
chat_box.init_session()
chat_box.output_messages()

if query := st.chat_input('Input your question here'):
    chat_box.user_say(query)
    if streaming:
        generator = llm.chat_stream(query)
        for x, docs in generator:
            text = x
            chat_box.ai_say(text, in_expander=in_expander)
    else:
        text, docs = llm.chat(query)
        chat_box.ai_say(text, in_expander=in_expander)

# Additional buttons and functionality
cols = st.columns(2)
if cols[0].button('Show multimedia'):
    # Example multimedia content
    chat_box.ai_say("Example multimedia content.")

if cols[1].button('Run agent'):
    chat_box.user_say('Run agent')
    # Example agent functionality
    chat_box.ai_say("Agent response.")

# Export chat history buttons
btns.download_button("Export Markdown", "".join(chat_box.export2md()), file_name="chat_history.md", mime="text/markdown")
btns.download_button("Export JSON", chat_box.to_json(), file_name="chat_history.json", mime="text/json")

# Clear history button
if btns.button("Clear history"):
    st.session_state['chat_history'] = []
    st.experimental_rerun()

# Display chat history if option is enabled
if show_history:
    st.write(st.session_state['chat_history'])