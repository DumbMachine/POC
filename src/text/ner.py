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
from nltk import tokenize

from gensim import corpora, models

stopword_list = nltk.corpus.stopwords.words('english')

base_json = '../../data/poc_ner/Entity Recognition in Resumes.json'
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
small_df = resume_df.sample(10)
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
doc_list = [clean_text(text) for text in string_list if clean_text(text) is not None]

dictionary = corpora.Dictionary(doc_list)
corpus = [dictionary.doc2bow(doc) for doc in doc_list]
tfidf = models.TfidfModel(corpus, id2word = dictionary)

#filter low value words
low_value = 0.025

for i in range(0, len(corpus)):
    bow = corpus[i]
    low_value_words = [] #reinitialize to be safe. You can skip this.
    low_value_words = [id for id, value in tfidf[bow] if value < low_value]
    new_bow = [b for b in bow if b[0] not in low_value_words]

    #reassign
    corpus[i] = new_bow

def clean_text(text):
    # tokenization
    tokens = tokenize_word_text(text)
    tokens = convert_letters(tokens)

    # Remove spaces
    tokens = [token.strip() for token in tokens]
    tokens = remove_accent_after_tokens(tokens)
    tokens = rm_stopwords(tokens, stopword_list)
    return tokens

def tokenize_word_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.strip() for token in tokens]
    return tokens



"""
Converting all letters to lower or upper case (common : lower case)
"""
def convert_letters(tokens, style = "lower"):
    if (style == "lower"):
        tokens = [token.lower() for token in tokens]
    else :
        tokens = [token.upper() for token in tokens]
    return(tokens)

def remove_after_token(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text

def remove_accent_after_tokens(tokens):
    tokens = [unidecode.unidecode(token) for token in tokens]
    return(tokens)

def rm_stopwords(tokens, stopwords):
    return [w for w in tokens if w not in stopwords]