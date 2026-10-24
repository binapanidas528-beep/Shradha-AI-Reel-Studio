import streamlit as st
import os
from main import generate_reel

st.set_page_config(page_title="Shradha AI Reel Studio", layout="wide", page_icon="🎬")

st.title("🎬 Shradha AI Reel Studio")
st.write("Generate engaging social media reels with AI-driven captions and background music!")

# Sidebar for controls
st.sidebar.header("Reel Settings")
script_text = st.sidebar.text_area("Script / Prompt", "Welcome to Shradha AI Reel Studio! Let's create amazing reels easily.")
bgm_option = st.sidebar.selectbox("Background Music", ["Default Music", "No Music"])

if st.sidebar.button("🚀 Generate Reel"):
    with st.spinner("Processing video, captions, and audio..."):
        try:
            output_path = generate_reel(script_text, bgm_option)
            st.success("Reel generated successfully!")
            
            # Display video
            st.video(output_path)
            
            # Audio Preview
            st.audio(output_path, format="video/mp4")
            
            with open(output_path, "rb") as file:
                st.download_button(
                    label="📥 Download Reel",
                    data=file,
                    file_name="shradha_ai_reel.mp4",
                    mime="video/mp4"
                )
        except Exception as e:
            st.error(f"Error generating reel: {e}")
