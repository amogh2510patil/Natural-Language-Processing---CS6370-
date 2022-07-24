import json
from sentenceSegmentation import SentenceSegmentation
from tokenization import Tokenization
from inflectionReduction import InflectionReduction
from stopwordRemoval import StopwordRemoval
from Wikipedia_extract import main

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
        reducedDoc = InflectionReduction().reduce(doc,1)
        reducedDocs.append(reducedDoc)
    # Remove stopwords from docs
    stopwordRemovedDocs = []
    for doc in reducedDocs:
        stopwordRemovedDoc = StopwordRemoval().fromList(doc)
        stopwordRemovedDocs.append(stopwordRemovedDoc)

    preprocessedDocs = stopwordRemovedDocs
    return preprocessedDocs


docs_json = json.load(open("cranfield/" + "cran_docs.json", 'r'))[:]
doc_ids, docs = [item["id"] for item in docs_json], \
                    [item["title"] for item in docs_json]
# Process documents
processedDocs = preprocess(docs)

#Create_corpus
unique_terms = {term for doc in processedDocs for sentence in doc for term in sentence}
for word in unique_terms:
    if len(word) <=3 :
        continue
    print(word)
    main(word,1,"corpus")
