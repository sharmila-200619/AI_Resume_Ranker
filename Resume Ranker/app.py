import streamlit as st
import PyPDF2

# 🎯 One common list of target keywords (for all levels)
TARGET_KEYWORDS = [
    "python", "java", "c", "c++", "html", "css", "javascript", "sql", "tableau", "power bi",
    "excel", "ms office", "machine learning", "data analysis", "deep learning",
    "data visualization", "data science", "pandas", "numpy", "matplotlib", "seaborn",
    "git", "github", "communication", "teamwork", "problem solving", "project",
    "internship", "academic", "leadership", "mini project", "final year project"
]

# 🔍 Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text.lower()

# 🧠 Function to rank resume based on keyword match
def calculate_match_score(text):
    matched_keywords = [kw for kw in TARGET_KEYWORDS if kw in text]
    score = (len(matched_keywords) / len(TARGET_KEYWORDS)) * 100
    return round(score, 2)

# 🌐 Streamlit UI
st.title("📄 AI Resume Ranker")
st.markdown("Upload your resumes to check how well they match with industry-relevant skills!")

uploaded_files = st.file_uploader("📎 Upload one or more PDF resumes", type="pdf", accept_multiple_files=True)

if uploaded_files:
    results = []
    for uploaded_file in uploaded_files:
        text = extract_text_from_pdf(uploaded_file)
        score = calculate_match_score(text)
        results.append((uploaded_file.name, score))
    
    st.success("✅ Ranking Complete!")
    st.subheader("📊 Resume Results:")
    ranked = sorted(results, key=lambda x: x[1], reverse=True)
    for i, (filename, score) in enumerate(ranked, 1):
        st.write(f"*{i}. {filename}* — Match Score: {score}%")
else:
    st.info("Upload resumes in PDF format to begin.")