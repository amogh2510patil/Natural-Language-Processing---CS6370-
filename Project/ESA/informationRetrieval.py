from typing import no_type_check
from util import *

# Add your import statements here
import numpy as np
import pickle

class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.dictionary = {}
		self.doc_term_matrix = {}
		self.idf = None
		self.word_article = None
		self.doc_Id = []

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = []
		
		with open('word_article_matrix', 'rb') as handle:
			data = handle.read()
		
		# reconstructing the data as dictionary
		doc_term_matrix = pickle.loads(data)

		id = 0
		for term in doc_term_matrix.keys():
			no_articles = len(doc_term_matrix[term])
			self.dictionary[term] = id
			id+=1
		N_Unique0 = id
		
		#Create a dictionary Id for all the words present across all documents
		for doc in docs:
			for sentence in doc:
				for word in sentence:
					if word not in self.dictionary.keys():
						self.dictionary[word] = id
						id+=1
		N_Unique = id		#number of unique words
		
		word_article = np.zeros((N_Unique,no_articles+N_Unique-N_Unique0))

		#Creating Word x psuedo article Matrix
		i = no_articles
		for word in self.dictionary.keys():
			if word in doc_term_matrix.keys():
				temp = doc_term_matrix[word]
				temp.extend([0 for i in range(N_Unique-N_Unique0)])
				word_article[self.dictionary[word]] = np.array(temp)
			else:
				temp = np.zeros(no_articles+N_Unique-N_Unique0)
				temp[i] = 1
				i+=1
				word_article[self.dictionary[word]] = temp

		#Finding IDF values of all words and the tf-idf representation of the documents
		df = np.zeros(N_Unique)
		for doc in docs:
			doc_tf = np.zeros(N_Unique,dtype='float32')	#Term frequency of words in a given document
			for sentence in doc:
				for word in sentence:
					doc_tf[self.dictionary[word]] += 1
			#Finding all words that occured in the document
			ind = np.where(doc_tf!=0)
			#Incrementing document freq for all words in the document
			df[ind] += 1
			#Appending the term freq of each document
			index.append(doc_tf)
		#Finding the idf of words
		self.idf = np.array(np.log10(len(docs)/(1+df)))
		#TF-IDF representation of all documents
		self.index = index * self.idf
		self.index = np.dot(np.array(self.index), word_article)
		self.word_article = word_article
		# print(self.index.shape)
		self.doc_Id = docIDs
		

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""
		# queries = [queries]
		doc_IDs_ordered = []
		N_Unique = len(self.dictionary.keys())

		#Fill in code here
		for query in queries:
			query_tf = np.zeros(N_Unique)
			for sentence in query:
				for word in sentence:
					try:
						query_tf[self.dictionary[word]] += 1
					except:
						pass

			tf_idf_query = query_tf * self.idf	#Tf-Idf of the query
			tf_idf_query = np.dot(tf_idf_query,self.word_article)
			ind = np.where(tf_idf_query!=0)			#Indexes where its non zero
			cos_sims = []	
			#Cosine Similarity betweeen query and all documents
			for i,doc in enumerate(self.index):
				if len(ind[0])>0:
					cosine_sim = sum(tf_idf_query[ind]*doc[ind])/np.linalg.norm(tf_idf_query)/np.linalg.norm(doc)
				else:
					cosine_sim = 0			
				cos_sims.append((cosine_sim,self.doc_Id[i]))
			#Sorting of the document IDs according to the cosine_similarity values.
			doc_IDs_ordered.append(list(zip(*sorted(cos_sims, key = lambda x: x[0],reverse=True)))[1])
		return doc_IDs_ordered
