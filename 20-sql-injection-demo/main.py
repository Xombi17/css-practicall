# This demo uses only a temporary in-memory database.
import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE users (username TEXT, password TEXT)")
db.execute("INSERT INTO users VALUES (?, ?)", ("admin", "secret123"))

username = input("Username (try: ' OR '1'='1' --): ")
password = input("Password (normal login: secret123): ")
unsafe_query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
unsafe_login = db.execute(unsafe_query).fetchone() is not None
safe_login = db.execute(
    "SELECT * FROM users WHERE username=? AND password=?", (username, password)
).fetchone() is not None

print("Unsafe query:", unsafe_query)
print("Unsafe login accepted:", unsafe_login)
print("Parameterized login accepted:", safe_login)
print("The safe query treats the entered text as data, not SQL.")
db.close()
