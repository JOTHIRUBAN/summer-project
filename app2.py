from flask import Flask,render_template,request
from flask_cors import CORS
from API import groq_api_key
from db_connection import get_db_connection
from groq import Groq


client = Groq(
    api_key= groq_api_key,
)

app = Flask(__name__)
CORS(app)

def fetch_id(usergmail):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"Select id from users where email='{usergmail}'")
    rows = cur.fetchone()
    cur.close()
    conn.close()
    return rows[0]

def fetch_keywords():
    usergmail = "abc@gmail.com"    #session["gmail"] 
    userid = fetch_id(usergmail)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT keyword FROM feed WHERE user_id = '{userid}'AND feed_date >= date_trunc('week', current_date) AND feed_date < date_trunc('week', current_date) + interval '1 week';")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.route('/summary',methods=['GET','POST'])
def gensum():
    keyword= fetch_keywords()
    chat_completion = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": f"Give the summary of 150 words using {keyword} ",
            }
        ],
        model="llama3-8b-8192",
    )
    summary_content= chat_completion.choices[0].message.content
    return render_template('summary.html', summary=summary_content).replace('*',"&nbsp;&nbsp;")


@app.route('/quiz',methods=['GET','POST'])
def genquiz():
    
    keyword= fetch_keywords()
    quiz_generation = client.chat.completions.create(
            messages=[
                    {
                    "role": "user",
                    "content": f"Give the 5MCQ questions for each topic in {keyword}.",
                    }
                ],
                model="llama3-8b-8192",  
                stream=False
            )
    quiz_content = (quiz_generation.choices[0].message.content).replace('*',"<br>")
    quiz_content = quiz_content.replace("?","? <br>")
    quiz_content = quiz_content.replace(";"," <br>")

    return render_template('quiz.html', quiz=quiz_content)

@app.route('/feed.html',methods=['GET','POST'])
def feed():
    return render_template('feed.html')

if(__name__ == "__main__"):
    app.run(debug=True)