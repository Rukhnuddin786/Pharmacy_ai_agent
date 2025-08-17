import streamlit as st
import cohere

# Setup Cohere API
co = cohere.Client("Zdcyx9mxeFtVemihLfsk3vo6cfxBkpLJnhOl3FIm")

# Streamlit Page Configuration
st.set_page_config(page_title="Pharmacy AI Assistant", page_icon="💊", layout="centered")

# Load Bootstrap and responsive styles
st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #0e1117;
        }
        .main-container {
            max-width: 100%;
            width: 100%;
            padding: 5vw;
            background-color: #161b22;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }
        .btn-custom {
            background-color: #4B8BBE;
            color: white;
            border-radius: 30px;
            padding: 10px 25px;
            font-weight: bold;
            border: none;
        }
        .btn-custom:hover {
            background-color: #3776AB;
        }
        .title-text {
            font-size: 6vw;
            font-weight: bold;
            color: #58a6ff;
            text-align: center;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: gray;
            font-size: 3vw;
        }
        .result-box {
            background-color: #21262d;
            padding: 20px;
            border-left: 5px solid #4B8BBE;
            border-radius: 10px;
            margin-top: 20px;
        }
        input[type="text"] {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            border-radius: 10px !important;
            border: 1px solid #444 !important;
            padding: 10px !important;
            font-size: 4vw !important;
        }
        @media(min-width: 768px) {
            .title-text { font-size: 36px; }
            .footer { font-size: 16px; }
            input[type="text"] { font-size: 16px !important; }
        }
    </style>
""", unsafe_allow_html=True)

# 🧼 Start Main Container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 🔠 Title
st.markdown('<div class="title-text">Pharmacy AI Assistant 💊</div>', unsafe_allow_html=True)

# ✅ Cleaned Input Field
medicine_name = st.text_input(label="", placeholder="Enter the tablet name e.g. Paracetamol", label_visibility="collapsed")

# 🔘 Submit Button
if st.button("Get Tablet Info", key="btn"):
    if medicine_name.strip() == "":
        st.warning("Please enter a tablet name.")
    else:
        with st.spinner("Fetching AI-powered medical information..."):
            prompt = f"""
You are a helpful medical assistant. Explain in detail about the tablet: "{medicine_name}". Include:
1. What it is used for
2. Suitable age groups
3. Dosage instructions
4. Common side effects
5. Any warnings or precautions
6. Whether it needs a prescription

Keep it clear, medically sound, and understandable for students.
"""
            try:
                response = co.generate(
                    model='command-r-plus',
                    prompt=prompt,
                    max_tokens=500,
                    temperature=0.5
                )
                result = response.generations[0].text.strip()

                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.markdown(f"##### 📄 Info about **{medicine_name.capitalize()}**")
                st.write(result)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("Something went wrong. Please check the API key or your internet connection.")
                st.exception(e)

# Footer
st.markdown('<div class="footer">Made with ❤️ for all devices</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
