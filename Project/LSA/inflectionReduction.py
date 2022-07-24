from util import *
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet




        


# Add your import statements here




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
		

		#Fill in code here

		# stemming 
		
		# stemmer = PorterStemmer()
		# reducedText = [[ stemmer.stem(word) for word in sentence] for sentence in text]
		


		# Lemmatization 

		lemmatizer = WordNetLemmatizer()
		reducedText=[]
		for sentence in text:
			reducedSentence=[]
			sentence_pos_tag = nltk.pos_tag(sentence)   #  POS-tagging using nltk of each word
			sentence_pos_tagged=[]

			for word,tag in sentence_pos_tag:
				if(tag[0]=='J'):
					sentence_pos_tagged.append((word,'a'))  # POS-tagging according to wordnet eg: 'a' for adjective, 'n' for noun, 'v' for verb, 'r' for adverb
				elif(tag[0]=='V'):
					sentence_pos_tagged.append((word,'v'))
				elif(tag[0]=='N'):
					sentence_pos_tagged.append((word,'n'))
				elif(tag[0]=='R'):
					sentence_pos_tagged.append((word,'r'))
				else:
					sentence_pos_tagged.append((word,None))

			for word,tag in sentence_pos_tagged:
				if(tag==None):
					reducedSentence.append(word)
				else:
					reducedSentence.append(lemmatizer.lemmatize(word, pos=tag))  # each word  with pos specified gets lemmatized 

			reducedText.append(reducedSentence)
					
		return reducedText


