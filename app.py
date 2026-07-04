import streamlit as st
from agent import research
from memory import get_history
from export import create_pdf

st.set_page_config(
    page_title="Autonomous Research Agent",
    page_icon="🔍",
    layout="wide"
)

# -------------------- Session State --------------------

if "report" not in st.session_state:
    st.session_state.report = None

if "topic" not in st.session_state:
    st.session_state.topic = ""

# -------------------- Header --------------------

st.title("🔍 Autonomous Research Agent")
st.caption("Research • Analyze • Summarize using AI")

# -------------------- Sidebar --------------------

with st.sidebar:
    st.header("📜 Search History")

    history = get_history()

    if history:
        for item in reversed(history):
            st.write(f"• {item}")
    else:
        st.info("No previous searches yet.")

st.divider()

# -------------------- User Input --------------------

topic = st.text_input(
    "Enter a research topic",
    value=st.session_state.topic,
    placeholder="Example: Artificial Intelligence"
)

# -------------------- Research Button --------------------

if st.button("🚀 Start Research", use_container_width=True):

    if topic.strip():

        st.session_state.topic = topic

        try:
            with st.spinner("Researching... This may take a few seconds..."):
                report = research(topic)

            st.session_state.report = report

        except Exception as e:
            st.error(f"❌ Error: {e}")

    else:
        st.warning("Please enter a research topic.")

# -------------------- Display Report --------------------

if st.session_state.report:

    st.success("✅ Research completed successfully!")

    st.markdown(st.session_state.report)

    pdf_path = create_pdf(st.session_state.report)

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_file,
            file_name="Research_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )