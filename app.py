import base64
import streamlit as st

# Function to encode image file to base64 for HTML circular framing
def get_image_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# --- HEADER & BRANDING ---
col1, col2 = st.columns([1, 5])

with col1:
    try:
        img_b64 = get_image_base64("logo.png")
        # Renders the logo inside a circular frame
        st.markdown(
            f"""
            <div style="
                width: 90px;
                height: 90px;
                border-radius: 50%;
                overflow: hidden;
                border: 2px solid #FF4B4B;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            ">
                <img src="data:image/png;base64,{img_b64}" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception:
        st.warning("Please ensure 'logo.png' is saved in your project folder.")

with col2:
    st.title("EZERV Forge — AI Content Creation Agent")
    st.caption("🚀 *From ideation to execution — autonomously, with AI agents.*")
    # --- SIDEBAR CONFIGURATION ---
st.sidebar.header("⚙️ EZERV Forge Settings")

# 1. Mode Selection (Automatic / Manual)
mode = st.sidebar.radio(
    "Choose Generation Mode:",
    ["Automatic", "Manual"],
    help="Automatic generates everything instantly. Manual lets you review each step."
)

# 2. Topic Input
topic = st.sidebar.text_input(
    "Enter Content Topic / Keyword:",
    value="",
    placeholder="e.g., Future of AI in Software Testing"
)

# 3. Tone & Style Settings
tone = st.sidebar.selectbox(
    "Select Content Tone:",
    ["Professional", "Conversational", "Technical & Detailed", "Engaging & Creative"]
)

# 4. Generate Button
generate_btn = st.sidebar.button("Generate Content with EZERV Forge 🚀", use_container_width=True)

# --- MAIN CONTENT AREA ---
st.divider()

if generate_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic in the sidebar to begin generation!")
    else:
        st.success(f"🚀 Starting EZERV Forge in **{mode}** mode for topic: **{topic}**")
        st.info(f"Target Tone: **{tone}**")
        # Agent execution logic will trigger here
else:
    st.info("👈 Fill out the settings in the left sidebar and click **Generate Content** to start!")