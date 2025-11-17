import streamlit as st
from utils.ai_utils import ask_gpt

st.title("💬 Chat With Your Notes")

notes = st.text_area("Paste your notes here:")

question = st.text_input("Ask a question about your notes:")

if st.button("Ask"):
    if notes.strip() and question.strip():
        with st.spinner("Thinking..."):
            prompt = f"Here are my notes:\n\n{notes}\n\nAnswer this question using ONLY the notes: {question}"
            answer = ask_gpt(prompt)
            st.markdown(answer)
    else:
        st.error("Please enter both notes and a question.")
