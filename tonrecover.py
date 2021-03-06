from modules.wordlist import words
from modules.brute import generate
import sys

# TODO: Move this all messages to module
helpMsg = '''\033[96m _                                               
| |_ ___  _ __  _ __ ___  ___ _____   _____ _ __ 
| __/ _ \| '_ \| '__/ _ \/ __/ _ \ \ / / _ \ '__|
| || (_) | | | | | |  __/ (_| (_) \ V /  __/ |   
 \__\___/|_| |_|_|  \___|\___\___/ \_/ \___|_|   \033[00m
    by @lux01sv👻

  -s, --silent          Output only when found something\n
Usage:
  (Example) main.py blast abadon crater ? true
'''

def main():
    knownWords = []
    start = False
    print(len(sys.argv))
    # Display help msg if no arguments
    if len(sys.argv) == 1:
        print(helpMsg)
    # Argument handler
    for arg in sys.argv:
        if arg[0] == '-':
            if arg == '--help' or arg == '-h':
                print(helpMsg)
        if arg != "python" and arg != "tonrecover.py":
            if arg in words:
                knownWords.append(arg)
            elif arg == "?":
                knownWords.append(0)
            else:
                print("\033[91mERROR:\033[00m Word \""+arg+"\" is not correct.")
                break
    #print(knownWords)
    if len(knownWords) > 24:
        print("\033[91mERROR:\033[00m"+'''
        You entered more than 24 words. do you really need tonrecover?
        Use -h for help
        ''')
    elif len(knownWords) <= 15:
        print("\u001b[33mWARNING:\033[00m"+'''
        You entered less than 15 words. Seed-phrase search will take forever
        ''')
    if input("Start? (y\\n)") == 'y':
        start = True
    else:
        sys.exit()
    if start:
        generate(knownWords)

if __name__ == "__main__":
    main()
