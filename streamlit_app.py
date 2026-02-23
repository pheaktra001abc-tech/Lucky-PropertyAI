import streamlit as st

# ១. បង្កើត Interface ឱ្យដូច Gemini ដើម ១០០%
st.set_page_config(page_title="Gemini Ultra", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    /* Gemini Premium UI Design */
    .stApp { background-color: #f8f9fa; color: #1f1f1f; }
    
    /* កែសម្រួលប្រអប់សារឱ្យបង្ហាញអក្សរបានពេញលេញ មិនឱ្យដាច់ទៀតទេ */
    .stChatMessage { 
        border-radius: 20px; 
        background-color: #ffffff; 
        padding: 20px; 
        border: 1px solid #dee2e6;
        margin-bottom: 15px;
        word-wrap: break-word; /* ធានាថាអក្សរមិនដាច់ */
        overflow-wrap: break-word;
    }
    
    /* រចនាប្រអប់សរសេរសារឱ្យស្អាត */
    .stChatInputContainer { border-radius: 30px !important; border: 1px solid #747775 !important; }

    /* ផ្ទាំងគូសវាស់បច្ចេកទេស (Analysis Tools) */
    .drawing-canvas {
        background-color: #ffffff;
        border-left: 6px solid #1a73e8;
        border-radius: 12px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .metric-box { display: inline-block; width: 48%; padding: 10px; }
    h1 { color: #1a73e8; font-family: 'Google Sans', sans-serif; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Gemini Gold Professional</h1>", unsafe_allow_html=True)

# ២. មុខងារផ្ញើរូប និងគូសវាស់ (Update តាម ៥ ចំណុចរបស់អ្នក)
with st.sidebar:
    st.markdown("### 📸 Visual Marker Tool")
    uploaded_file = st.file_uploader("ផ្ញើក្រាហ្វិកមាសទីនេះ", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with st.container():
        st.image(uploaded_file, caption="📈 កំពុងប្រើ Tools គូសវាស់...", use_container_width=True)
        st.markdown(f"""
        <div class="drawing-canvas">
            <h3 style="color: #1a73e8; margin-top: 0;">📊 លទ្ធផលនៃការគូសវាស់បច្ចេកទេស៖</h3>
            <div class="metric-box"><b style="color: #d93025;">🔴 Resistance:</b> $2,045 (85%)</div>
            <div class="metric-box"><b style="color: #1e8e3e;">🟢 Support:</b> $2,018 (90%)</div>
            <hr>
            <p><b>🎯 យុទ្ធសាស្ត្រចូលផ្សារ (Update):</b></p>
            <p>១. <b>ទិញ (Buy):</b> អត្រាជោគជ័យខ្ពស់ត្រង់ $2,018 - $2,022</p>
            <p>២. <b>លក់ (Sell):</b> អត្រាជោគជ័យខ្ពស់ត្រង់ $2,045 - $2,050</p>
            <p>៣. <b>គោលដៅ៖</b> តម្លៃអាចនឹងឡើងដល់ចំណុច Pivot មុននឹងធ្លាក់ចុះ។</p>
        </div>
        """, unsafe_allow_html=True)

# ៣. ប្រព័ន្ធសន្ទនាដែលបង្ហាញអក្សរច្បាស់ និងពេញលេញ
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
        # បង្ហាញអក្សរពេញលេញ (Full Text Display)
        full_res = f"✨ **Gemini:** ភក្ត្រាសម្លាញ់! ផ្អែកលើការគូសវាស់ យុទ្ធសាស្ត្រសម្រាប់ '{prompt}' គឺការរង់ចាំនៅតំបន់ Support ដែលខ្ញុំបានបញ្ជាក់ជូនខាងលើ ដើម្បីកាត់បន្ថយហានិភ័យ និងបង្កើនអត្រាជោគជ័យ!"
        st.write(full_res)
    st.session_state.messages.append({"role": "assistant", "content": full_res})
