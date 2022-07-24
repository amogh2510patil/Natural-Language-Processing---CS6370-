from util import *

# Add your import statements here

from math import *



class Evaluation():
	def __init__(self):
		self.qrels = None

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

		precision = -1

		top_k_IDs = query_doc_IDs_ordered[:k]
		top_k_matches = 0

		for i in top_k_IDs:
			if i in true_doc_IDs:
				top_k_matches+=1

		#precision - first k
		precision = top_k_matches / k
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

		meanPrecision = -1
		
		tot = 0
		qrel_dict = {}
		for qrel in qrels:
			if int(qrel["query_num"]) not in qrel_dict.keys():
				qrel_dict[int(qrel["query_num"])] = [int(qrel["id"])] 
			else:
				qrel_dict[int(qrel["query_num"])].append(int(qrel["id"]))

		for q_id,d_id in zip(query_ids,doc_IDs_ordered):
			q_id = int(q_id)
			id_true = qrel_dict[q_id]
			id_pred = [int(ele) for ele in d_id]
			query_precision = self.queryPrecision(id_pred,q_id,id_true,k)
			tot += query_precision
		#Mean precision
		meanPrecision = tot / len(query_ids)
		
		return meanPrecision

	
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

		recall = -1

		top_k_IDs = query_doc_IDs_ordered[:k]
		top_k_matches = 0

		for i in top_k_IDs:
			if i in true_doc_IDs:
				top_k_matches+=1

		total_matches = len(true_doc_IDs)
		#Query recall 
		recall = top_k_matches / total_matches

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

		meanRecall = -1

		tot = 0
		
		qrel_dict = {}
		for qrel in qrels:
			if int(qrel["query_num"]) not in qrel_dict.keys():
				qrel_dict[int(qrel["query_num"])] = [int(qrel["id"])] 
			else:
				qrel_dict[int(qrel["query_num"])].append(int(qrel["id"]))

		for q_id,d_id in zip(query_ids,doc_IDs_ordered):
			q_id = int(q_id)
			id_true = qrel_dict[q_id]
			id_pred = [int(ele) for ele in d_id]
			query_precision = self.queryRecall(id_pred,q_id,id_true,k)
			tot += query_precision
		meanRecall = tot / len(query_ids)

		return meanRecall


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

		p = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		r = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		# f score just takes the harmonic mean of the precision and the 
		# recall which we calculate using the above functions
		try:
			fscore = 2*p*r/(p+r)
		except:
			fscore = 0

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

		meanFscore = -1

		tot = 0
		qrel_dict = {}
		for qrel in qrels:
			if int(qrel["query_num"]) not in qrel_dict.keys():
				qrel_dict[int(qrel["query_num"])] = [int(qrel["id"])] 
			else:
				qrel_dict[int(qrel["query_num"])].append(int(qrel["id"]))

		for q_id,d_id in zip(query_ids,doc_IDs_ordered):
			q_id = int(q_id)
			id_true = qrel_dict[q_id]
			id_pred = [int(ele) for ele in d_id]
			F_score = self.queryFscore(id_pred,q_id,id_true,k)
			tot += F_score
		meanFscore = tot / len(query_ids)

		return meanFscore
	

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
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		rel_vals = {}
		rel_docs = []
		DCGk = 0
		IDCGk = 0
		
		# the nDCG uses a relevance metric, we use 5 - (rank) values that are provided in the qrels file.
		
		for ID in true_doc_IDs:
			if int(ID["query_num"]) == int(query_id):
				id = int(ID["id"])
				rel = 5-ID["position"]
				rel_docs.append(int(id))
				rel_vals[int(id)] = rel	

		# we use relevance/log2(i+1)
		# since we start i from 1, we need not add another +1 to it
		# for more details see the report for this part

		for i in range(1, k+1):
			docID = int(query_doc_IDs_ordered[i-1])
			if docID in rel_docs:
				rel = rel_vals[docID]
				DCGk += (rel)/log2(i+1)

		order = sorted(rel_vals.values(), reverse=True)
		for i in range(1, min(len(order), k)+1):
			rel = order[i-1]
			IDCGk += (rel)/log2(i+1)

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

		nDCGs = []
		for i in range(len(query_ids)):
			query_doc_IDs_ordered = doc_IDs_ordered[i]
			query_id = int(query_ids[i])
			nDCG = self.queryNDCG(
				query_doc_IDs_ordered, query_id, qrels, k)
			nDCGs.append(nDCG)
		return sum(nDCGs)/len(nDCGs)
				
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

		# value of the precision is added if the document is relevant, else it isn't
		# then this sum is divided by the number of relevant documents
		# see the report for more information on this function

		cnt = 0
		prec = 0
		for i in range(k):
			if query_doc_IDs_ordered[i] in true_doc_IDs:
				cnt += 1
				prec += cnt/(i+1)
		if cnt == 0:
			return 0
		else:
			return prec / cnt

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

		meanAveragePrecision = -1

		tot = 0
		qrel_dict = {}
		for qrel in qrels:
			if int(qrel["query_num"]) not in qrel_dict.keys():
				qrel_dict[int(qrel["query_num"])] = [int(qrel["id"])] 
			else:
				qrel_dict[int(qrel["query_num"])].append(int(qrel["id"]))

		for q_id,d_id in zip(query_ids,doc_IDs_ordered):
			q_id = int(q_id)
			id_true = qrel_dict[q_id]
			id_pred = [int(ele) for ele in d_id]
			query_precision = self.queryAveragePrecision(id_pred,q_id,id_true,k)
			tot += query_precision
		meanAveragePrecision = tot / len(query_ids)

		return meanAveragePrecision