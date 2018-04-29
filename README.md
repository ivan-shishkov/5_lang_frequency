# Frequency Analysis of Words

This script is intended for print of ten most frequent words in text file.

# Quickstart

For script launch need to install Python 3.5.

Usage:

```bash

$ python3 lang_frequency.py -h
usage: lang_frequency.py [-h] filename

positional arguments:
  filename    an analyzed text file in UTF-8 encoding

optional arguments:
  -h, --help  show this help message and exit

```

Example of script launch on Linux:

```bash

$ python3 lang_frequency.py pep-0008.txt

      Most frequent words in text
----------------------------------------
|           Word           |   Count   |
----------------------------------------
| the                      |    302    |
----------------------------------------
| to                       |    170    |
----------------------------------------
| a                        |    165    |
----------------------------------------
| and                      |    118    |
----------------------------------------
| in                       |    116    |
----------------------------------------
| is                       |    115    |
----------------------------------------
| of                       |    109    |
----------------------------------------
| for                      |    85     |
----------------------------------------
| are                      |    84     |
----------------------------------------
| be                       |    80     |
----------------------------------------

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
