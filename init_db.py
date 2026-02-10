import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Insert a dummy user (admin / password123)
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))
    print("User 'admin' created successfully.")
except sqlite3.IntegrityError:
    print("User 'admin' already exists.")

conn.commit()
conn.close()
print("Database initialized.")