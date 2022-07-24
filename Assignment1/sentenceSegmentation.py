from util import *

# Add your import statements here
import re
import nltk

class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""
		
		segmentedText = re.split('\.\s|\?\s|!\s',text)
		segmentedText[-1] = segmentedText[-1][:-1] if (segmentedText[-1][-1] == '.' or segmentedText[-1][-1] == '?' or segmentedText[-1][-1] == '!') else segmentedText[-1]
		return segmentedText


	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = nltk.tokenize.sent_tokenize(text)
		# sent_tokenize uses a pre-trained model from nltk_data/tokenizers/punkt/english.pickle
		# If we want to train our own model we can do so by using:
		#tokenizer = nltk.tokenize.PunktSentenceTokenizer(text)
		#segmentedText = tokenizer.tokenize(text)
		# This works best when there is separate training text to train from and then we can use the tokenizer on it. 
		# Using this here would not yield the best results, as the tokenizer uses an unsupervised learning algorithm, 
		# and would overfit to a very small dataset
		
		return segmentedText