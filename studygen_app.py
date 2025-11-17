import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="StudyGen", page_icon="📚", layout="wide")

st.title("📚 StudyGen: AI-Powered Study Guide Generator")

topic = st.text_input("Enter a topic you want to study:")

if st.button("Generate Study Guide"):
    if not topic.strip():
        st.error("Please enter a topic first.")
    else:
        with st.spinner("Generating your study guide..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert tutor who explains topics clearly and simply."},
                    {"role": "user", "content": f"Create a detailed study guide on: {topic}"}
                ],
            )
            study_guide = response.choices[0].message["content"]
            st.success("Done!")
            st.write(study_guide)
