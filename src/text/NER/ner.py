import unidecode
import json
import nltk
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
from nltk import tokenize

from gensim import corpora, models
from utils import *
stopword_list = nltk.corpus.stopwords.words('english')

base_json = '../../../data/poc_ner/Entity Recognition in Resumes.json'
def pop_annot(raw_line):
    in_line = defaultdict(list, **raw_line)
    if 'annotation' in in_line:
        labels = in_line['annotation']
        for c_lab in labels:
            if len(c_lab['label'])>0:
                in_line[c_lab['label'][0]] += c_lab['points']
    return in_line
with open(base_json, 'r') as f:
    # data is jsonl and so we parse it line-by-line
    resume_data = [json.loads(f_line) for f_line in f.readlines()]
    resume_df = pd.DataFrame([pop_annot(line) for line in resume_data])
resume_df['length'] = resume_df['content'].map(len)

# Taking a small sample
small_df = resume_df.sample(20)
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
    for value in small_df[ner]:
        if isinstance(value, list):
            for smaller_value in value:
                NER_TYPES[ner].append(smaller_value['text'])

string_list = NER_TYPES['Skills']
string_list = [clean_text_kaggle(text) for text in string_list]
doc_list = [clean_text(text) for text in string_list if clean_text(text) is not None]
# doc_list = [clean_text_kaggle(text) for text in string_list if clean_text(text) is not None]

# dictionary = corpora.Dictionary(doc_list)
# corpus = [dictionary.doc2bow(doc) for doc in doc_list]
# tfidf = models.TfidfModel(corpus, id2word = dictionary)

# #filter low value words
# low_value = 0.025

# for i in range(0, len(corpus)):
#     bow = corpus[i]
#     low_value_words = [] #reinitialize to be safe. You can skip this.
#     low_value_words = [id for id, value in tfidf[bow] if value < low_value]
#     new_bow = [b for b in bow if b[0] not in low_value_words]

#     #reassign
#     corpus[i] = new_bow

"""
Sklearn
"""
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

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
# df.sort_values(by=["tfidf"],ascending=False)
df.sort_values(by=["tfidf"],ascending=False).index.values[:int(len(df)*0.1)]
"""
Bi-Gram TFIDF
"""

# Finding the most command the normal way

string_list = NER_TYPES['Skills']
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
df.sort_values(by=["tfidf"],ascending=False)[df.tfidf > 0]


# Fidning the most

# Taking a small sample
sample_amount = 10
small_df = resume_df.sample(sample_amount)
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
    for value in small_df[ner]:
        if isinstance(value, list):
            for smaller_value in value:
                NER_TYPES[ner].append(smaller_value['text'])


string_list = NER_TYPES['Skills']
string_list = [clean_text_kaggle(text) for text in string_list]
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
df.sort_values(by=["tfidf"],ascending=False)[df.tfidf > 0]




# Count overlap
sample_amount = 10
test_skills_df = resume_df.iloc[sample_amount:].Skills
test_skills = []
for skill in test_skills_df:
    if isinstance(skill, list):
        for smaller_skill in skill:
            test_skills.append(
                smaller_skill['text']
            )

# Will count the overlap of tokens, proceding sentence by sentence:
for candidate in test_skills:
    candidate_tokens = clean_text_kaggle(candidate)
    break