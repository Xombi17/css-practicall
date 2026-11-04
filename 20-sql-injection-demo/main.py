# SQL Injection attack - demonstration on a LOCAL toy database
# Shows WHY building a query by joining strings is unsafe, then the safe fix.
#
# Attack idea: type SQL inside the username box so the password check is skipped.
# Payload used:  ' OR '1'='1' --
#   - the  ' OR '1'='1'  part makes the WHERE condition always TRUE
#   - the  --  turns the rest of the line into a comment, so the password
#     check is thrown away completely.

import sqlite3

# set up a small in-memory database with one user
db = sqlite3.connect(":memory:")
cur = db.cursor()
cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES ('admin', 'secret123')")
db.commit()

def login_unsafe(username, password):
    # BAD: query is built by joining strings -> injectable
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    print("Query sent:", query)
    cur.execute(query)
    return cur.fetchall()

def login_safe(username, password):
    # GOOD: placeholders (?), input is treated as data, not SQL
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cur.fetchall()

attacker_user = "' OR '1'='1' --"
attacker_pass = "anything"

print("=== Attack on the UNSAFE login ===")
rows = login_unsafe(attacker_user, attacker_pass)
if rows:
    print("Logged in WITHOUT a valid password! Rows returned:", rows)
else:
    print("Login failed")

print()
print("=== Same attack on the SAFE login ===")
rows = login_safe(attacker_user, attacker_pass)
if rows:
    print("Logged in:", rows)
else:
    print("Login blocked - injection did not work")

db.close()
