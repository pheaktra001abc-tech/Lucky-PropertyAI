import streamlit as st

# កំណត់ការរចនាទូទៅឱ្យដូច Gemini
st.set_page_config(page_title="Pheaktra & Lucky Gemini", page_icon="💎", layout="centered")

# ការរចនា CSS ដើម្បីឱ្យដូច Gemini App
st.markdown("""
    <style>
    .main { background-color: #131314; color: #e3e3e3; }
    .stChatInputContainer { bottom: 20px !important; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; }
    h1 { color: #4285f4; text-align: center; font-family: 'Inter', sans-serif; }
    .stFileUploader { border: 1px dashed #444746; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Pheaktra & Lucky Gemini</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8e918f;'>AI ជំនួយការវិភាគមាសលំដាប់ពិភពលោក</p>", unsafe_allow_html=True)
st.write("---")

# ១. ផ្នែកបញ្ចូលរូបភាព (បង្រួមឱ្យតូចស្អាត)
with st.expander("➕ បញ្ចូលរូបភាពក្រាហ្វិកវិភាគ", expanded=False):
    uploaded_file = st.file_uploader("ជ្រើសរើសរូបភាព...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption='📊 កំពុងស្កេនក្រាហ្វិក...', use_container_width=True)
        st.success("🤖 Lucky: ខ្ញុំបានទទួលរូបភាពហើយ! សញ្ញាមាសបច្ចុប្បន្នគឺ Bullish។")

# ២. ប្រព័ន្ធសន្ទនាបែប Gemini (Chat Interface)
if "messages" not in st.session_state:
    st.session_state.messages = []

# បង្ហាញប្រវត្តិសន្ទនា
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ប្រអប់សន្ទនាដែលស្ថិតនៅខាងក្រោម (ដូច Gemini)
if prompt := st.chat_input("សួរអ្វីមួយមកកាន់ Lucky..."):
    # បង្ហាញសាររបស់អ្នកប្រើ
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # ចម្លើយរបស់ AI
    with st.chat_message("assistant"):
        response = f"✨ **Lucky Property:** ភក្ត្រាសម្លាញ់! ចំពោះ '{prompt}' ខ្ញុំយល់ថាវាជាឱកាសល្អក្នុងការត្រៀមទិញ។"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

st.write("---")
st.caption("© 2026 Pheaktra & Lucky Gemini - Powered by Google AI Style")

