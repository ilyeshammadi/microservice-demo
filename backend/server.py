from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


client = MongoClient('mongodb', 27017)

db = client.pymongo_test


@app.route('/')
def index():
    posts = db.posts
    post_data = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    result = posts.insert_one(post_data)
    print('One post: {0}'.format(result.inserted_id))

    return jsonify(str(result.inserted_id))

@app.route('/hello')
def hello():
    return 'world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)