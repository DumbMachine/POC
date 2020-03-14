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
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from utils import *

stopword_list = nltk.corpus.stopwords.words('english')






# Loading data related stuff
def load_conll_ner_data():
    base_txt = "../../../data/poc_ner/conll2.txt"
    with open(base_txt, 'r') as file:
        content = file.read()
    sentences = content.split(". . O O\n\n")
    DATASET = []
    for sentence in sentences:
        header = {
            "sentence": "",
            "O": [],
            "B-PER": [],
            "B-ORG": [],
            "B-MISC": [],
            "B-LOC": [],

            "I-LOC": [],
            "I-PER": [],
            "I-MISC": [],
            "I-ORG": [],
        }
        for line in sentence.split("\n"):
            if line:
                word, something, somethingelse, tag = line.split(" ")
                header["sentence"]+= f" {word}"
                header[tag].append(word)
        DATASET.append(header)

    return pd.DataFrame(DATASET)

def load_resume_ner_data():
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
    return resume_df

def tfidf_model(string_list, ngram_range=(1,3), thrshold=0.1):
    docs = string_list
    cv=CountVectorizer(ngram_range)
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

    # Returning the top threshold percentage
    return df.sort_values(by=["tfidf"],ascending=False).index.values[:int(len(df)*thrshold)]

# TODO: Remove special symbols
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

# Preprocessing
def remove_string_special_characters(s):

    # removes special characters with ' '
    stripped = re.sub('[^a-zA-z\s]', '', s)
    stripped = re.sub('_', '', stripped)

    # Change any white space to one space
    stripped = re.sub('\s+', ' ', stripped)

    # Remove start and end white spaces
    stripped = stripped.strip()
    if stripped != '':
            return

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



def clean_text_kaggle(text):
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    # text = stem_words(text)
    # text = lemmatize_words(text)
    return text



STOPWORDS = set(stopwords.words('english'))
PUNCT_TO_REMOVE = string.punctuation

def remove_punctuation(text):
    """custom function to remove the punctuation"""
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def stem_words(text, stemmer=None):
    if stemmer is None:
        stemmer = PorterStemmer()
    return " ".join([stemmer.stem(word) for word in text.split()])

def lemmatize_words(text, lemmatizer=None):
    if lemmatizer is None:
        lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

# Reference : https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def remove_emoticons(text):
    emoticon_pattern = re.compile(u'(' + u'|'.join(k for k in EMOTICONS) + u')')
    return emoticon_pattern.sub(r'', text)

def convert_emoticons(text):
    for emot in EMOTICONS:
        text = re.sub(u'('+emot+')', "_".join(EMOTICONS[emot].replace(",","").split()), text)
    return text

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)
