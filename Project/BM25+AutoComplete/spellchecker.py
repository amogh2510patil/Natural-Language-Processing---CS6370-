# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:34:26 2022

@author: nency
"""
# import sys
#pip install pyspellchecker
# !{sys.executable} - m pip install pyspellchecker

from util import *
#from nltk.corpus import stopwords
# from nltk.metrics.distance import jaccard_distance
# from nltk.util import ngrams

# from nltk.metrics.distance  import edit_distance
# nltk.download('words')
# from nltk.corpus import words


from textblob import TextBlob
from spellchecker import SpellChecker

# Add your import statements here


class SpellCheck():

    def check(self, text):
        spellCheckedText = []
        for sentence in text:
           spellCheckedSentence = []
           for word in sentence:
              word = TextBlob(word)
              spellCheckedSentence.append(str(word.correct()))
           spellCheckedText.append(spellCheckedSentence)
        
        # correct_words = words.words()
        # for sentence in text:
        
        #     incorrect_words=sentence
        #     for word in incorrect_words:
        #         temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]
        #         #print(sorted(temp, key = lambda val:val[0])[0][1])
                    
        
        # spell = SpellChecker()
        # spellCheckedText=[]
        # for sentence in text:
        #     spellCheckedSentence = []
        #     misspelled = sentence
        #     for word in misspelled:
        #         spellCheckedSentence.append(spell.correction(word))
        #     spellCheckedText.append(spellCheckedSentence)
        
          
                   
        #Fill in code here

        return spellCheckedText




    