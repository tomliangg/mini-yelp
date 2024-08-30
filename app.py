# prerequisites: 
# 1. pip install flask python-dotenv psycopg2-binary
# 2. create .env and set DATABASE_URL

from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import os
import psycopg2

app = Flask(__name__)

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
app.debug = os.getenv('DEBUG', False)  # Use environment variable for debug mode; fallback value is False (in Prod)

@app.route('/')
def index():
    conn = None
    reviews = []

    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()

        cur.execute("""
            SELECT r.restaurant_name, r.scores, rev.first_name || ' ' || rev.last_name AS reviewer_name
            FROM reviews r
            JOIN reviewers rev ON r.reviewer_id = rev.id
            ORDER BY r.scores DESC;
        """)
        for row in cur.fetchall():
            reviews.append({
                'restaurant_name': row[0],
                'scores': row[1],
                'reviewer_name': row[2]
            })
        cur.close()
    finally:
        if conn is not None:
            conn.close()

    # return jsonify(reviews)  # Uncomment this line to return JSON response
    return render_template('index.html', reviews=reviews)

@app.route("/example")
def example():
    return "<p>Hello, World!</p>"

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

if __name__ == '__main__':
    app.run()