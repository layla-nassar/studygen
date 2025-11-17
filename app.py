import streamlit as st

st.set_page_config(
    page_title="StudyGen Pro",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.markdown("<h1 style='color:#A57CFF;'>📚 StudyGen Pro</h1>", unsafe_allow_html=True)
st.sidebar.write("Your AI-powered study assistant.")
st.sidebar.markdown("---")
st.sidebar.success("Select a tool from the sidebar to begin.")
st.sidebar.markdown("---")

st.markdown("""
# <span style="color:#A57CFF;">Welcome to StudyGen Pro</span>

A simple and effective AI-powered study assistant powered by GPT-4o-mini.

### Tools Included
- 🧠 Study Guide Generator  
- 🗂️ Flashcard Creator  
- ❓ Quiz Generator  
- 💬 Chat With Notes (Optional)

All text-based. Fast. Stable. Error-free.

Use the sidebar on the left to choose a tool.
""", unsafe_allow_html=True)
