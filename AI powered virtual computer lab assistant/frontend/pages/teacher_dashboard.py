# frontend/pages/teacher_dashboard.py
import streamlit as st
from backend.progress import fetch_all_progress
import pandas as pd

def app():  # ✅ Make sure function name is exactly 'app'
    st.title("🧑‍🏫 Teacher Dashboard")
    st.subheader("📊 Student Progress Overview")

    all_progress = fetch_all_progress()  # all students
    if all_progress:
        df = pd.DataFrame(all_progress)

        # Summary per student
        summary = df.groupby("username").agg(
            Topics_Attempted=pd.NamedAgg(column="topic", aggfunc="count"),
            Topics_Completed=pd.NamedAgg(column="status", aggfunc=lambda x: sum(x=="Completed"))
        ).reset_index()
        st.markdown("### 📌 Summary per Student")
        st.table(summary)

        # Detailed progress
        st.markdown("### 📋 Detailed Progress")
        st.dataframe(df)

    else:
        st.info("No student progress available yet.")
