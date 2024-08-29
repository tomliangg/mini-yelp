**1. Retrieving Data:**

* **Get all reviews:**
  ```sql
  SELECT * FROM reviews;
  ```

* **Get reviews for a specific restaurant:**
  ```sql
  SELECT * FROM reviews WHERE restaurant_name = 'The Italian Place';
  ```

* **Get reviews with a score above 8:**
  ```sql
  SELECT * FROM reviews WHERE scores > 8;
  ```

* **Get reviews in a specific city, ordered by score (descending):**
  ```sql
  SELECT * FROM reviews WHERE city = 'New York' ORDER BY scores DESC;
  ```

* **Get the top 5 highest-rated restaurants:**
  ```sql
  SELECT restaurant_name, AVG(scores) AS average_score
  FROM reviews
  GROUP BY restaurant_name
  ORDER BY average_score DESC
  LIMIT 5;
  ```


**2. Inserting Data:**

* **Inserting a single row:**
  ```sql
  INSERT INTO reviews (created_at, restaurant_name, city, state, scores, reviewer_id, comment) 
  VALUES ('2023-10-30T10:00:00Z', 'New Restaurant', 'San Diego', 'CA', 8, 101, 'Great food and atmosphere!');
  ```

* **Inserting multiple rows:**
  ```sql
    INSERT INTO reviews (created_at, restaurant_name, city, state, scores, reviewer_id, comment)
    VALUES 
        ('2023-10-30T11:00:00Z', 'Another Restaurant', 'New York', 'NY', 7, 102, 'Decent food, good service.'),
        ('2023-10-30T12:00:00Z', 'Yet Another Restaurant', 'Chicago', 'IL', 9, 103, 'Excellent food and service!');
  ```

**3. Updating Data:**

* **Update a review's comment:**
  ```sql
  UPDATE reviews SET comment = 'Updated comment' WHERE id = 1;
  ```

* **Increase the score of a review by 1:**
  ```sql
  UPDATE reviews SET scores = scores + 1 WHERE id = 2;
  ```

**4. Deleting Data:**

* **Delete a specific review:**
  ```sql
  DELETE FROM reviews WHERE id = 3;
  ```

* **Delete reviews for a specific restaurant:**
  ```sql
  DELETE FROM reviews WHERE restaurant_name = 'Burger Joint';
  ```

**5. Aggregation and Grouping:**

* **Get the average score for each restaurant:**
  ```sql
  SELECT restaurant_name, AVG(scores) AS average_score FROM reviews GROUP BY restaurant_name;
  ```

* **Count the number of reviews for each city:**
  ```sql
  SELECT city, COUNT(*) AS review_count FROM reviews GROUP BY city;
  ```

**6. Searching:**

* **Find reviews containing a specific keyword (e.g., "delicious"):**
  ```sql
  SELECT * FROM reviews WHERE comment LIKE '%delicious%';
  ```

**Important Notes:**
* **Data Types:** Be mindful of data types when filtering or updating data (e.g., use single quotes for string values).
* **`WHERE` Clause:** Use the `WHERE` clause to filter results based on specific criteria.
* **`ORDER BY` Clause:** Use the `ORDER BY` clause to sort results based on one or more columns.
* **`LIMIT` Clause:** Use the `LIMIT` clause to restrict the number of rows returned.
* **`GROUP BY` Clause:** Use the `GROUP BY` clause to group rows based on one or more columns, often used with aggregate functions like `AVG` or `COUNT`.
* **`LIKE` Operator:** Use the `LIKE` operator with wildcard characters (`%`) for pattern matching in text data.
