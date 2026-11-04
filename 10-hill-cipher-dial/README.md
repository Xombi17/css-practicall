# 10. Hill cipher: encrypt DIAL (2×2)

**Language:** Python

## Idea

Maps A=0 through Z=25, then multiplies each pair by the provided key matrix `[[3, 3], [2, 5]]` modulo 26. This matrix comes from the supplied ZIP; it was not visible in the original question sheet. Confirm it is the one your instructor expects.

## Run

Run with `python main.py`.
