import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Custom CSS with updated footer styles
st.markdown("""
    <style>
    /* Full-screen gradient background */
    body {
        background: linear-gradient(45deg, #F58529, #FEDA77, #DD2A7B, #8134AF, #515BD4);
        color: white;
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
    }

    /* Remove card and use full-screen layout */
    .stApp {
        background-color: transparent; /* Remove the card */
        padding: 0;
        max-width: 100%;
        margin: 0;
        box-shadow: none; /* Remove shadow */
        color: #FFFFFF; /* White text for visibility on the colorful background */
    }

    /* Main title with a professional color */
    .main-title {
        color: #003366; /* Dark blue for a professional look */
        font-size: 3.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Subtle shadow for depth */
    }

    /* Subtitle with light, contrasting effect */
    .sub-title {
        color: #FFE3E3;
        font-size: 1.2em;
        margin-bottom: 40px;
        text-align: center;
        font-style: italic;
    }

    /* Input fields with Instagram color border */
    .stTextInput input, .stTextArea textarea {
        font-size: 16px;
        padding: 14px;
        border-radius: 10px;
        border: 2px solid #FEDA77;
        background-color: #FFFFFF;
        color: #000000; /* Dark text in the input areas */
        transition: border-color 0.3s ease;
    }
    .stTextInput input:hover, .stTextArea textarea:hover {
        border-color: #DD2A7B;
    }

    /* Buttons with Instagram gradient background */
    .stButton button {
        background: linear-gradient(45deg, #F58529, #DD2A7B);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 12px 30px;
        border-radius: 30px;
        border: none;
        transition: background-color 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }

    .stButton button:hover {
        background-color: #FEDA77;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
    }

    /* Checkbox and supported languages container */
    .supported-languages {
        font-size: 16px;
        background-color: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 10px;
        color: #000000; /* Dark text for readability */
        margin: 20px 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }

    /* Footer with updated styles for better visibility */
    .footer {
        text-align: center;
        padding-top: 20px;
        font-size: 14px;
        color: #FFFFFF;
        margin-top: 30px;
        background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
        padding: 10px 0; /* Add padding for better spacing */
    }

    .footer a {
        text-decoration: none;
        color: #FEDA77;
        font-weight: bold;
    }

    </style>
    """, unsafe_allow_html=True)

# Streamlit UI with professional background
st.markdown('<h1 class="main-title">🌟 Language Translator</h1>', unsafe_allow_html=True)


# Input text
source_text = st.text_area("📝 Enter the text you want to translate:", "", height=150)

# Input source language
source_lang = st.selectbox(
    "Select source language",
    ["en", "fr", "es", "de", "it", "pt", "nl", "ru", "zh-cn", "ja", "ko", "ar", "hi", "tr"]
)

# Target language input
target_language_search = st.text_input("🔍 Target language name (e.g., French, Spanish, German):")

# Translate button
if st.button("🌍 Translate"):
    target_lang_code = get_language_code(target_language_search)

    if target_lang_code is None:
        st.error(f"⚠️ '{target_language_search}' is not a valid language. Please try again.")
    else:
        try:
            translated_text = translator.translate(source_text, src=source_lang, dest=target_lang_code).text
            st.success(f"**Translated Text:** {translated_text}")
        except Exception as e:
            st.error(f"Translation failed: {str(e)}")

# Show supported languages
if st.checkbox("Show supported languages"):
    st.markdown('<div class="supported-languages">Supported Languages:</div>', unsafe_allow_html=True)
    st.write(", ".join([lang_name.capitalize() for lang_name in LANGUAGES.values()]))

# Footer
st.markdown("""<div class="footer">
    Created by <a href="https://github.com/sonajoy" target="_blank">SONA PJ</a> | Powered by Streamlit & Google Translate API
</div>""", unsafe_allow_html=True)
