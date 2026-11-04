# CSS Cryptography and System Security Practicals

Beginner study set for the 22 questions in the supplied practical sheet. Each numbered folder contains one self-contained program and a short explanation. Python programs use only the standard library; C is used for the two C-specific buffer examples.

## How to study

1. Read the `Idea` section before running the program.
2. Trace a small input by hand (for letter ciphers, use A=0 through Z=25).
3. Run the program and compare its output with your trace.
4. Change one input/key and explain what changed.

## Question index

| Practical | Language |
|---|---|
| [01. Product cipher: substitution + transposition](./01-product-cipher/README.md) | Python |
| [02. Salt and pepper password protection](./02-salt-pepper-password/README.md) | Python |
| [03. Shift cipher](./03-shift-cipher/README.md) | Python |
| [04. Additive cipher](./04-additive-cipher/README.md) | Python |
| [05. Multiplicative cipher](./05-multiplicative-cipher/README.md) | Python |
| [06. Vernam cipher (one-time pad)](./06-vernam-one-time-pad/README.md) | Python |
| [07. Vigenere cipher](./07-vigenere-cipher/README.md) | Python |
| [08. Playfair cipher: same row / same column](./08-playfair-row-column/README.md) | Python |
| [09. Compare MD5 and SHA-1 speed](./09-md5-sha1-timing/README.md) | Python |
| [10. Hill cipher: encrypt DIAL (2×2)](./10-hill-cipher-dial/README.md) | Python |
| [11. Affine cipher](./11-affine-cipher/README.md) | Python |
| [12. RSA public-key encryption](./12-rsa-encryption/README.md) | Python |
| [13. RSA digital signature (toy)](./13-rsa-digital-signature/README.md) | Python |
| [14. Diffie–Hellman key exchange](./14-diffie-hellman/README.md) | Python |
| [15. Hill cipher: encrypt DONE (2×2)](./15-hill-cipher-done/README.md) | Python |
| [16. Simple columnar cipher: 4 columns](./16-columnar-cipher-4-col/README.md) | Python |
| [17. Simple columnar cipher: 3 columns](./17-columnar-cipher-3-col/README.md) | Python |
| [18. First three totient rules](./18-totient-rules/README.md) | Python |
| [19. Even-position then odd-position transposition](./19-even-odd-transposition/README.md) | Python |
| [20. SQL injection: local demonstration](./20-sql-injection-demo/README.md) | Python |
| [21. Buffer overflow: gets() and strcpy()](./21-overflow-gets-strcpy/README.md) | C |
| [22. Buffer overflow: strcat() and sprintf()](./22-overflow-strcat-sprintf/README.md) | C |

## Notes about the supplied sheet

- The matrices are absent from the question sheet, but the supplied ZIP provides candidate keys for questions 10 and 15; these are now used in the programs and identified in their READMEs.
- Questions 16 and 17 do not give a column read order/key; these use the basic left-to-right column order.
- Question 18 uses the three listed totient rules and falls back to counting coprime values for other positive inputs. The sheet’s φ(1)=0 differs from the standard convention φ(1)=1.
- The MD5/SHA-1 example expects a file path and reports its byte count; use a 1,024-byte file for the specified 1 KiB input.
- Question 20 is a safe, local in-memory SQL example. The buffer programs intentionally contain unsafe C calls for lab study; do not use them with valuable data or on a connected system.
