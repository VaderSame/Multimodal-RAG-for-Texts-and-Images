# streamlit_app.py
# A Streamlit app to dynamically display images and their AI-generated summaries side by side

import streamlit as st
import json
import os
from PIL import Image

# Page configuration
st.set_page_config(page_title="Image-Explanation Demo", layout="wide")
st.title("Dynamic Image Summaries from Extracted Figures/Tables")

# Paths to data and images
DATA_FILE = "img_data.json"
IMAGES_DIR = "extracted_images"

# Ensure the JSON data file exists
if not os.path.exists(DATA_FILE):
    st.error(f"Data file '{DATA_FILE}' not found. Please run your pipeline to generate it.")
    st.stop()

# Load the image-summary data
with open(DATA_FILE, "r") as f:
    img_data = json.load(f)

# Iterate and display each image with its explanation
for item in img_data:
    name = item.get("name")  # Now includes .jpg extension
    explanation = item.get("explanation", "")
    page = item.get("page", "N/A")

    # Direct path construction since JSON now has correct filename
    img_path = os.path.join(IMAGES_DIR, name)
    
    if not os.path.exists(img_path):
        st.warning(f"Image file '{name}' not found in '{IMAGES_DIR}'.")
        continue

    # Display header with page info
    st.subheader(f"Figure: {name} (Page {page})")
    
    # Display in two columns: image and text
    col1, col2 = st.columns([1, 2])
    
    with col1:
        img = Image.open(img_path)
        st.image(img, caption=name, width=350)
    
    with col2:
        # Use st.write for better text formatting
        st.write(explanation)
    
    st.markdown("---")

# To run this app:
# 1. Make sure img_data.json has the corrected filenames (with .jpg)
# 2. In terminal: streamlit run streamlit_app.py