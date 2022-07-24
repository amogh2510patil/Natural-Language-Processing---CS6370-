#Corpi Documents are processed and a word - article matrix is created and stored into a file.
import numpy as np
import os
from sentenceSegmentation import SentenceSegmentation
from tokenization import Tokenization
from inflectionReduction import InflectionReduction
from stopwordRemoval import StopwordRemoval

def preprocess(docs):
# Segment docs
    segmentedDocs = []
    for doc in docs:
        segmentedDoc = SentenceSegmentation().naive(doc)
        segmentedDocs.append(segmentedDoc)
    # Tokenize docs
    tokenizedDocs = []
    for doc in segmentedDocs:
        tokenizedDoc = Tokenization().naive(doc)
        tokenizedDocs.append(tokenizedDoc)
    # Stem/Lemmatize docs
    reducedDocs = []
    for doc in tokenizedDocs:
        reducedDoc = InflectionReduction().reduce(doc)
        reducedDocs.append(reducedDoc)
    # Remove stopwords from docs
    stopwordRemovedDocs = []
    for doc in reducedDocs:
        stopwordRemovedDoc = StopwordRemoval().fromList(doc)
        stopwordRemovedDocs.append(stopwordRemovedDoc)

    preprocessedDocs = stopwordRemovedDocs
    return preprocessedDocs

def check(word):
    if any(chr.isdigit() for chr in word):
        return ""
    return word 

#Reading Corpus
dir_list = os.listdir('corpus//')
docs = []
for file in dir_list:
    with open('corpus//'+file,encoding="utf8") as f:
        try:
            doc = f.read()
        except:
            pass
    docs.append(doc)
    break

#Process the documents
docs = preprocess(docs)
no_of_docs = len(docs)

unique_terms = {check(term) for doc in docs for sentence in doc for term in sentence}

#Building word x article Matrix
doc_term_matrix = {}

print("Build word x article Matrix")
terms = []
for doc in docs:
    terms.append([word for sentence in doc for word in sentence])

#Finding the distribution of a word
for term in unique_terms:
    doc_term_matrix[term] = []
    df = 0
    for doc in terms:
        cnt = doc.count(term)
        doc_term_matrix[term].append(float(cnt))
        if cnt != 0:
            df+=1
    #Multiplying idf value for the word.
    for i in range(len(terms)):
        doc_term_matrix[term][i] = doc_term_matrix[term][i] * np.log(no_of_docs/(df+1))


#Storing the Matrix in a file
import pickle

try:
	file = open('word_article_matrix', 'wb')
	pickle.dump(doc_term_matrix, file)
	file.close()

except:
	print("Something went wrong")
