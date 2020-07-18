# flask run --host=0.0.0.0 --port=8008

from flask import Flask, request, abort
import json
import sys, os

sys.path.append(os.path.abspath('./categorization'))
from categorization import Recommend
from interest_mapping import InterestConverter
converter = InterestConverter()
recommender = Recommend()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'To use this recommendation service, send a <strong>GET</strong> request to <strong>x.x.x.x:8008/fetch-related?category=YOUR-CATEGORY</strong>'

@app.route('/fetch-related')
def sample_endpoint(methods=['GET']):
    if request.method != 'GET':
        abort(400)

    # extract fields
    topic = request.args['category']

    # create response json
    res = json.loads('{}')
    res['message'] = topic

    # map topic to category
    category = converter.convert_topic_to_category(topic)
    print(category)

    # grab recommendations
    podcasts = recommender.recommend(category)
    
    res['podcasts'] = podcasts
    return res