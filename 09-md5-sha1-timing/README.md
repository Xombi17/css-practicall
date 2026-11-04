# 09. Compare MD5 and SHA-1 speed

**Language:** Python

## Idea

Prompts for a file path, shows the number of bytes read, each fixed-length digest, and the time for each hash. It hashes identical bytes with Python's `hashlib.md5` and `hashlib.sha1`. Use exactly 1,024 bytes for the requested 1 KiB test. Timing one run is illustrative and does not establish which algorithm is generally faster.

## Run

Run with `python main.py`.
