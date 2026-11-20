
import streamlit as st

st.set_page_config(
    page_title="Weird Psychology AI Studio",
    page_icon="🧠"
)

st.title("🧠 Weird Psychology AI Studio")
st.subheader("YouTube Shorts Content Assistant")

st.header("1. Video Topic")
topic = st.text_input("Enter your video topic")

st.header("2. Video Script")
hook = st.text_area("Strong Hook")
script = st.text_area("Full Voice-over Script")

st.header("3. Visual Planning")
scenes = st.text_area("Stickman Scene Prompts")

st.header("4. Upload Details")
title = st.text_input("YouTube Title")
description = st.text_area("Video Description")
hashtags = st.text_input("Hashtags")

if st.button("Create Upload Pack"):
    if not topic or not script:
        st.warning("Please enter topic and script first.")
    else:
        pack = f"""
TOPIC:
{topic}

HOOK:
{hook}

VOICE-OVER:
{script}

VISUAL SCENES:
{scenes}

TITLE:
{title}

DESCRIPTION:
{description}

HASHTAGS:
{hashtags}
"""
        st.success("Your Upload Pack is Ready!")

        st.text_area("Your Complete Upload Pack", pack, height=400)

        st.download_button(
            "Download Upload Pack",
            pack,
            file_name="youtube_upload_pack.txt"
        )

st.caption("Made for Weird Psychology SJX")
