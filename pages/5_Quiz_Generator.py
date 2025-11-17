import streamlit as st
from utils.ai_utils import ask_gpt

st.title("❓ Quiz Generator")

topic = st.text_input("Enter topic:")

if st.button("Generate Quiz"):
    if topic.strip():
        with st.spinner("Creating quiz..."):
            prompt = f"Create a 10-question multiple choice quiz on: {topic}. Add answer key at bottom."
            output = ask_gpt(prompt)
            st.markdown(output)
