# 20. SQL injection: local demonstration

**Language:** Python

## Idea

Prompts for username and password. Try username `' OR '1'='1' --` with any password: the unsafe query accepts it and the parameterized query rejects it. The database is temporary and exists only in memory.

## Run

Run with `python main.py`.
