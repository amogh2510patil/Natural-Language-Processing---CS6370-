from util import *

# Add your import statements here
import nltk
from nltk.stem import PorterStemmer
from collections import defaultdict
import numpy as np
from numpy.linalg import norm

def cosine_similarity(v1, v2):
    epsilon = 0.0001
    vec1 = np.array(v1) 
    vec1 = vec1 + np.full(vec1.shape, epsilon)
    vec2 = np.array(v2)
    vec2 = vec2 + np.full(vec2.shape, epsilon)
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2)) 


class InformationRetrieval():

    def __init__(self):
        self.index = None

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

        termFrequencyTable = defaultdict(defaultdict)
        i = 0
        self.docIDs = docIDs
        index2 = {}
        words_in_doc = {}

        for doc in docs:
            words_in_doc[docIDs[i]] = 0
            for sent in doc:
                for word in sent:
                    if word not in index2.keys():
                        index2[word] = [docIDs[i]]
                    else:
                        if(docIDs[i] not in index2[word]):
                            index2[word].append(docIDs[i])



                    if(word not in termFrequencyTable[docIDs[i]].keys()):
                        termFrequencyTable[docIDs[i]][word] = 1
                    else:
                        termFrequencyTable[docIDs[i]][word] += 1
                    
                    words_in_doc[docIDs[i]] += 1
            i += 1

        self.tf_idf = {}

        i = 0
        for doc in termFrequencyTable.keys():
            self.tf_idf[doc] = [0.0] * len(index2.keys())
            for word in termFrequencyTable[doc].keys():
                ind = list(index2.keys()).index(word)
                self.tf_idf[doc][ind] = (termFrequencyTable[doc][word] / (words_in_doc[docIDs[i]]+0.0001)) * np.log(len(docIDs)/ (len(index2[word])+0.0001))
            i += 1
        #print(index2)
        self.index = index2


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

        doc_IDs_ordered = []

        #Fill in code here
        vocabulary = list(self.index.keys())
        termFrequency = {}
        comparisions = []

        for query in queries:
            count = 0 
            for sent in query:
                for word in sent:
                    count += 1
                    if word not in vocabulary:
                        continue
                    if(word not in termFrequency):
                        termFrequency[word] = 1
                    else:
                        termFrequency[word] += 1
            
            queryVector = [0] * len(self.index.keys())
            for word in termFrequency.keys():
                ind = list(self.index.keys()).index(word)
                queryVector[ind] = (termFrequency[word] / (count+0.0001)) * np.log(len(self.docIDs) / (len(self.index[word])+0.0001))
            
            count = 0
            termFrequency = {}

            similarities = {}
            for doc in self.tf_idf.keys():
                similarities[doc] = cosine_similarity(self.tf_idf[doc], queryVector)
            
            similarities = {k : v for k, v in sorted(similarities.items(), key= lambda item : item[1], reverse=True)}
            comparisions.append(list(similarities.keys()))

        doc_IDs_ordered = comparisions


        return doc_IDs_ordered




