from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
import PyPDF2 as pdf
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from db_connection import get_db_connection
from API import gemini_api_key

app = Flask(__name__)
CORS(app)

# Configure the Gemini API
genai.configure(api_key=gemini_api_key)

# Prompt template for ATS evaluation
input_prompt_template = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive, and you should provide 
the best assistance for improving the resumes. Assign the percentage matching based 
on the job description and
the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# Prompt template for YouTube video summarization
youtube_prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        raise e

@app.route('/upload', methods=['POST'])
def upload():
    jd = request.form['jd']
    file = request.files['file']
    resume_text = input_pdf_text(file)
    input_prompt = input_prompt_template.format(text=resume_text, jd=jd)
    response = get_gemini_response(input_prompt)
    return jsonify(response)

@app.route('/summary', methods=['POST'])
def summary():
    data = request.get_json()
    print(f"data - {data}")
    youtube_link = data.get('youtubeLink')
    transcript_text = extract_transcript_details(youtube_link)
    if transcript_text:
        summary = get_gemini_response(youtube_prompt + transcript_text)
        print(summary)
        return jsonify({'summary': summary})
    return jsonify({'error': 'Failed to get transcript'}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and user[2] == password:
        return jsonify({"status": "success", "message": "Login successful"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid email or password"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        conn.close()
        return jsonify({"status": "failure", "message": "Email already exists"}), 400

    cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    conn.close()

    return jsonify({"status": "success", "message": "Account created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
