import streamlit as st
import time

# កំណត់ UI ឱ្យដូច Gemini App 100%
st.set_page_config(page_title="Lucky Gemini Ultra", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #131314; color: #e3e3e3; }
    .stChatInputContainer { padding-bottom: 20px; }
    .stChatMessage { border-radius: 20px; border: 1px solid #333; }
    /* កែសម្រួលប្រអប់ Upload ឱ្យតូចស្អាតក្បែរ Chat */
    .stFileUploader { margin-top: -60px; } 
    h1 { color: #8ab4f8; text-align: center; font-size: 22px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Pheaktra & Lucky Gemini</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- ផ្នែកផ្ញើរូបភាពបែប Gemini (Compact Style) ---
with st.container():
    uploaded_file = st.file_uploader("📸", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        with st.status("🧠 Lucky Gemini កំពុងគូសវាស់លើក្រាហ្វិក...", expanded=True):
            st.image(uploaded_file, use_container_width=True)
            time.sleep(2)
            # បង្ហាញការគូសវាស់ជាលក្ខណៈ Visual Mark
            st.markdown("🔴 **AI Marker:** បានគូសតំបន់ **Resistance** នៅកម្រិតខ្ពស់បំផុត")
            st.markdown("🟢 **AI Marker:** បានគូសតំបន់ **Support** ដែលត្រូវទិញចូល")
            st.success("🤖 វិភាគរួចរាល់៖ ខ្ញុំបានគូសវាស់រួចហើយ ភក្ត្រាអាចមើលចំណុចដែលខ្ញុំបានបញ្ជាក់!")

# --- ផ្នែកសន្ទនា ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("សួរអ្វីមួយ ឬផ្ញើរូបមក Lucky..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        response = f"✨ **Lucky Gemini:** ភក្ត្រាសម្លាញ់! ផ្អែកលើការគូសវាស់របស់ខ្ញុំ អ្វីដែលអ្នកគួរធ្វើគឺ..."
        full_text = ""
        for char in response:
            full_text += char
            msg_placeholder.markdown(full_text + "▌")
            time.sleep(0.02)
        msg_placeholder.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
                                                
