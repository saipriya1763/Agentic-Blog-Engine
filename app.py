import streamlit as st

# --- HEADER & BRANDING ---
st.title("EZERV Forge — AI Content Creation Agent")
st.caption("From ideation to execution — autonomously, with AI agents.")

# --- SIDEBAR CONFIGURATION (Defined ONCE) ---
st.sidebar.header("⚙️ EZERV Forge Settings")

mode = st.sidebar.radio("Choose Generation Mode:", ["Automatic", "Manual"])
topic = st.sidebar.text_input("Enter Content Topic / Keyword:")
tone = st.sidebar.selectbox("Select Content Tone:", ["Professional", "Conversational", "Technical"])

# Unique key added to prevent duplicate button errors
generate_btn = st.sidebar.button("Generate Content with EZERV Forge 🚀", use_container_width=True, key="main_generate_btn")

# --- MAIN CONTENT AREA ---
st.divider()

if generate_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic in the sidebar to begin generation!")
    else:
        st.success(f"🚀 Starting EZERV Forge in **{mode}** mode for topic: **{topic}**")
        
        with st.spinner("🤖 AI Agents are generating your content..."):
            try:
                # Import planner inside button execution to avoid circular imports
                from agents.planner import generate_outline
                
                outline = generate_outline(topic)
                
                st.subheader("📄 Generated Outline")
                st.markdown(outline)
                
            except Exception as e:
                st.error(f"An error occurred while fetching information: {e}")
else:
    st.info("👉 Fill out the settings in the left sidebar and click **Generate Content** to start!")