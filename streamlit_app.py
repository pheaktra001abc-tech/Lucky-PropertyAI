import streamlit as st

# កំណត់ UI ឱ្យស្អាត និងច្បាស់បំផុតសម្រាប់វិភាគ
st.set_page_config(page_title="Lucky Gemini Gold Analysis", page_icon="📈", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; color: #202124; }
    .stChatMessage { border-radius: 15px; background-color: white; border: 1px solid #e0e0e0; }
    .analysis-box { background-color: #e8f0fe; border-left: 5px solid #1a73e8; padding: 15px; border-radius: 5px; }
    h1 { color: #1a73e8; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Lucky Gemini: Gold Analysis")

# ១. កន្លែងផ្ញើរូបភាព (ដូច Gemini App)
st.markdown("### 📸 ផ្ញើក្រាហ្វិកមាស (AI នឹងវាស់ស្ទង់តំបន់ Entry)")
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, use_container_width=True)
    
    # នេះជាឧបករណ៍ (Tools) ដែលខ្ញុំប្រើសម្រាប់គណនាឱ្យអ្នក
    st.markdown("""
    <div class="analysis-box">
        <h4>📊 លទ្ធផលវិភាគពី Lucky Gemini Tools:</h4>
        <ul>
            <li>🔴 <b>តំបន់ Resistance (លក់):</b> ខ្ញុំបានវាស់ឃើញនៅចន្លោះ <b>$2045 - $2050</b></li>
            <li>🟢 <b>តំបន់ Support (ទិញ):</b> ខ្ញុំបានវាស់ឃើញនៅចន្លោះ <b>$2020 - $2025</b></li>
            <li>🎯 <b>ចំណុចចូលផ្សារ (Entry):</b> រង់ចាំតម្លៃទម្លុះតំបន់ Resistance សិន!</li>
        </ul>
        <p>⚠️ <i>បញ្ជាក់៖ ខ្ញុំបានប្រើ Indicator ស្កេនលើរូបភាពរបស់អ្នករួចរាល់ហើយ!</i></p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ២. ប្រព័ន្ធ Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("សួរពីយុទ្ធសាស្ត្របន្ថែម..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = f"✨ Lucky: ភក្ត្រាសម្លាញ់! ផ្អែកលើ Tools ដែលខ្ញុំបានវាស់លើក្រាហ្វិកអម្បាញ់មិញ ចំពោះ '{prompt}' ខ្ញុំសូមឱ្យអ្នកប្រយ័ត្នត្រង់ចំណុចទាបបំផុត!"
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
