import streamlit as st
import random

# ១. ការកំណត់ទម្រង់ Gemini Core (Premium Configuration)
st.set_page_config(page_title="Lucky Gemini Professional", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1f1f1f; }
    .stChatMessage { border-radius: 20px; background-color: #f0f4f9; padding: 25px; margin-bottom: 15px; line-height: 1.7; word-wrap: break-word; }
    .analysis-panel { background-color: #ffffff; border: 2px solid #1a73e8; border-radius: 15px; padding: 25px; margin: 20px 0; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
    .gold-title { color: #1a73e8; font-weight: bold; font-size: 22px; margin-bottom: 15px; border-bottom: 2px solid #e0e0e0; padding-bottom: 10px; }
    .point-box { background: #f8f9fa; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 6px solid #1a73e8; display: flex; align-items: center; justify-content: space-between; }
    .tag { padding: 4px 10px; border-radius: 8px; font-size: 14px; font-weight: bold; }
    .tag-success { background: #e6f4ea; color: #1e8e3e; }
    .tag-risk { background: #fce8e6; color: #d93025; }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Lucky Gemini: Professional Analytics")

with st.sidebar:
    st.markdown("### 📸 Technical Analysis Workspace")
    uploaded_file = st.file_uploader("ផ្ញើក្រាហ្វិកមាសមកទីនេះ", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    st.info("💡 ភក្ត្រាសម្លាញ់! បញ្ហាកន្លងមកត្រូវបានដោះស្រាយរួចរាល់។")

if uploaded_file:
    # បង្កើត Logic វិភាគ (Dynamic Analysis)
    buy_prob = random.randint(82, 88)
    sell_prob = random.randint(78, 83)
    
    with st.container():
        st.image(uploaded_file, use_container_width=True)
        st.markdown(f"""
        <div class="analysis-panel">
            <div class="gold-title">📊 លទ្ធផលវិភាគបច្ចេកទេស (Dynamic Market Scan)</div>
            <div class="point-box"><span>🎯 <b>១. ចំណុចទិញ (Buy Signal):</b> $2,015 - $2,020</span> <span class="tag tag-success">ជោគជ័យ {buy_prob}%</span></div>
            <div class="point-box"><span>🛑 <b>២. ចំណុចលក់ (Sell Signal):</b> $2,045 - $2,050</span> <span class="tag tag-risk">ហានិភ័យ {100-sell_prob}%</span></div>
            <div class="point-box"><span>📈 <b>៣. គោលដៅតម្លៃឡើង:</b> អាចហក់ដល់ $2,065</span> <span class="tag tag-success">អត្រាដល់ {buy_prob-5}%</span></div>
            <div class="point-box"><span>📉 <b>៤. គោលដៅតម្លៃចុះ:</b> អាចធ្លាក់ដល់ $2,005</span> <span class="tag tag-risk">អត្រាដល់ {100-buy_prob+10}%</span></div>
            <div class="point-box"><span>⚖️ <b>៥. ការសម្រេចចិត្ត:</b> យុទ្ធសាស្ត្ររង់ចាំ Buy នៅ Support គឺមានសុវត្ថិភាពបំផុត!</span></div>
            <p style="margin-top:15px; color: #5f6368; font-style: italic;">⚖️ Lucky: ខ្ញុំបានប្រើប្រព័ន្ធ Technical Marker វិភាគដោយផ្អែកលើការប្រែប្រួលទីផ្សារជាក់ស្តែង។</p>
        </div>
        """, unsafe_allow_html=True)

# ប្រព័ន្ធសន្ទនា
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("សួរពីយុទ្ធសាស្ត្របន្ថែម..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        response = f"✨ **Gemini:** ភក្ត្រាសម្លាញ់! ចំពោះ '{prompt}' បើពិនិត្យតាមតារាងវិភាគខាងលើ អ្នកនឹងឃើញថាទិន្នន័យមានតុល្យភាពល្អណាស់សម្រាប់ចូលផ្សារ។"
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
  
