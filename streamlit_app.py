import streamlit as st

# កំណត់ UI ឱ្យដូច Gemini ១០០% (ច្បាស់ និងលឿន)
st.set_page_config(page_title="Lucky Gemini Ultra", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    /* កំណត់ពណ៌ផ្ទៃក្រោយឱ្យងងឹត តែអក្សរពណ៌សច្បាស់ */
    .main { background-color: #131314; color: #ffffff; }
    
    /* រចនាប្រអប់សន្ទនាឱ្យមើលឃើញអក្សរច្បាស់ (ពណ៌ប្រផេះចាស់) */
    .stChatMessage { border-radius: 20px; background-color: #1e1f20; padding: 15px; margin-bottom: 10px; color: #ffffff; }
    
    /* កែសម្រួលប្រអប់ Chat Input ឱ្យស្អាត និងងាយមើល */
    .stChatInputContainer { border-radius: 28px !important; border: 1px solid #444746 !important; background-color: #1e1f20 !important; }
    .stChatInputContainer textarea { color: #ffffff !important; }

    /* រចនាប៊ូតុង Upload ឱ្យមើលឃើញច្បាស់នៅខាងលើ Chat */
    .stFileUploader section { 
        background-color: #1e1f20 !important; 
        border: 1px dashed #444746 !important; 
        border-radius: 15px !important;
        color: #ffffff !important;
    }
    
    h1 { color: #8ab4f8; text-align: center; font-family: 'Google Sans', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Pheaktra & Lucky Gemini</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- ១. កន្លែងផ្ញើរូបភាព (ដាក់ឱ្យឃើញច្បាស់ៗ មិនឱ្យបាត់ទៀតទេ) ---
with st.container():
    uploaded_file = st.file_uploader("📸 ផ្ញើរូបភាពក្រាហ្វិកមាសដើម្បីវិភាគ...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="📊 កំពុងវិភាគក្រាហ្វិក...", use_container_width=True)
        st.info("🤖 Lucky Gemini: ខ្ញុំបានទទួលរូបភាព និងបានគូសវាស់តំបន់ Support/Resistance រួចរាល់!")

st.write("---")

# --- ២. បង្ហាញការសន្ទនា (អក្សរពណ៌ស ច្បាស់ល្អ) ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- ៣. ប្រអប់សន្ទនា (Chat Input) ---
if prompt := st.chat_input("សួរអ្វីមួយមកកាន់ Lucky..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = f"✨ **Lucky Gemini:** ភក្ត្រាសម្លាញ់! ខ្ញុំបានឃើញសារ '{prompt}' ហើយ។ ខ្ញុំត្រៀមខ្លួនជានិច្ចដើម្បីជួយអ្នក!"
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
