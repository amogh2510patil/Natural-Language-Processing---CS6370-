from util import *

# Add your import statements here
from nltk.stem.snowball import SnowballStemmer
#the stemmer requires a language parameter
snow_stemmer = SnowballStemmer(language='english')

# from nltk.stem import PorterStemmer
  
# ps = PorterStemmer()

class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		
		# Using Lemmatizer

		#lemmatizer = nltk.stem.WordNetLemmatizer()
		#return [lemmatizer.lemmatize(w,'v') for w in text]
		

		# Using Stemming
		
		reducedText = [["" for j in range(len(text[i]))] for i in range(len(text))]
		for i,sentence in enumerate(text):
			for j,word in enumerate(sentence):
				#reducedText[i][j] = ps.stem(word) # Using Porter Stemmer
				reducedText[i][j] = snow_stemmer.stem(word) # Using Snowball Stemmer
		return reducedText
