from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach
		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence
		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		#text is a list
		tokenizedText = [[] for i in range(len(text))]

		#Fill in code here

		#string punctuation '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
		sent_list_cleaned = []
		for i in range(len(text)):
			txt = text[i] #access individual string (sentence)
			txt = re.sub(r"'", "", txt) #remove "'" and join both the words. prandtl's -> prandtls
			txt = re.sub(r"[^a-zA-Z0-9.=\+]", " ", txt) #remove all punctuation except, letters, numbers, '.', '=', '()' and '-'. Replace with ' '
			txt = re.sub(r"\s{2,}", " ", txt) #remove all spaces >= 2
			#txt = txt.replace(' .', '') #replace ' .' with ''
			#input cleaned list of sentences
			tokens = txt.split()
			tokenizedText[i] = tokens

		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer
		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence
		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = [[] for i in range(len(text))]

		#Fill in code here
		penn_tokenizer = TreebankWordTokenizer()

		for i in range(len(text)):
			#input cleaned list of sentences
			tokens = penn_tokenizer.tokenize(text[i])
			tokenizedText[i] = tokens

		return tokenizedText