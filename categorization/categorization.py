from collections import Counter
import json
from nltk.corpus import stopwords
from collections import defaultdict
from gensim import corpora, models, similarities
import pandas as pd

JSON_FEATURES_PATH = "./json/keywords.json"
JSON_PODCAST_LIST = "./json/podcast_list.json"
keyword_to_bucket = {}

class Recommend:
    def __init__(self):
        with open(JSON_PODCAST_LIST) as f:
            self.data = {}
            podcasts_list = json.load(f)['podcasts']
            for podcast in podcasts_list:
                del podcast['transcript']
                self.data['{} - {}'.format(podcast['show'], podcast['episode'])] = podcast

    # Loads in the keywords.json file
    # Populates the keyword_to_bucket global dictionary
    # Each keyword from the JSON maps to its parent bucket
    def load_features(self):
        with open(JSON_FEATURES_PATH) as f:
            json_read = json.load(f)
            mappings = json_read['bucket_to_keyword']

        for mapping in mappings:
            bucket = mapping['bucket']
            keywords = mapping['keywords']
            for word in keywords:
                keyword_to_bucket[word] = bucket

    def recommend(self, topic):
        text_corpus = []
        podcast_list = []
        with open(JSON_PODCAST_LIST) as f:
            json_read = json.load(f)
            podcasts = json_read['podcasts']
            for podcast in podcasts:
                text_corpus.append(podcast['transcript'])
                podcast_list.append(podcast['show'] + " - " + podcast['episode'])

        stoplist = set(stopwords.words('english'))
        texts = [[word for word in document.lower().split() if word not in stoplist] for document in text_corpus]

        # Lowercase each document, split it by white space and filter out stopwords
        frequency = defaultdict(int)
        for text in texts:
            for token in text:
                frequency[token] += 1

        # Only keep words that appear more than once
        processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
        dictionary = corpora.Dictionary(processed_corpus)
        bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

        # train the model
        tfidf = models.TfidfModel(bow_corpus)

        index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=len(dictionary.token2id))

        with open(JSON_FEATURES_PATH) as f:
            mapping = json.load(f)

        genre_score_map = {}
        genre_keyword = mapping['bucket_to_keyword']

        genre_score_map = {}
        genre_keyword = mapping['bucket_to_keyword']
        for genre in genre_keyword:
            query_bow = dictionary.doc2bow(genre_keyword[genre])
            sims = index[tfidf[query_bow]]
            genre_score_map[genre] = list(sims)

        df = pd.DataFrame(data = genre_score_map)
        categories = df.idxmax(axis=1)
        podcast_index = categories[categories == topic].index.tolist()
        
        return [self.data[podcast_list[i]] for i in podcast_index]

