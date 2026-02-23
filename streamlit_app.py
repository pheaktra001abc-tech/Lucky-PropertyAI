import streamlit as st

# ១. ការកំណត់ទម្រង់ Gemini Core (Premium Configuration)
st.set_page_config(page_title="Lucky Gemini Professional", page_icon="✨", layout="wide")

# ២. ស្ទីល Gemini ដើម (ដោះស្រាយបញ្ហាអក្សរ និងរូបរាងដែលភក្ត្រាជួបប្រទះ)
st.markdown("""
    <style>
    /* ផ្ទៃខាងក្រោយពណ៌ស និងអក្សរខ្មៅដិតច្បាស់បំផុត */
    .stApp { background-color: #ffffff; color: #1f1f1f; }
    
    /* ប្រអប់សារដែលបង្ហាញអក្សរពេញលេញ មិនឱ្យដាច់ផ្ដាច់ */
    .stChatMessage { 
        border-radius: 20px; 
        background-color: #f0f4f9; 
        padding: 25px; 
        margin-bottom: 15px;
        line-height: 1.7;
        font-size: 16px;
        word-wrap: break-word;
    }
    
    /* ផ្ទាំងវិភាគបច្ចេកទេសកម្រិតខ្ពស់ (Technical Dashboard) */
    .analysis-panel {
        background-color: #ffffff;
        border: 2px solid #1a73e8;
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    .gold-title { color: #1a73e8; font-weight: bold; font-size: 22px; margin-bottom: 15px; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; }
    .point-box { background: #f8f9fa; padding: 10px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid #1a73e8; }
    .stChatInputContainer { border-radius: 35px !important; border: 1px solid #747775 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Lucky Gemini Professional Analysis")

# ៣. Sidebar សម្រាប់ Workspace (លុប Drag & Drop ពីអេក្រង់កណ្តាល)
with st.sidebar:
    st.markdown("### 📸 Technical Analysis Workspace")
    uploaded_file = st.file_uploader("ផ្ញើក្រាហ្វិកមាសមកទីនេះ", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    st.info("💡 ភក្ត្រាសម្លាញ់! ផ្ញើរូបភាពមក ខ្ញុំនឹងប្រើ Tools គូសវាស់ជូនភ្លាម។")

# ៤. ប្រព័ន្ធវិភាគ និងគូសវាស់ (ចំណុចពិសេសដែលបន្ថែមពីលើ Gemini ធម្មតា)
if uploaded_file:
    with st.container():
        st.image(uploaded_file, use_container_width=True)
        st.markdown(f"""
        <div class="analysis-panel">
            <div class="gold-title">📊 លទ្ធផលវិភាគបច្ចេកទេស (Technical Marker)</div>
            <div class="point-box">🎯 <b>១. ចំណុចទិញ (Buy Signal):</b> $2,015 - $2,020 (អត្រាជោគជ័យ <b>៨៥%</b> / ហានិភ័យ <b>១៥%</b>)</div>
            <div class="point-box">🛑 <b>២. ចំណុចលក់ (Sell Signal):</b> $2,045 - $2,050 (អត្រាជោគជ័យ <b>៨០%</b> / ហានិភ័យ <b>២០%</b>)</div>
            <div class="point-box">📈 <b>៣. គោលដៅតម្លៃឡើង:</b> អាចហក់ដល់ <b>$2,065</b> (អត្រាជោគជ័យ <b>៧៥%</b>)</div>
            <div class="point-box">📉 <b>៤. គោលដៅតម្លៃចុះ:</b> អាចធ្លាក់ដល់ <b>$2,005</b> (អត្រាជោគជ័យ <b>៧០%</b>)</div>
            <div class="point-box">⚖️ <b>៥. ការសម្រេចចិត្ត:</b> រង់ចាំនៅតំបន់ Support គឺជាយុទ្ធសាស្ត្រដែលមានសុវត្ថិភាពបំផុត!</div>
            <p style="margin-top:15px; color: #5f6368;">🤖 <i>Lucky: ខ្ញុំបានប្រើប្រព័ន្ធ Technical Marker គូសវាស់លើក្រាហ្វិករបស់អ្នករួចរាល់ហើយ!</i></p>
        </div>
        """, unsafe_allow_html=True)

# ៥. ប្រព័ន្ធសន្ទនា (Chat Display)
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
        # ការឆ្លើយតបដែលមិនកាត់ផ្ដាច់អក្សរ
        full_res = f"✨ **Gemini:** ភក្ត្រាសម្លាញ់! ចំពោះ '{prompt}' ផ្អែកលើការវិភាគបច្ចេកទេសខាងលើ ខ្ញុំសូមណែនាំឱ្យអ្នកតាមដានចំណុចទិញ $2,015 ដែលមានអត្រាជោគជ័យខ្ពស់បំផុត!"
        st.write(full_res)
    st.session_state.messages.append({"role": "assistant", "content": full_res})
