# 22. Buffer overflow: strcat() and sprintf()

**Language:** C

## Idea

Choose one operation at a time so one overflow does not interfere with the other. A long name makes strcat write past message’s end; sprintf also has no destination-size limit. Input uses bounded fgets, but the requested operations remain unsafe. Run only in an isolated lab with harmless input.

## Run

Compile with `gcc main.c -o demo` and run `./demo` (only in an isolated lab).
