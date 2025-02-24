import sqlite3

# Connect to SQLite database (creates 'quiz_data.db' if it doesn't exist)
conn = sqlite3.connect("quiz_data.db")  
cursor = conn.cursor()

# Create Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
)
""")

# Create Quiz Scores table
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS quiz_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    score INTEGER NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Create Image Search History table
cursor.execute("""
CREATE TABLE IF NOT EXISTS image_search_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    search_term TEXT NOT NULL,
    image_url TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Commit changes and close connection
conn.commit()
conn.close()

def add_user(username):
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        print(f"User '{username}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
    
    conn.close()

def add_quiz_score(username, score):
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()
    
    # Get user ID
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        user_id = user[0]
        cursor.execute("INSERT INTO quiz_scores (user_id, score) VALUES (?, ?)", (user_id, score))
        conn.commit()
        print(f"Score {score} added for user '{username}'.")
    else:
        print(f"User '{username}' not found.")
    
    conn.close()

def add_image_search(username, search_term, image_url):
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()
    
    # Get user ID
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        user_id = user[0]
        cursor.execute("INSERT INTO image_search_history (user_id, search_term, image_url) VALUES (?, ?, ?)",
                       (user_id, search_term, image_url))
        conn.commit()
        print(f"Search '{search_term}' added for user '{username}'.")
    else:
        print(f"User '{username}' not found.")
    
    conn.close()

def get_quiz_scores(username):
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT quiz_scores.score, quiz_scores.timestamp 
    FROM quiz_scores
    JOIN users ON quiz_scores.user_id = users.id
    WHERE users.username = ?
    """, (username,))
    
    scores = cursor.fetchall()
    
    conn.close()
    return scores

def get_image_search_history(username):
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT image_search_history.search_term, image_search_history.image_url, image_search_history.timestamp 
    FROM image_search_history
    JOIN users ON image_search_history.user_id = users.id
    WHERE users.username = ?
    """, (username,))
    
    history = cursor.fetchall()
    
    conn.close()
    return history


    
