import os  # Import the os library for manipulating file paths
import streamlit as st  # Import Streamlit to create the web application
from annotated_text import annotated_text  # Import the annotated_text function to highlight text
from utils import *  # Import useful functions defined in utils.py
from vectorial_representation import *  # Import functions for vector representation
import base64  # Import base64 to encode images
from langdetect import detect  # Import detect to detect the language of the text
from config import *  # Import pre-defined configurations
import datetime  # Import datetime for working with dates and times

# Function to add an HTML banner with title and image
def add_banner(png_file, title):
    with open(png_file, "rb") as f:
        bin_str = base64.b64encode(f.read()).decode("utf-8")  # Encode the image to base64
    banner_html = '''
    <div class="banner">
        <h1>%s</h1>
        <img src="data:image/png;base64,%s" alt="Banner Image">
    </div>
    <style>
    .banner {
        width: 100%%;
        height: 200px;  # Adjust this to change the height of the banner
        overflow: hidden;
        position: relative;
    }
    .banner h1 {
        position: absolute;
        top: 20%%;
        left: 0;  # Change this to adjust the horizontal position of the title
        transform: translateY(-50%%);
        color: white;  # Change this to change the text color
        font-size: 2em;  # Change this to change the text size
        white-space: nowrap;  # This prevents the title from wrapping into multiple lines
    }
    .banner img {
        width: 100%%;
        object-fit: cover;
    }
    </style>
    ''' % (title, bin_str)
    st.markdown(banner_html, unsafe_allow_html=True)


# Add banner
add_banner('images/Image-Banner_1.png', 'Phishing Detector')


# Function to load rules from a file
@st.cache_resource
def load_rules(path):
    rules = []
    with open(path, 'r', encoding="unicode_escape") as file:
        for line in file:
            rules.append(parse_rule(line))
    return rules

# Construct file paths using os.path.join
rules_path = os.path.join(rootPath, 'files')
rules_txt_path = os.path.join(rules_path, 'rules.txt')
rules_en_txt_path = os.path.join(rules_path, 'rules_en.txt')

# Load rules from files
rules = load_rules(rules_txt_path)
rules_en = load_rules(rules_en_txt_path)

# User interface
selected_entities = st.sidebar.multiselect(
    "Select which type of rules you want to evaluate",
    options=["Phishing", "Legit"],
    default=["Phishing"],
)

threshold = st.sidebar.slider('Phishing Probability Threshold', 0, 100, 70)

text_input = st.text_area("Enter text to analyze its content", height=200)

# Function to analyze the entered text
def analyze_text():
    with st.status("Analyzing text..."):
        st.markdown("**Analyzed Text**")
        st.info('Highlighted in the text are words or phrases that require presence by the rules being met.', icon="ℹ️")
        st.markdown("---")
        text = text_input
        variables = vectorial_representation(text)
        rules_eval = rules
        if detect(text) == 'en':
            # If the text is in English, English rules can be used (requires the existence of such rules)
            # rules_eval = rules_en
            st.toast('English language detected in the text. Only Spanish rules are being evaluated.', icon="ℹ️")
        else:
            st.toast('Spanish language detected in the text. Specific rules for that language will be evaluated.', icon="ℹ️")
        phishing_list, legit_list, id_major_prob = evaluar_reglas(rules_eval, variables)
        id_list = phishing_list
        if len(selected_entities) > 1:
            id_list = phishing_list + legit_list
        elif "Legit" in selected_entities:
            id_list = legit_list
        if len(phishing_list) == 0:
            st.sidebar.success('No phishing rules are met', icon="✅")
            print(text.replace("\n", " ") + "\nclass: Legit")
        elif len(phishing_list) > 0:
            if threshold <= float(rules[id_major_prob]['probabilidad']):
                st.sidebar.error('Number of phishing rules met: :red[' + str(len(phishing_list)) + "]\n" +
                                                                              "Probability that the email is Phishing: :red[" + 
                                                                              rules[id_major_prob]['probabilidad'] + "%], based on :red[" + 
                                                                              rules[id_major_prob]['muestras'] + "%] samples studied.", icon="🚨")
            else:
                st.sidebar.warning('Phishing rules met with lower probability for the analyzed text',
                            icon="⚠️")
            print(text.replace("\n", " ") + "\nclass: Phishing \nruleID: " + str(id_major_prob))
        tokens = Paint_Text(text, rules, id_list)
        annotated_text(*tokens)
        print("----------------------------------")

# File upload
uploaded_file = st.file_uploader("Upload a file to analyze its content", type=["doc", "docx", "pdf", "txt"])
if uploaded_file is not None:
    text_input = uploaded_file.getvalue()
    text_input = text_input.decode("utf-8")

# Button to analyze the text
if st.button("Analyze", type="primary"):
    analyze_text()

# Footer section
st.markdown("<br><hr><center>🕵 Powertoy tool developed by <a href='mailto:lazaro.bustio@ibero.mx?subject= about Phishing Detector !&body=Specify your intended usage.'><strong>Lázaro Bustio-Martínez, PhD.</strong></a> and <a href='mailto:vherrera@cenatav.co.cu?subject= about Phishing Detector !&body=Specify your intended usage.'><strong>Vitali Herrera-Semenets, PhD.</strong></a> .</center><hr>", unsafe_allow_html=True)
st.markdown(f"<center>© {datetime.datetime.now().year} Data Science departement and CENATAV</center>", unsafe_allow_html=True)
st.markdown(f"<center>© {datetime.datetime.now().year} All rights reserved</center>", unsafe_allow_html=True)