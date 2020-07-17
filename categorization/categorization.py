from collections import Counter
import json
from nltk.corpus import stopwords
from collections import defaultdict
from gensim import corpora, models, similarities
import pandas as pd

JSON_FEATURES_PATH = "./json/keywords.json"
JSON_PODCAST_LIST = "./json/podcast_list.json"
keyword_to_bucket = {}

# Loads in the keywords.json file
# Populates the keyword_to_bucket global dictionary
# Each keyword from the JSON maps to its parent bucket
def load_features():
    with open(JSON_FEATURES_PATH) as f:
        json_read = json.load(f)
        mappings = json_read['bucket_to_keyword']

    for mapping in mappings:
        bucket = mapping['bucket']
        keywords = mapping['keywords']
        for word in keywords:
            keyword_to_bucket[word] = bucket


# Placeholder for now
# Reads in the transcript information for each podcast episode from podcast_list.json
# Performs td-idf and creates feature vectors for each podcast
def extract_feature_vector(transcript):
    pass


# Placeholder for now
# Takes a feature vector from extract_feature_vector() (for some particular podcast)
# Classifies the podcast as one of the buckets defined in keywords.json
def classify(feature_vector):
    pass


def recommend(topic):
    text_corpus = []
    with open(JSON_PODCAST_LIST) as f:
        json_read = json.load(f)
        podcasts = json_read['podcasts']
        for podcast in podcasts:
            text_corpus.append(podcast['transcript'])

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

    with open('../json/keywords.json') as f:
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
    print (df.idxmax(axis=1))




if __name__ == "__main__":
    # starter for getting top n occurring words
    # st = "coronavirus"
    # arr = st.split()
    # Counter = Counter(arr)
    # common = Counter.most_common()
    # print(common)
    recommend("Education")
