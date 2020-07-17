# flask run --host=0.0.0.0 --port=8008

from flask import Flask, request, abort
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'To use this recommendation service, send a <strong>GET</strong> request to <strong>x.x.x.x:8008/fetch-related?category=YOUR-CATEGORY</strong>'

@app.route('/fetch-related')
def sample_endpoint(methods=['GET']):
    if request.method != 'GET':
        abort(400)

    res = json.loads('{}')
    res['message'] = 'Podcasts related to {}'.format(request.args['category'])
    podcasts = []
    # -- CALL CATEOGRIZATION ALGORITHM AND ADD ALL RELATED PODCASTS --
    # -- insert code here --
    res['podcasts'] = podcasts
    return res