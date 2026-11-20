import streamlit as st

st.set_page_config(
    page_title="Weird Psychology AI Studio",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Weird Psychology AI Studio")
st.caption("Your YouTube Shorts Production Assistant")

st.header("1. Enter Video Topic")

topic = st.text_input(
    "Video topic",
    placeholder="Example: Why You Overthink at Night"
)

duration = st.selectbox(
    "Video duration",
    ["30 seconds", "45 seconds", "60 seconds"]
)

st.header("2. Production Style")

style = st.selectbox(
    "Visual style",
    [
        "Minimalist black stickman on white background",
        "Dark psychology cinematic stickman"
    ]
)

st.header("3. Generate Production Prompt")

if st.button("Generate AI Production Prompt", type="primary"):

    if not topic.strip():
        st.warning("Please enter a video topic.")
    else:

        prompt = f"""
You are the expert content director for my YouTube
channel Weird Psychology SJX.

VIDEO TOPIC:
{topic}

VIDEO DURATION:
{duration}

TARGET AUDIENCE:
USA viewers. Use simple, natural American English.

VISUAL STYLE:
{style}

IMPORTANT REQUIREMENTS:

1. Create a powerful, curiosity-driven opening hook.
2. Write a complete voice-over script matching the duration.
3. Keep the storytelling engaging until the end.
4. Divide the video into exactly 8 scenes.
5. Give 8 separate detailed IMAGE PROMPTS.
6. Give 8 matching VEO 3.1 VIDEO PROMPTS.
7. Every video prompt must match its image prompt.
8. Add camera movement, animation, transitions
   and sound effects to every video prompt.
9. Scene 1 must start with fast, attention-grabbing action.
10. Keep the main stickman character consistent.

STICKMAN CHARACTER LOCK:
Simple black stickman, big round white head,
thick 6px black outline, small dot eyes,
no mouth, no nose, clean white background.
Use red only for important visual emphasis.
No gradients, no 3D, no realistic human characters.

OUTPUT FORMAT:

A. VIDEO HOOK

B. COMPLETE VOICE-OVER SCRIPT
Simple American English with emotion cues.

C. 8 IMAGE PROMPTS
Number each scene from 1 to 8.
Describe character, action, background and composition.

D. 8 MATCHING VEO 3.1 VIDEO PROMPTS
Number each scene from 1 to 8.
Include movement, camera direction, effects and timing.

E. YOUTUBE TITLE
Give 3 clickable title options.

F. DESCRIPTION

G. HASHTAGS

H. FINAL UPLOAD CHECKLIST

Make everything original, engaging and ready for
production in Google Flow.
"""

        st.success("Your production prompt is ready!")

        st.text_area(
            "Copy this prompt into ChatGPT",
            prompt,
            height=450
        )

        st.download_button(
            "Download Production Prompt",
            prompt,
            file_name="psychology_production_prompt.txt",
            mime="text/plain"
        )

st.divider()
st.caption("Made for Weird Psychology SJX")
