from progress.bar import Bar
from progress.spinner import Spinner
from modules.wordlist import words
import itertools
import ton
from time import sleep


def generate(array):
    lenght = 24-len(array) # lenght of words we need to find
    bar = Bar('Generating', max=(2047**lenght)/lenght, suffix='%(percent)d%%')
    for word in itertools.combinations(words, lenght):
        print(word) #TODO: check seed-phrase balance
        currentPhrase = ' '.join(array)+' '+' '.join(word) #look`s shitty but works
        sleep(1)
        # print(currentPhrase)
        bar.next()
