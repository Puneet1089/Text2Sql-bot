from openai import OpenAI
import api_key  

client = OpenAI(
    api_key=api_key.API_KEY,
    base_url="https://api.a4f.co/v1"
)

def generate_sql(user_question, schema):
    prompt = f"""
Convert this question to an SQL query:
Schema:
{schema}

Question:
{user_question}

SQL:
"""
    response = client.chat.completions.create(
        model="provider-5/gpt-4.1-nano",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()





