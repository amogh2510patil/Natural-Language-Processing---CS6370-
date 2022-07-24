# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:38:01 2022

@author: Ritwiz
"""

import csv
import matplotlib.pyplot as plt

#PRECISION
with open('bm25_precision.csv', newline='') as f:
    reader = csv.reader(f)
    bm25_precision = list(reader)
    
for j in range(len(bm25_precision)):
    bm25_precision[j] = [float(i) for i in bm25_precision[j]]

with open('vsm_precision.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_precision = list(reader)
    
for j in range(len(vsm_precision)):
    vsm_precision[j] = [float(i) for i in vsm_precision[j]]

#RECALL
with open('bm25_recall.csv', newline='') as f:
    reader = csv.reader(f)
    bm25_recall = list(reader)
    
for j in range(len(bm25_recall)):
    bm25_recall[j] = [float(i) for i in bm25_recall[j]]

with open('vsm_recall.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_recall = list(reader)
    
for j in range(len(vsm_recall)):
    vsm_recall[j] = [float(i) for i in vsm_recall[j]]

#F-SCORE
with open('bm25_fscore.csv', newline='') as f:
    reader = csv.reader(f)
    bm25_fscore = list(reader)
    
for j in range(len(bm25_fscore)):
    bm25_fscore[j] = [float(i) for i in bm25_fscore[j]]

with open('vsm_fscore.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_fscore = list(reader)
    
for j in range(len(vsm_fscore)):
    vsm_fscore[j] = [float(i) for i in vsm_fscore[j]]

#MAP
with open('bm25_map.csv', newline='') as f:
    reader = csv.reader(f)
    bm25_map = list(reader)
    
for j in range(len(bm25_map)):
    bm25_map[j] = [float(i) for i in bm25_map[j]]

with open('vsm_map.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_map = list(reader)
    
for j in range(len(vsm_map)):
    vsm_map[j] = [float(i) for i in vsm_map[j]]

#NDCG
with open('bm25_ndcg.csv', newline='') as f:
    reader = csv.reader(f)
    bm25_ndcg = list(reader)
    
for j in range(len(bm25_ndcg)):
    bm25_ndcg[j] = [float(i) for i in bm25_ndcg[j]]

with open('vsm_ndcg.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_ndcg = list(reader)
    
for j in range(len(vsm_ndcg)):
    vsm_ndcg[j] = [float(i) for i in vsm_ndcg[j]]


bm25_precision = [sum(j)/len(j) for j in bm25_precision]
vsm_precision = [sum(j)/len(j) for j in vsm_precision]

bm25_recall = [sum(j)/len(j) for j in bm25_recall]
vsm_recall = [sum(j)/len(j) for j in vsm_recall]

bm25_fscore = [sum(j)/len(j) for j in bm25_fscore]
vsm_fscore = [sum(j)/len(j) for j in vsm_fscore]

bm25_map = [sum(j)/len(j) for j in bm25_map]
vsm_map = [sum(j)/len(j) for j in vsm_map]

bm25_ndcg = [sum(j)/len(j) for j in bm25_ndcg]
vsm_ndcg = [sum(j)/len(j) for j in vsm_ndcg]


print("BM25 vs VSM: Evaluation Metrics")
from scipy import stats
from statsmodels.stats import weightstats as stests

ttest_precision ,pval_precision = stats.ttest_rel(vsm_precision, bm25_precision, nan_policy='omit')
print("Precision: p =", pval_precision)

ttest_recall ,pval_recall = stats.ttest_rel(vsm_recall, bm25_recall, nan_policy='omit')
print("Recall: p =", pval_recall)

ttest_fscore ,pval_fscore = stats.ttest_rel(vsm_fscore, bm25_fscore, nan_policy='omit')
print("F score: p =", pval_fscore)

ttest_map ,pval_map = stats.ttest_rel(vsm_map, bm25_map, nan_policy='omit')
print("MAP: p =", pval_map)

ttest_ndcg ,pval_ndcg = stats.ttest_rel(vsm_ndcg, bm25_ndcg, nan_policy='omit')
print("NDCG: p =", pval_ndcg)

print("")
alpha = 0.09
print("Considering level of significance as 0.09 i.e. 90% confidence:")
if pval_precision < alpha:
    print("Precision: Reject Null Hypothesis.")
else:
    print("Precision: Fail to Reject Null Hypothesis.")
    
if pval_recall < alpha:
    print("Recall: Reject Null Hypothesis.")
else:
    print("Recall: Fail to Reject Null Hypothesis.")

if pval_fscore < alpha:
    print("F Score: Reject Null Hypothesis.")
else:
    print("F score: Fail to Reject Null Hypothesis.")

if pval_map < alpha:
    print("MAP: Reject Null Hypothesis.")
else:
    print("MAP: Fail to Reject Null Hypothesis.")

if pval_ndcg < alpha:
    print("NDCG: Reject Null Hypothesis.")
else:
    print("NDCG: Fail to Reject Null Hypothesis.")
    
    
#PLOTS
plt.plot(vsm_precision, label='VSM')
plt.plot(bm25_precision, label='BM25')
plt.legend()
plt.title('VSM vs BM25: Precision')
plt.show()

plt.plot(vsm_recall, label='VSM')
plt.plot(bm25_recall, label='BM25')
plt.legend()
plt.title('VSM vs BM25: Recall')
plt.show()

plt.plot(vsm_fscore, label='VSM')
plt.plot(bm25_fscore, label='BM25')
plt.legend()
plt.title('VSM vs BM25: Fscore')
plt.show()

plt.plot(vsm_map, label='VSM')
plt.plot(bm25_map, label='BM25')
plt.legend()
plt.title('VSM vs BM25: MAP')
plt.show()

plt.plot(vsm_ndcg, label='VSM')
plt.plot(bm25_ndcg, label='BM25')
plt.legend()
plt.title('VSM vs BM25: NDCG')
plt.show()
    
print("")
print("LSA vs VSM: Computation Time")

with open('LSA_time.csv', newline='') as f:
    reader = csv.reader(f)
    lsa_time = list(reader)
    
for j in range(len(lsa_time)):
    lsa_time[j] = [float(i) for i in lsa_time[j]]
    
lsa_time = [item for sublist in lsa_time for item in sublist]

with open('tfidf_time.csv', newline='') as f:
    reader = csv.reader(f)
    vsm_time = list(reader)
    
for j in range(len(vsm_time)):
    vsm_time[j] = [float(i) for i in vsm_time[j]]

vsm_time = [item for sublist in vsm_time for item in sublist]


ttest_time ,pval_time = stats.ttest_rel(vsm_time, lsa_time, nan_policy='omit')
print("LSA vs VSM Time: p =", pval_time)


if pval_time < alpha:
    print("LSA vs VSM Time: Reject Null Hypothesis.")
else:
    print("LSA vs VSM Time: Fail to Reject Null Hypothesis.")









