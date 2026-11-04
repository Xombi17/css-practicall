# 20. SQL injection: local demonstration

**Language:** Python

## Idea

Runs an automatic injection attempt against a temporary in-memory SQLite database, then repeats it with a parameterized query. The unsafe string-built query accepts the injected login; the safe query treats the input as data and rejects it. The demo prints the unsafe query so you can explain how it changed. It never connects to a real database.

## Run

Run with `python main.py`.
