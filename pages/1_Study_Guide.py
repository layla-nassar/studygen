import streamlit as st
from utils.ai_utils import ask_gpt

st.title("🧠 Study Guide Generator")

topic = st.text_input("Enter your topic:")

if st.button("Generate Study Guide"):
    if topic.strip():
        with st.spinner("Creating your study guide..."):
            prompt = f"Create a detailed, organized, beginner-friendly study guide about: {topic}."
            result = ask_gpt(prompt)
            st.markdown(result)
    else:
        st.error("Please enter a topic.")
