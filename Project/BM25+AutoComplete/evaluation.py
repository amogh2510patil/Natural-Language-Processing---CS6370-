#!/usr/bin/env python
# coding: utf-8

from math import log2

# In[1]:

nDCG_vals = []

class Evaluation():
    

    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query

        arg2 : int
        The ID of the query in question
        arg3 : list
        The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
        The k value

        Returns
        -------
        float
        The precision value as a number between 0 and 1
        """


    
        true_set = set(true_doc_IDs) 
        pred_set = set(query_doc_IDs_ordered[:k]) 
        precision = len(true_set & pred_set) / float(k) 


        #Fill in code here
        return precision
    
    
    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries
        
        Parameters
        
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
            
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
            
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
                
        arg4 : int
        The k value
            
        Returns
        -------
        float
        The mean precision value as a number between 0 and 1
        """
        Precisions = []
        meanPrecision = -1
        total_precision = 0
        count = 0
        for i in query_ids:
            true_doc_IDs=[]
            flag=0
            for dic in qrels:
                if(int(dic["query_num"]) == i):
                    flag = 1
                    true_doc_IDs.append(int(dic["id"]))
                elif(flag == 1):
                    break
            total_precision = total_precision + self.queryPrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            temp = self.queryPrecision(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            Precisions.append(temp)
            count = count+1
        meanPrecision = total_precision/count
        
        #Fill in code here
        
        return meanPrecision, Precisions
    
    
    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The recall value as a number between 0 and 1
        """


        total_recall = 0.0
        l = len(query_doc_IDs_ordered)
        count = 0
        for i in range(l):
            true_set = set(true_doc_IDs)
            pred_set = set(query_doc_IDs_ordered[:k])
            if len(true_set) != 0:
                total_recall += len(true_set & pred_set) / float(len(true_set))
                count += 1
        recall = total_recall / count

        return recall
    

    
    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean recall value as a number between 0 and 1
        """
        Recalls = []
        meanRecall = -1
        total_recall = 0
        count = 0
        for i in query_ids:
            true_doc_IDs=[]
            flag=0
            for dic in qrels:
                if(int(dic["query_num"]) == i):
                    flag = 1
                    true_doc_IDs.append(int(dic["id"]))
                elif(flag == 1):
                    break
            total_recall = total_recall + self.queryRecall(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            temp = self.queryRecall(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            Recalls.append(temp)
            count = count+1
        meanRecall = total_recall/count

        #Fill in code here

        return meanRecall, Recalls


    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The fscore value as a number between 0 and 1
        """

        fscore = -1
        precision = self.queryPrecision(query_doc_IDs_ordered , query_id , true_doc_IDs, k)
        recall = self.queryRecall(query_doc_IDs_ordered , query_id , true_doc_IDs, k)
        #print("FSCORE",precision,recall)
        if(precision==0 and recall ==0):
            fscore = 0
        else:
            fscore = 2*(precision*recall)/(precision+recall)

        #Fill in code here

        return fscore
    
    
    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value
        
        Returns
        -------
        float
            The mean fscore value as a number between 0 and 1
        """
        Fscores = []
        meanFscore = -1
        total_Fscore = 0
        count = 0
        for i in query_ids:
            true_doc_IDs=[]
            flag=0
            for dic in qrels:
                if(int(dic["query_num"]) == i):
                    flag = 1
                    true_doc_IDs.append(int(dic["id"]))
                elif(flag == 1):
                    break
            #print("My print", doc_IDs_ordered[count], true_doc_IDs)
            temp = self.queryFscore(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            Fscores.append(temp)
            total_Fscore = total_Fscore + self.queryFscore(doc_IDs_ordered[count] , i , true_doc_IDs, k)
            count = count+1
            #break
        meanFscore = total_Fscore/count

        #Fill in code here

        return meanFscore, Fscores
    

    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query
        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The qrels list of dictionaries 
        arg4 : int
                The k value
        Returns
        -------
        float
                The nDCG value as a number between 0 and 1
        """
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        relevance_vals = {}
        relevant_docs = []
        DCGk = 0
        IDCGk = 0
        for dict_ in true_doc_IDs:
            #print(dict_)
            if int(dict_["query_num"]) == int(query_id):
                id_ = int(dict_["id"])
                relevance = 5-dict_["position"]
                relevant_docs.append(int(id_))
                relevance_vals[int(id_)] = relevance

        for i in range(1, k+1):
            docID = int(query_doc_IDs_ordered[i-1])
            if docID in relevant_docs:
                relevance = relevance_vals[docID]
                DCGk += (2**relevance-1)/log2(i+1)

        optimal_order = sorted(relevance_vals.values(), reverse=True)
        number_of_relevant_docs = len(optimal_order)
        for i in range(1, min(number_of_relevant_docs, k)+1):
            relevance = optimal_order[i-1]
            IDCGk += (2**relevance-1)/log2(i+1)

        nDCGk = DCGk/IDCGk
        return nDCGk
    
    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries
        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value
        Returns
        -------
        float
                The mean nDCG value as a number between 0 and 1
        """

        number_of_queries = len(query_ids)
        nDCGs = []
        
        for i in range(number_of_queries):
            query_doc_IDs_ordered = doc_IDs_ordered[i]
            query_id = int(query_ids[i])
            nDCG = self.queryNDCG(query_doc_IDs_ordered, query_id, qrels, k)
            nDCGs.append(nDCG)
        
        return sum(nDCGs)/len(nDCGs), nDCGs
    
    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)
        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of documents relevant to the query (ground truth)
        arg4 : int
                The k value
        Returns
        -------
        float
                The average precision value as a number between 0 and 1
        """
        number_of_true_docs = len(true_doc_IDs)
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        
        relevances = []
        precisions = []
        
        for docID in query_doc_IDs_ordered:
            if int(docID) in true_doc_IDs:
                relevances.append(1)
            else:
                relevances.append(0)
        for i in range(1, k+1):
            precision_at_i = self.queryPrecision(
                query_doc_IDs_ordered, query_id, true_doc_IDs, i)
            precisions.append(precision_at_i)

        precision_at_k_times_rel_k = []
        for i in range(k):
            value = precisions[i]*relevances[i]
            precision_at_k_times_rel_k.append(value)
            
        AveP = sum(precision_at_k_times_rel_k)/number_of_true_docs
        return AveP
    
    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries
        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value
        Returns
        -------
        float
                The MAP value as a number between 0 and 1
        """
        number_of_queries = len(query_ids)
        AvePs = []
        for i in range(number_of_queries):
            query_doc_IDs_ordered = doc_IDs_ordered[i]
            query_id = int(query_ids[i])
            true_doc_IDs = []
            for dict_ in qrels:
                if int(dict_["query_num"]) == int(query_id):
                    true_doc_IDs.append(int(dict_["id"]))
            AveP = self.queryAveragePrecision(
                query_doc_IDs_ordered, query_id, true_doc_IDs, k)
            AvePs.append(AveP)
            
        return sum(AvePs)/len(AvePs), AvePs
# In[ ]:




