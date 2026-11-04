# 21. Buffer overflow: gets() and strcpy()

**Language:** C

## Idea

gets() can write beyond input because it has no size argument. strcpy() can write beyond name when input exceeds 7 characters plus the terminator. This is deliberately vulnerable classroom code: run only in an isolated lab with harmless input; modern C libraries may no longer provide gets().

## Run

Compile with `gcc main.c -o demo` and run `./demo` (only in an isolated lab).
