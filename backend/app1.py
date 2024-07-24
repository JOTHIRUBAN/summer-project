from API import groq_api_key
from db_connection import get_db_connection
from groq import Groq

client = Groq(
    api_key= groq_api_key,
)

def fetch_id(usergmail):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"Select id from users where email='{usergmail}'")
    rows = cur.fetchone()
    cur.close()
    conn.close()
    return rows[0]

def fetch_keywords(userid):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT keyword FROM feed WHERE user_id = '{userid}'AND feed_date >= date_trunc('week', current_date) AND feed_date < date_trunc('week', current_date) + interval '1 week';")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def gensum(keyword):
    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": f"Give the summary of 150 words using {keyword} ",
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


def genquiz(keyword):
    quiz_generation = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": f"Give the 5MCQ questions for each topic in {keyword} ",
            }
        ],
        model="llama3-8b-8192",
    )
    return quiz_generation.choices[0].message.content


usergmail = "abc@gmail.com"    #session["gmail"] 
userid = fetch_id(usergmail)
keyword= fetch_keywords(userid)
summary = gensum(keyword)
quiz = genquiz(keyword)
print(summary)
print(quiz)