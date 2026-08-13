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