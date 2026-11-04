# CSS Practical Study

The programs below are copied verbatim from [AnushkaKedare/css-pracs](https://github.com/AnushkaKedare/css-pracs). The source repository uses Python for Q1–Q20 and C for Q21–Q22.

## Practicals

| No. | Topic | Folder | Language |
|---:|---|---|---|
| 1 | Product cipher | `01-product-cipher` | Python |
| 2 | Salt and pepper password protection | `02-salt-pepper-password` | Python |
| 3 | Shift cipher | `03-shift-cipher` | Python |
| 4 | Additive cipher | `04-additive-cipher` | Python |
| 5 | Multiplicative cipher | `05-multiplicative-cipher` | Python |
| 6 | Vernam cipher (one-time pad) | `06-vernam-one-time-pad` | Python |
| 7 | Vigenere cipher | `07-vigenere-cipher` | Python |
| 8 | Playfair cipher | `08-playfair-row-column` | Python |
| 9 | MD5 vs SHA-1 speed | `09-md5-sha1-timing` | Python |
| 10 | Hill cipher: DIAL | `10-hill-cipher-dial` | Python |
| 11 | Affine cipher | `11-affine-cipher` | Python |
| 12 | RSA public key cryptography | `12-rsa-encryption` | Python |
| 13 | RSA digital signature | `13-rsa-digital-signature` | Python |
| 14 | Diffie-Hellman key exchange | `14-diffie-hellman` | Python |
| 15 | Hill cipher: DONE | `15-hill-cipher-done` | Python |
| 16 | Columnar transposition: 4 columns | `16-columnar-transposition` | Python |
| 17 | Columnar transposition: 3 columns | `17-columnar-transposition-3-col` | Python |
| 18 | Euler totient function | `18-totient-rules` | Python |
| 19 | Even/odd position transposition | `19-even-odd-transposition` | Python |
| 20 | SQL injection demonstration | `20-sql-injection-demo` | Python |
| 21 | Buffer overflow: gets and strcpy | `21-overflow-gets-strcpy` | C |
| 22 | Buffer overflow: strcat and sprintf | `22-overflow-strcat-sprintf` | C |

## Run a practical

For Python, enter its folder and run:

```sh
python3 main.py
```

Q9 also includes the sample 1 KB file from the source repository.

For C, enter the practical folder and compile:

```sh
gcc -std=gnu89 -w main.c -o main
./main
```

Q21–Q22 contain the original unsafe C buffer examples. They are educational samples; do not run them with sensitive data or outside a disposable local environment.

Source snapshot: `23ac9eee2285a63dcded7c694f6eb5b11c3fbdc9`.
