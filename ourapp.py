# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 19:56:37 2026

@author: rsehlabo
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Rebohele Sehlabo | Research Profile", layout="wide")

# ---------------- Sidebar ----------------
st.sidebar.title("Rebohele Sehlabo")
st.sidebar.info("""
MSc in Computer sciences, Researcher in Machine Learning & AI  
Breast Cancer Diagnosis Support Systems  
Rural Eastern Cape, South Africa
""")

st.sidebar.markdown("### Links")
st.sidebar.markdown("[GitHub](https://github.com/sehlabo1808)")
st.sidebar.markdown("[LinkedIn](www.linkedin.com/in/rebohele-sehlabo-587b51236)")

# ---------------- Header ----------------
st.title("Researcher Profile Page")
st.subheader("Machine Learning for Early Breast Cancer Detection")

st.image(
    "https://www.usz.ch/app/uploads/2025/02/usz-brustkrebs-illustration-medizinisch.png",
    caption="AI in Healthcare Research"
)

# ---------------- About ----------------
st.header("Research Overview")

name = "Rebohele Sehlabo"
field = "Machine Learning & Artificial Intelligence in Healthcare"
institution = "MSc in science in Computer Sciences"

st.write(f"**Name:** {name}")
st.write(f"**Field:** {field}")
st.write(f"**Institution:** {institution}")

st.write("""
This research focuses on developing an AI decision-support portal using Support Vector Machine (SVM)
to assist rural healthcare practitioners in early breast cancer diagnosis.
""")

# ---------------- Publications Upload ----------------
st.header("Publications / Research Outputs")
uploaded_file = st.file_uploader("Upload CSV of your publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    keyword = st.text_input("Filter by keyword")
    if keyword:
        filtered = publications[
            publications.apply(
                lambda row: keyword.lower() in row.astype(str).str.lower().values,
                axis=1,
            )
        ]
        st.write(f"Filtered results for '{keyword}'")
        st.dataframe(filtered)

# ---------------- Methodology Section ----------------
st.header("SVM Methodology Phases")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Training Phase")
    st.write("""
    - Data preprocessing  
    - Feature extraction  
    - SVM kernel training
    """)

with col2:
    st.subheader("Testing Phase")
    st.write("""
    - Model validation  
    - Image classification tests
    """)

with col3:
    st.subheader("Evaluation")
    st.write("""
    - Accuracy  
    - Precision / Recall  
    - Confusion Matrix
    """)

# ---------------- STEM / Sample Data Viewer ----------------
st.header("Sample Medical Data Viewer")

data = pd.DataFrame({
    "Patient ID": [101, 102, 103, 104, 105],
    "Tumor Size (mm)": [12, 25, 18, 30, 22],
    "Texture Score": [0.45, 0.78, 0.56, 0.81, 0.63],
    "Diagnosis": ["Benign", "Malignant", "Benign", "Malignant", "Benign"],
})

st.dataframe(data)

size_filter = st.slider("Filter by Tumor Size", 0, 50, (0, 50))
filtered_data = data[data["Tumor Size (mm)"].between(size_filter[0], size_filter[1])]
st.write("Filtered Patient Data")
st.dataframe(filtered_data)

# ---------------- Contact ----------------
st.header("Contact")
st.write("Email: rsehlabo@wsu.ac.za")
st.write("0716359467")


st.markdown("---")
st.write("© 2026 Rebohele Sehlabo | MSc in Sceince in Computer Science")

