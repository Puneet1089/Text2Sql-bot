import streamlit as st
import sqlite3
import pandas as pd  # ✅ import pandas
from sql_generator import generate_sql

with open("schema.txt", "r") as f:
    schema = f.read()

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

st.title("🧠 Text-to-SQL Bot using OpenAI")

question = st.text_input("Ask a question:")

if st.button("Generate and Run"):
    sql = generate_sql(question, schema)

    # 🔥 Clean unwanted markdown-style formatting
    sql = sql.replace("```sql", "").replace("```", "").strip()

    st.subheader("🧾 SQL Generated:")
    st.code(sql, language="sql")

    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]

        # ✅ Convert to pandas DataFrame
        df = pd.DataFrame(data, columns=cols)

        st.subheader("📊 Result:")
        st.dataframe(df)  # ✅ Use cleaned DataFrame
    except Exception as e:
        st.error(f"❌ Error: {e}")
