import json
import random

JSON_BUCKET_TO_INTEREST_FILEPATH = './json/bucket_to_interest.json'

class InterestConverter:

    def __init__(self):
        self.interest_to_bucket = {}
        with open(JSON_BUCKET_TO_INTEREST_FILEPATH) as f:
            json_read = json.load(f)
            buckets = json_read['buckets']

        for bucket in buckets:
            category = bucket['category'].lower()
            for topic in bucket['interests']:
                self.interest_to_bucket[topic.lower()] = category

    def convert_topic_to_category(self, topic):
        topic = topic.lower()
        if topic not in self.interest_to_bucket:
            return self.interest_to_bucket[random.choice(list(self.interest_to_bucket))]
        return self.interest_to_bucket[topic]

