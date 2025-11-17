import streamlit as st
from utils.ai_utils import ask_gpt

st.title("🗂️ Flashcard Generator")

topic = st.text_input("Enter topic:")

if st.button("Generate Flashcards"):
    if topic.strip():
        with st.spinner("Generating flashcards..."):
            prompt = f"Generate 15 flashcards for {topic}. Format as Q/A pairs."
            output = ask_gpt(prompt)
            st.markdown(output)
