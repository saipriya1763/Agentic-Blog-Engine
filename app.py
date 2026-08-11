import streamlit as st
from main import app  # Imports your compiled LangGraph workflow

# Page Configuration
st.set_page_config(page_title="Agentic Blog Engine", page_icon="🤖", layout="centered")

st.title("🤖 Agentic Blog Engine")
st.markdown("Enter a topic below to let your **Planner**, **Writer**, and **Editor** agents collaborate and generate a published draft.")

# Input Field
topic = st.text_input("Blog Topic", placeholder="e.g., The Impact of Quantum Computing on Cybersecurity")

# Action Button
if st.button("Generate Article", type="primary"):
    if not topic.strip():
        st.warning("Please enter a valid topic!")
    else:
        # Animated Status Container
        status = st.status("🤖 Agents are working on your article...", expanded=True)
        
        with status:
            st.write("📝 **Planner Agent:** Drafting structured outline...")
            initial_state = {"topic": topic, "outline": "", "draft": "", "final_post": ""}
            
            # Run LangGraph pipeline
            final_state = app.invoke(initial_state)
            
            st.write("✍️ **Writer Agent:** Writing detailed draft...")
            st.write("🔍 **Editor Agent:** Polishing tone, style, and adding key takeaways...")
            status.update(label="🎉 Article complete!", state="complete", expanded=False)

        # Output Section
        st.subheader("📄 Generated Article")
        st.markdown(final_state["final_post"])

        st.divider()

        # Download Button
        file_name = f"{topic.lower().replace(' ', '_')[:30]}.md"
        st.download_button(
            label="📥 Download Article (.md)",
            data=final_state["final_post"],
            file_name=file_name,
            mime="text/markdown"
        )