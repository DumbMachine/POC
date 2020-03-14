from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from utils import *

dataset = load_conll_ner_data()
NER_TYPES = {
    'B-MISC': [],
    'B-PER': [],
    'B-ORG': [],
    'B-LOC': [],
    'I-LOC': [],
    'I-PER': [],
    'I-MISC': [],
    'I-ORG': [],
    'O': [],
}

SAMPLE_DATA = .30
small_df = dataset.iloc[:int(len(dataset)*SAMPLE_DATA)]


for ner in NER_TYPES.keys():
    temp_data = []
    for value in small_df[ner]:
        if isinstance(value, list):
            for smaller_value in value:
                temp_data.append(smaller_value)
    # Will make the dict for that NER data now
    docs = [clean_text_kaggle(text) for text in temp_data]
    # string_list = [" ".join(clean_text(text)) for text in temp_data]
    cv=CountVectorizer()
    word_count_vector=cv.fit_transform(docs)
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(word_count_vector)
    df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
    NER_TYPES[ner].extend(df_idf.sort_values(by=["idf_weights"],ascending=False)[df_idf.idf_weights > 0].index.values.tolist())

#  Testing with the above sample
history = []
test = dataset.iloc[int(len(dataset)*SAMPLE_DATA):]
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

print(total_help)



