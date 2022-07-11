# 💎 TONRECOVER (NOT WORKING CURRENTLY)
Tonrecover (like btcrecover) is utility, to search all seed-phrase for your forgotten ton wallet.
Currently it works in Python with `ton` library, but we got plan`s to move some perfomance
modules to Rust. This tool will brute-force all diffirent combinations with your known words.
## Installation

Use Python 3.10 and install all requirements using this command:


`pip install -r requirements.txt`

## Usage

`python tonrecover.py <words>`
Just enter all words that you know, use `?` symbol, if you don`t remember next word

Example:
`python tonrecover.py blast toe ? true`
