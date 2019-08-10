
from flask import Flask, jsonify, request, json

from com.eurekamw_mg.utils import SearchUtils as su

app = Flask(__name__)

@app.route('/search/<word_name>', methods=['GET'])
def get_word(word_name):
    result = su.search(word_name)
    if result is None:
        return jsonify('{}')
    res=jsonify(result)
    # res['name']=result['_id']
    # res['shortdef']=result['shortdef']
    return res

# @app.route('/messages', methods=['POST'])
# def test_post():
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON Message: " + json.dumps(request.json)

if __name__ == '__main__':
    app.run(debug=True)
