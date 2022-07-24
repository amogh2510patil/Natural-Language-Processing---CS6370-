from util import *
from nltk.tokenize import PunktSentenceTokenizer
import re
# Add your import statements here
delimiters = '[.?!]'

class SentenceSegmentation():
    
    def naive(self, text):
        if isinstance(text, str):
            segmentedText = re.split(delimiters, text)  #Split wherever ./?/! occurs
            if '' in segmentedText:
                segmentedText.remove('')
            return segmentedText
        else:
            print("Error in argument...")
            return 0
    
    def punkt(self, text):
        if isinstance(text, str):
            tokenizer = PunktSentenceTokenizer(text)
            segmentedText = tokenizer.tokenize(text)
            return segmentedText
        else:
            print("Error in argument...")
            return 0