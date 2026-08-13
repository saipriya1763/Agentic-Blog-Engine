import streamlit as st
from agents.planner import generate_outline
from agents.writer import write_blog_post
from agents.editor import review_blog_post
import random

st.set_page_config(page_title="Agentic Blog Engine", layout="wide")

st.title("🚀 Agentic Blog Engine")
st.write("Generate professional, multi-agent AI blogs tailored for LinkedIn and social media!")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("Blog Generation Settings")

# Enhancement 1: Mode Selector (Manual vs Automatic)
mode = st.sidebar.radio("Choose Generation Mode:", ["Manual", "Automatic"])

topic = ""

if mode == "Manual":
    st.sidebar.subheader("Manual Input")
    topic = st.sidebar.text_input("Enter your custom blog topic:", "Introduction to Agentic Workflows")

else:  # Automatic Mode
    st.sidebar.subheader("Automatic Discovery")
    if st.sidebar.button("Discover Trending Topic"):
        # Enhancement 1: Backend prompt/pool for trending tech topics
        trending_topics = [
            "Breakthroughs in Quantum Computing for 2026",
            "Advanced Multi-Agent Software Engineering Workflows",
            "Next-Gen Rocket Propulsion and Aerospace Technology",
            "The Rise of Autonomous AI Agents in Data Science",
            "Edge AI and Scalable Microservices Architecture"
        ]
        selected_topic = random.choice(trending_topics)
        st.sidebar.success(f"Selected: {selected_topic}")
        topic = selected_topic
    else:
        topic = st.sidebar.text_input("Current Auto-Topic (or click button above):", "Autonomous AI Agents in Data Science")

# Enhancement 2: Style Selector emphasizing Social Media / LinkedIn format
post_style = st.sidebar.selectbox(
    "Select Output Format Style:",
    ["LinkedIn Tech Post (Engaging, Infographic style, Emojis)", "Standard Social Media Thread"]
)

if st.button("Generate Blog Post 🤖"):
    if not topic:
        st.warning("Please provide or generate a topic first!")
    else:
        with st.status("Agents at work...", expanded=True) as status:
            st.write("Planner Agent: Structuring the outline...")
            outline = generate_outline(topic)
            
            st.write("Writer Agent: Drafting content with social media layout...")
            # Pass style instructions to the writer
            raw_draft = write_blog_post(topic, outline, style=post_style)
            
            st.write("Editor Agent: Polishing tone and layout...")
            final_blog = review_blog_post(raw_draft)
            
            status.update(label="Blog generation complete!", state="complete", expanded=False)

        st.subheader("Generated Blog Output")
        st.markdown(final_blog)
        
        # Download button for mentor review
        st.download_button(
            label="Download Blog Post (.md)",
            data=final_blog,
            file_name="social_blog_post.md",
            mime="text/markdown"
        )