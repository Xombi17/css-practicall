# 09. Compare MD5 and SHA-1 speed

**Language:** Python

## Idea

Reads bytes (so text encoding does not alter the input), then times one digest operation for each algorithm. Ensure your input file is exactly 1,024 bytes for a 1 KiB comparison. Timing one run is noisy; repeat runs for a better comparison. MD5 and SHA-1 are not secure for modern integrity/signature use.

## Run

Run with `python main.py`.
