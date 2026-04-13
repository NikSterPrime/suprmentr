import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader
from utils import preprocess

st.set_page_config(page_title="Resume Analyser", layout="centered")
st.title("AI Resume Analyser")

#upload resume
resume_file=st.file_uploader("Upload your resume (TXT or PDF)", type=["txt", "pdf"])

job_desc=st.text_area("Enter the job description")

if resume_file and job_desc:
    try:
        if resume_file.name.lower().endswith(".pdf"):
            reader = PdfReader(resume_file)
            pages_text = [page.extract_text() or "" for page in reader.pages]
            resume_text = "\n".join(pages_text)
        else:
            resume_text = resume_file.read().decode("utf-8")
    except Exception:
        st.error("Unable to read the uploaded resume. Please upload a valid TXT or PDF file.")
        st.stop()

    resume_clean=preprocess(resume_text)

    job_clean=preprocess(job_desc)

    #TF-IDF Vectorization
    vectorizer=TfidfVectorizer()
    vectors=vectorizer.fit_transform([resume_clean, job_clean])

    #Cosine Similarity
    similarity=cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    #score
    score=round(similarity*100, 2)

    st.subheader(f"Resume Match Score:{score}%")
    if(score>70):
        st.success("Great match! Your resume aligns well with the job description.")
    elif(score>40):
        st.warning("Decent match. Consider tailoring your resume more to the job description.")
    else:
        st.error("Poor match. Consider revising your resume to better fit the job description.")

    st.subheader("Top Keywords in Resume:")
    feature_names=vectorizer.get_feature_names_out()
    st.write(", ".join(feature_names[:20]))