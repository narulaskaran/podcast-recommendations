from collections import Counter
import json

JSON_FEATURES_PATH = "./json/keywords.json"
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


if __name__ == "__main__":
    # starter for getting top n occurring words
    st = "coronavirus"
    arr = st.split()
    Counter = Counter(arr)
    common = Counter.most_common()
    print(common)