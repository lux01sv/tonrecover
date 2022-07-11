from progress.bar import Bar
from modules.wordlist import words
import itertools


def generate(array):
    lenght = 24-len(array) # lenght of words we need to find
    bar = Bar('Generating', max=2048**lenght, suffix='%(percent)d%%')
    for word in itertools.combinations(words, lenght):
        print(word) #TODO: check seed-phrase balance
        bar.next()
    bar.finish()