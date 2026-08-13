import streamlit as st

# --- HEADER & BRANDING ---
st.title("EZERV Forge — AI Content Creation Agent")
st.caption("From ideation to execution — autonomously, with AI agents.")

# --- SIDEBAR CONFIGURATION (Rendered ONCE) ---
st.sidebar.header("⚙️ EZERV Forge Settings")

mode = st.sidebar.radio(
    "Choose Generation Mode:", 
    ["Automatic", "Manual"],
    key="mode_radio"
)

topic = st.sidebar.text_input(
    "Enter Content Topic / Keyword:",
    key="topic_input"
)

tone = st.sidebar.selectbox(
    "Select Content Tone:", 
    ["Professional", "Conversational", "Technical"],
    key="tone_selectbox"
)

generate_btn = st.sidebar.button(
    "Generate Content with EZERV Forge 🚀", 
    use_container_width=True,
    key="generate_btn"
)

# --- MAIN CONTENT AREA ---
st.divider()

if generate_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic in the sidebar to begin generation!")
    else:
        st.success(f"🚀 Starting EZERV Forge in **{mode}** mode for topic: **{topic}**")
        
        with st.spinner("🤖 AI Agents are generating your content..."):
            try:
                # Import inline to prevent circular dependencies
                from agents.planner import generate_outline
                
                outline = generate_outline(topic)
                
                st.subheader("📄 Generated Outline")
                st.markdown(outline)
                
            except Exception as e:
                st.error(f"An error occurred while fetching information: {e}")
else:
    st.info("👉 Fill out the settings in the left sidebar and click **Generate Content** to start!")