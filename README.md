# Cryptography and System Security Practicals

This folder now uses the implementations from [shreyshNair/Cryptographic-codes](https://github.com/shreyshNair/Cryptographic-codes). Each practical folder contains the linked program and a short note about its inputs and behavior. Run a Python practical with `python main.py` from that folder.

## Practical index

| No. | Topic | Language |
|---:|---|---|
| 1 | Product cipher | Python |
| 2 | Salt and pepper password protection | Python |
| 3 | Shift cipher | Python |
| 4 | Additive cipher | Python |
| 5 | Multiplicative cipher | Python |
| 6 | Vernam cipher | Python |
| 7 | Vigenere cipher | Python |
| 8 | Playfair cipher | Python |
| 9 | MD5 and SHA-1 comparison | Python |
| 10 | Hill cipher: DIAL | Python |
| 11 | Affine cipher | Python |
| 12 | RSA encryption | Python |
| 13 | RSA digital signature | Python |
| 14 | Diffie–Hellman exchange | Python |
| 15 | Hill cipher: DONE | Python |
| 16 | Columnar transposition: 4 columns | Python |
| 17 | Rail Fence: 3 rails | Python |
| 18 | Euler totient | Python |
| 19 | Even/odd transposition | Python |
| 20 | SQL injection demo | Python |
| 21 | Diffie–Hellman man-in-the-middle demo | Python |
| 22 | Buffer overflow size demo | Python |

## Check against your practical sheet

The linked repository’s Q17 is Rail Fence, while your sheet asks for a 3-column cipher. Its Q21 is a Diffie–Hellman man-in-the-middle demo, while your sheet asks for `gets()`/`strcpy()`. Its Q22 is a Python buffer-size simulation, while your sheet asks for `strcat()`/`sprintf()` in C. The repository’s Q17 program also contains errors in its encryption/decryption calls. Check these differences with your instructor before relying on the reference set for the exam.

Some reference programs use fixed demonstration values; each practical README points those out. Q9 requires an existing `sample.txt` in its run folder. The security demonstrations are educational examples.
