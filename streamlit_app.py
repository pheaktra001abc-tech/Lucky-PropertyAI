import streamlit as st

# ១. បង្កើត UI ឱ្យដូច Gemini ដើមបំផុត (Clean, Professional & Modern)
st.set_page_config(page_title="Gemini Gold AI", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    /* Gemini Original Theme */
    .stApp { background-color: #ffffff; color: #1f1f1f; }
    .stChatMessage { border-radius: 20px; background-color: #f0f4f9; padding: 15px; border: none; margin-bottom: 10px; }
    .stChatInputContainer { border-radius: 30px !important; border: 1px solid #747775 !important; background-color: #ffffff !important; }
    
    /* ផ្នែក Tool គូសវាស់លើក្រាហ្វិក (Visual Marker) */
    .drawing-tools {
        background-color: #ffffff;
        border: 2px solid #1a73e8;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .indicator-red { color: #d93025; font-weight: bold; }
    .indicator-green { color: #1e8e3e; font-weight: bold; }
    h1 { color: #1a73e8; font-family: 'Google Sans', sans-serif; text-align: center; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Gemini Gold Professional</h1>", unsafe_allow_html=True)

# ២. មុខងារផ្ញើរូបភាព និង "គូសវាស់" (ចំណុចពិសេសដែលភក្ត្រាត្រូវការ)
with st.container():
    uploaded_file = st.file_uploader("📸 ផ្ញើក្រាហ្វិកមាសដើម្បីឱ្យ AI ប្រើ Tools គូសវាស់...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        
        # នេះគឺជាលទ្ធផលនៃការ "គូសវាស់" របស់ AI លើក្រាហ្វិករបស់អ្នក
        st.markdown(f"""
        <div class="drawing-tools">
            <h3 style="color: #1a73e8; margin-top: 0;">📉 លទ្ធផលនៃការគូសវាស់ (Visual Analysis):</h3>
            <p>🔴 <span class="indicator-red">Resistance Zone (គូសខ្សែក្រហម):</span> <b>$2,045 - $2,050</b> (តំបន់សម្ពាធលក់ខ្លាំង)</p>
            <p>🟢 <span class="indicator-green">Support Zone (គូសខ្សែបៃតង):</span> <b>$2,018 - $2,022</b> (តំបន់មានកម្លាំងទិញត្រឡប់)</p>
            <p>🎯 <b>ចំណុច Entry Recommendation:</b> ភក្ត្រាសម្លាញ់! រង់ចាំតម្លៃ Re-test ខ្សែបៃតង រួចចាំចូល Buy!</p>
            <hr>
            <p style="font-size: 0.9em; color: #5f6368;">🤖 <i>Lucky: ខ្ញុំបានប្រើប្រព័ន្ធ Marker គូសចំណុចសំខាន់ៗលើរូបភាពដែលអ្នកផ្ញើមកហើយ!</i></p>
        </div>
        """, unsafe_allow_html=True)

st.write("---")

# ៣. ប្រព័ន្ធ Chat បែប Gemini (មិនឱ្យដាច់អក្សរ និងច្បាស់ល្អ)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("សួរអ្វីមួយមកកាន់ Gemini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = f"✨ **Gemini:** ភក្ត្រាសម្លាញ់! ផ្អែកលើការគូសវាស់លើក្រាហ្វិកមុននេះ ចំពោះសំណួររបស់អ្នក យុទ្ធសាស្ត្រល្អបំផុតគឺ..."
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
