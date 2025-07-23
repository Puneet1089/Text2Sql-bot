# 🧠 Text2SQL Bot

A powerful AI-powered tool that converts natural language queries into SQL and executes them on a local database using Streamlit UI.

## 🚀 Features

- Convert plain English questions to SQL using OpenAI GPT (via A4F API).
- Run SQL on a local SQLite database and view results instantly.
- Simple and clean Streamlit-based UI.
- Useful for learning, internal data exploration, or proof-of-concept apps.

## ⚙️ How It Works

1. User enters a question like:  
   `"Show me all users who joined in June"`
2. `sql_generator.py` sends the prompt to OpenAI model via A4F Gateway.
3. GPT returns a SQL query like:  
   `"SELECT * FROM users WHERE join_date LIKE '2023-06%'"`
4. This query is executed on `db.sqlite`, and result is shown using Streamlit.

## 🛠️ Tech Stack

- Python
- OpenAI API (via A4F Gateway)
- Streamlit
- SQLite

## 📦 Setup Instructions

1. Clone the repository:
git clone https://github.com/Puneet1089/Text2Sql-bot.git

2. Install dependencies:

3. pip install -r requirements.txt

4. Run the app:

5. streamlit run app.py

Make sure your `api_key.py` file contains your API key:
```python
API_KEY = "your-api-key"


📁 Folder Structure

Text2Sql-bot/
├── app.py                 # Streamlit UI
├── sql_generator.py       # GPT-based SQL generator
├── setup_db.py            # Initializes sample database
├── db.sqlite              # Sample SQLite database
├── requirements.txt
├── README.md
└── api_key.py             # Your A4F API key