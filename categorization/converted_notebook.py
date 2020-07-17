#cell 0
from pprint import pprint

#cell 1
### 0 - Load text file

#cell 2
podcast_list = ["TED_TALK_Daily", "Snack_Daily", "Joe_Rogan"]
paths = ["./TED_Talk_Daily.txt", "./snack_daily.txt", "./Joe_Rogan.txt"]
text_corpus = []
episode = []
for path in paths:
    with open(path) as f:
        line = f.readline()
        episode.append(line)
        while line:
            line = f.readline()
            episode.append(line)
    text_corpus.append(''.join(episode))
    episode = []
# pprint (text_corpus)

#cell 3
def split_and_append(bag_of_words, line):
    word_list = line.split(" ")
    for word in word_list:
        raw_word = '%r'%word
        if "\\" in raw_word:
            idx = raw_word.find("\\")
            word = raw_word[:idx]
        if len(word) == 0:
            continue
        bag_of_words.append(word)
    return bag_of_words

#cell 4
### 1 - Exclude all stopwords from the text file

#cell 5
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('english'))
stoplist = set(stopwords.words('english'))

#cell 6
### 2 - Top Frequent words

#cell 7
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in text_corpus]

#cell 8
# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

#cell 9
# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
pprint(processed_corpus)

#cell 10
from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

#cell 11
pprint(dictionary.token2id)

#cell 12
### 3 - TF-IDF modeling

#cell 13
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
pprint(bow_corpus)

#cell 14
from gensim import models

# train the model
tfidf = models.TfidfModel(bow_corpus)

# transform the "black lives matter" string
words = "black lives matter".lower().split()
print(tfidf[dictionary.doc2bow(words)])

#cell 15
from gensim import similarities

index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=len(dictionary.token2id))

#cell 16
### 4 - Categorize by inverted indexing

#cell 17
import json

with open('../json/keywords.json') as f:
    mapping = json.load(f)

#cell 18
genre_score_map = {}
genre_keyword = mapping['bucket_to_keyword']
for genre in genre_keyword:    
    query_bow = dictionary.doc2bow(genre_keyword[genre])
    sims = index[tfidf[query_bow]]
    # print(genre, ": ", list(enumerate(sims)))
    genre_score_map[genre] = list(sims)

#cell 19
import pandas as pd

#cell 21
df = pd.DataFrame(data = genre_score_map)
print (df.idxmax(axis=1))

#cell 22
for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)

#cell 23


