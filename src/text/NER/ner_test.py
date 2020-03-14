import json
import os
import re
import string
from collections import Counter, defaultdict
from glob import glob
from subprocess import check_output

import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import unidecode
from gensim import corpora, models
from nltk import tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

from utils import *

stopword_list = nltk.corpus.stopwords.words('english')


# Loading the dataset
dataset = load_resume_ner_data()

# Setting a sample to learn the data from it
# Taking a small sample
SAMPLE_DATA = 30
small_df = dataset.sample(SAMPLE_DATA)
NER_TYPES = {
    "College Name": [],
    "Degree": [],
    "Graduation Year": [],
    "Years of Experience": [],
    "Companies worked at": [],
    "Designation": [],
    "Skills": [],
    "Location": [],
    "Email Address": []
}

for ner in NER_TYPES.keys():
    temp_data = []
    for value in small_df[ner]:
        if isinstance(value, list):
            for smaller_value in value:
                temp_data.append(smaller_value['text'])

    # Will make the dict for that NER data now
    # string_list = [clean_text_kaggle(text) for text in temp_data]
    string_list = [" ".join(clean_text(text)) for text in temp_data]
    docs = string_list
    cv=CountVectorizer(ngram_range=(1,3))
    word_count_vector=cv.fit_transform(docs)
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(word_count_vector)
    df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
    df_idf.sort_values(by=['idf_weights'])
    count_vector=cv.transform(docs)
    tf_idf_vector=tfidf_transformer.transform(count_vector)
    feature_names = cv.get_feature_names()
    first_document_vector=tf_idf_vector[0]
    df = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["tfidf"])
    NER_TYPES[ner].extend(df.sort_values(by=["tfidf"],ascending=False)[df.tfidf > 0].index.values.tolist())


#  Testing with the above sample
history = []
test = dataset.iloc[SAMPLE_DATA:]
total_help = 0
total_matches = []
for candidate in test.values:
    local_help = 0
    matches = []
    tokens = candidate[0].split()
    for ner in NER_TYPES.keys():
        intersection = set(tokens).intersection(NER_TYPES[ner])
        if intersection:
            local_help += len(intersection)
            matches.append([ner, intersection])
    if local_help:
        total_help+=local_help
        total_matches+=matches