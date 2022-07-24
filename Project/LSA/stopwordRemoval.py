from util import *
from nltk.corpus import stopwords
 

# Add your import statements here




class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		stopWords = stopwords.words('english')

		stopwordRemovedText=[]
		
		for sentence in text:
			stopwordRemovedSentence = []
			for word in sentence:
				if word not in stopWords and len(word)>1:  # stopword removal using top down knowledge and removing words with length less than or equal to 1.
					stopwordRemovedSentence.append(word)
			stopwordRemovedText.append(stopwordRemovedSentence)


		#Fill in code here

		return stopwordRemovedText




	