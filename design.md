## Design Document: Simple Restaurant Review Web Application

**Requirements:**
* App users can see a list of reviews sorted by scores in DESC order. Each item of the list should include these info: name of restaurant, score, reviewer name (first name + last name).

**Requirements Analysis:**

* The frontend fetches review data from the `/api/reviews` endpoint and dynamically creates list items to display the data.
* The backend connects to the Supabase database, executes a SQL query to join the `reviews` and `reviewers` tables, retrieves the necessary data, and returns it as a JSON response.

**1. Introduction**

This document outlines the design of a simple full-stack web application similar to Yelp, focusing on displaying restaurant reviews. The application will use HTML, CSS, and JavaScript for the frontend, Python Flask for the backend, and Supabase as the database.

**2. System Architecture**

The application will follow a basic client-server architecture:

* **Frontend (Client):**
    * HTML, CSS, and JavaScript will be used to create a user interface for displaying the list of reviews.
    * JavaScript will handle fetching data from the backend via AJAX requests.
* **Backend (Server):**
    * Python Flask will handle API requests from the frontend.
    * Flask will interact with the Supabase database to retrieve and process data.
* **Database (Supabase):**
    * Supabase will store the restaurant reviews and reviewer information in two tables: `reviews` and `reviewers`.

**3. Data Model**

The database schema is as follows:

**Table: `reviews`**

| Column Name | Data Type | Description |
|---|---|---|
| id | bigint (primary key) | Unique identifier for each review |
| created_at | timestamp with time zone | Timestamp of review creation |
| restaurant_name | text | Name of the restaurant |
| city | text | City where the restaurant is located |
| state | text | State where the restaurant is located |
| scores | smallint | Review score (0-10) |
| reviewer_id | bigint (foreign key) | ID of the reviewer |
| comment | text | User's review comment |

**Table: `reviewers`**

| Column Name | Data Type | Description |
|---|---|---|
| id | bigint (primary key) | Unique identifier for each reviewer |
| first_name | character varying | Reviewer's first name |
| last_name | character varying | Reviewer's last name |
| email | text | Reviewer's email address |

**4. API Endpoints**

The backend will expose a single API endpoint:

* **`GET /api/reviews`:**
    * Returns a list of reviews sorted by `scores` in descending order.
    * Each review object will include:
        * `restaurant_name`
        * `scores`
        * `reviewer_name` (concatenated first and last name from the `reviewers` table)

**5. Frontend Functionality**

* The frontend will make an AJAX request to the `/api/reviews` endpoint to fetch the review data.
* The received data will be used to dynamically generate an HTML list of reviews.
* Each list item will display the restaurant name, score, and reviewer name.

**6. Implementation Details**

* **Frontend:**
    * HTML will structure the page with a container for the review list.
    * CSS will style the list items for readability.
    * JavaScript will use `fetch` or `XMLHttpRequest` to make the API request and update the HTML with the review data.
* **Backend (Flask):**
    * A Flask route will be defined for the `/api/reviews` endpoint.
    * The route handler will query the Supabase database using the `psycopg2` library (or a Supabase client library).
    * The query will join the `reviews` and `reviewers` tables, select the required columns, and order by `scores` in descending order.
    * The result will be converted to JSON and returned as the API response.

**7. Deployment**

The application can be deployed to a platform that supports Python Flask applications, such as Heroku, PythonAnywhere, or AWS.

## Code Implementation

**Frontend (index.html):**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Reviews</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Restaurant Reviews</h1>
    <ul id="review-list"></ul>

    <script src="script.js"></script>
</body>
</html>
```

**Frontend (style.css):**

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

**Frontend (script.js):**

```javascript
fetch('/api/reviews')
    .then(response => response.json())
    .then(reviews => {
        const reviewList = document.getElementById('review-list');
        reviews.forEach(review => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${review.restaurant_name}</strong> - Score: ${review.scores} - Reviewed by: ${review.reviewer_name}`;
            reviewList.appendChild(li);
        });
    });
```

**Backend (app.py):**

```python
from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL'] 

@app.route('/api/reviews')
def get_reviews():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()

    cur.execute("""
        SELECT r.restaurant_name, r.scores, rev.first_name || ' ' || rev.last_name AS reviewer_name
        FROM reviews r
        JOIN reviewers rev ON r.reviewer_id = rev.id
        ORDER BY r.scores DESC;
    """)

    reviews = []
    for row in cur.fetchall():
        reviews.append({
            'restaurant_name': row[0],
            'scores': row[1],
            'reviewer_name': row[2]
        })

    cur.close()
    conn.close()

    return jsonify(reviews)

if __name__ == '__main__':
    app.run(debug=True)
```
