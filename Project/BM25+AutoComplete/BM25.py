# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:53:25 2022

@author: Ritwiz
"""
from collections import Counter
import math

class My_BM25():

    def __init__(self):
        self.index = None
        self.docIDs = None
        self.adl = 0
        self.dls = []

    def buildIndex(self, docs, docIDs):
        index = {}
        tot_doc_len = 0
        dls = []
        for doc in docs:
            tot_doc_len += len(doc)
            dls.append(len(doc))
            doc_ID = docIDs[docs.index(doc)]
            all_terms = [term for sentence in doc for term in sentence]
            for term, frequency in list(Counter(all_terms).items()):
                try:
                    index[term].append([doc_ID, frequency])
                except:
                    index[term] = [[doc_ID,frequency]]

        self.docIDs = docIDs
        self.index = index
        self.adl = tot_doc_len/len(docIDs)
        self.dls = dls


    def rank(self, queries):
        doc_IDs_ordered = []

        index = self.index
        docIDs = self.docIDs
        adl = self.adl
        dls = self.dls
        dls = [i/adl for i in dls]
        #print(adl)
        #print(dls[0:10])
        inv_frequency = {}
        null = {}
        num_docs = len(docIDs)

        #IDF defined in a new way
        for term in index:
            num_terms = len(index[term])
            inv_frequency[term] = math.log10(float((num_docs-num_terms+0.5)/(num_terms+0.5)))
            null[term] = 0

        # Representing in tf-idf vector space
        documents = {}
        for doc_ID in docIDs:
            documents[doc_ID] = null.copy()

        for term in index:
            for doc_ID, frequency in index[term]:
                bm25k=1.85
                bm25b=0.8
                #print(len(docIDs))
                et = bm25k*(1-bm25b+(bm25b*dls[doc_ID-1]))
                documents[doc_ID][term] = (frequency/(frequency + et)) * inv_frequency[term]

		# Representing queries in tf-idf vector space
        tot_query_len = len(queries)
        qls = []
        for query in queries:
            qls.append(len(query))
        qal = sum(qls)/tot_query_len
        qls = [i/qal for i in qls]
        for query in queries:
            query_vector = null.copy()
            terms = [term for sentence in query for term in sentence]
            bm25k=1.85
            bm25b=0.8
            temp = queries.index(query)
            et = bm25k*(1-bm25b+(bm25b*qls[temp]))
            for term, frequency in list(Counter(terms).items()):
                try:
                    query_vector[term] =  (frequency/(frequency + et)) * inv_frequency[term]
                except:
                    pass

            similarities = {}
            for doc_ID in docIDs:
                try:
                    similarities[doc_ID] = sum(documents[doc_ID][key] * query_vector[key] for key in index) / (math.sqrt(sum(documents[doc_ID][key] * documents[doc_ID][key] for key in index)) * math.sqrt(sum(query_vector[key] * query_vector[key] for key in index)))
                except:
                    similarities[doc_ID] = 0
            doc_IDs_ordered.append([docID for docID, tf in sorted(similarities.items(), key=lambda item: item[1], reverse = True)])

        return doc_IDs_ordered