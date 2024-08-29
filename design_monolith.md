## Design Document: Simple Restaurant Review Web Application (Monolithic Approach)

**Requirements:**

- App users can see a list of reviews sorted by scores in DESC order. Each item of the list should include these info: name of restaurant, score, reviewer name (first name + last name).

**Requirements Analysis:**

- The Flask web server will render an HTML template with the review data fetched from the Supabase database.
- The backend connects to the Supabase database, executes a SQL query to join the `reviews` and `reviewers` tables, retrieves the necessary data, and passes it to the template for rendering.

**1. Introduction**

This document outlines the design of a simple monolithic web application similar to Yelp, focusing on displaying restaurant reviews. The application will use Python Flask as the web framework, Jinja as the template engine, and Supabase as the database.

**2. System Architecture**

The application will follow a monolithic architecture:

- **Web Server (Flask):**
  - Flask will handle HTTP requests and render HTML templates.
  - Flask will interact with the Supabase database to retrieve and process data.
- **Template Engine (Jinja):**
  - Jinja will be used to create dynamic HTML templates.
  - Templates will be rendered with data fetched from the database.
- **Database (Supabase):**
  - Supabase will store the restaurant reviews and reviewer information in two tables: `reviews` and `reviewers`.

**3. Data Model**

The database schema is as follows:

**Table: `reviews`**

| Column Name     | Data Type                | Description                           |
| --------------- | ------------------------ | ------------------------------------- |
| id              | bigint (primary key)     | Unique identifier for each review     |
| created_at      | timestamp with time zone | Timestamp of review creation          |
| restaurant_name | text                     | Name of the restaurant                |
| city            | text                     | City where the restaurant is located  |
| state           | text                     | State where the restaurant is located |
| scores          | smallint                 | Review score (0-10)                   |
| reviewer_id     | bigint (foreign key)     | ID of the reviewer                    |
| comment         | text                     | User's review comment                 |

**Table: `reviewers`**

| Column Name | Data Type            | Description                         |
| ----------- | -------------------- | ----------------------------------- |
| id          | bigint (primary key) | Unique identifier for each reviewer |
| first_name  | character varying    | Reviewer's first name               |
| last_name   | character varying    | Reviewer's last name                |
| email       | text                 | Reviewer's email address            |

**4. Routes**

The Flask application will define the following route:

- **`GET /`:**
  - Renders the `index.html` template with a list of reviews sorted by `scores` in descending order.
  - Each review object will include:
    - `restaurant_name`
    - `scores`
    - `reviewer_name` (concatenated first and last name from the `reviewers` table)

**5. Template Structure**

- The `index.html` template will contain an HTML structure for displaying the list of reviews.
- The template will use Jinja syntax to iterate over the list of reviews and generate HTML elements dynamically.

**6. Implementation Details**

- **Flask Application:**
  - A Flask route will be defined for the root URL (`/`).
  - The route handler will query the Supabase database using the `psycopg2` library (or a Supabase client library).
  - The query will join the `reviews` and `reviewers` tables, select the required columns, and order by `scores` in descending order.
  - The result will be passed to the `index.html` template for rendering.
- **Jinja Template (`index.html`):**
  - The template will include an HTML structure with placeholders for the review list.
  - Jinja syntax will be used to iterate over the list of reviews and generate HTML elements dynamically.

**7. Deployment**

The application can be deployed to a platform that supports Python Flask applications, such as Heroku, PythonAnywhere, or AWS.

## Code Implementation

**Flask Application (app.py):**

```python
from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import os
import psycopg2

app = Flask(__name__)

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

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

    return render_template('index.html', reviews=reviews)

if __name__ == '__main__':
    app.run(debug=True)
```

**Jinja Template (templates/index.html):**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Restaurant Reviews</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}"
    />
  </head>
  <body>
    <h1>Restaurant Reviews</h1>
    <ul id="review-list">
      {% for review in reviews %}
      <li>
        {{ review[0] }} - Score: {{ review[1] }} - Reviewed by: {{ review[2] }}
      </li>
      {% endfor %}
    </ul>
  </body>
</html>
```

**CSS (static/style.css):**

```css
#review-list {
  list-style: none;
  padding: 0;
}

#review-list li {
  border: 1px solid #ccc;
  padding: 10px;
  margin-bottom: 5px;
}
```
