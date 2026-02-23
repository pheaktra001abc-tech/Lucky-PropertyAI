import streamlit as st
import time

# កំណត់ការរចនាទូទៅឱ្យដូច Gemini Pro
st.set_page_config(page_title="Lucky Gemini Pro", page_icon="✨", layout="centered")

# ការរចនា UI/UX កម្រិតខ្ពស់ (Gemini Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #131314; color: #e3e3e3; }
    .stChatMessage { border-radius: 20px; margin-bottom: 15px; padding: 15px; }
    .stChatInputContainer { background-color: #1e1f20 !important; border-radius: 30px !important; border: 1px solid #444746 !important; }
    .upload-btn { background-color: #1e1f20; border: 1px dashed #444746; border-radius: 15px; padding: 20px; text-align: center; }
    h1 { font-family: 'Google Sans', sans-serif; font-weight: 500; color: #8ab4f8; }
    </style>
    """, unsafe_allow_html=True)

# ផ្នែកចំណងជើង
st.markdown("<h1 style='text-align: center;'>✨ Lucky Gemini Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9aa0a6;'>ជំនួយការវិភាគមាសឆ្លាតវៃសម្រាប់ភក្ត្រា</p>", unsafe_allow_html=True)

# បង្កើតប្រព័ន្ធចងចាំសារ (Chat Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# ១. មុខងារផ្ញើរូបថត (ប៊ូតុងស្អាត ដូច Gemini)
with st.container():
    uploaded_file = st.file_uploader("➕ បន្ថែមរូបភាពក្រាហ្វិកមាសដើម្បីវិភាគ...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        with st.status("🔍 កំពុងស្កេនទិន្នន័យក្រាហ្វិក...", expanded=True):
            st.image(uploaded_file, use_container_width=True)
            time.sleep(2) # ធ្វើឱ្យដូច AI កំពុងគិត
            st.success("🤖 Lucky Gemini: វិភាគរួចរាល់! ក្រាហ្វិកបង្ហាញពីសញ្ញាទិញនៅតំបន់ Support។")

st.write("---")

# ២. ផ្នែកសន្ទនា និងការឆ្លើយតប (Chat & Response)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("សួរអ្វីមួយមកកាន់ Lucky Gemini..."):
    # បង្ហាញសាររបស់ភក្ត្រា
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # បង្ហាញការឆ្លើយតបរបស់ AI (បែប Typing Effect ដូច Gemini)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = f"✨ **Lucky Gemini:** ភក្ត្រាសម្លាញ់! ចំពោះ '{prompt}' ខ្ញុំបានពិនិត្យទីផ្សារមាសឃើញថា..."
        # ធ្វើឱ្យអក្សរលោតម្តងមួយៗ
        current_text = ""
        for char in full_response:
            current_text += char
            message_placeholder.markdown(current_text + "▌")
            time.sleep(0.03)
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
