
from flask import Flask, jsonify, request, json

from com.eurekamw_mg.utils import SearchUtils as su, WordListUtils as wlu, CategoryUtils as cu

app = Flask(__name__)

@app.route('/search/<word_name>', methods=['GET'])
def get_word(word_name):
    result = su.search(word_name)
    if result is None:
        return jsonify('{}')
    res=jsonify(result)
    return res

# @app.route('/messages', methods=['POST'])
# def test_post():
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON Message: " + json.dumps(request.json)

@app.route('/list/search/<list_name>', methods=['GET'])
def get_list(list_name):
    result = wlu.get_compl_list(list_name)
    if result is None:
        return jsonify('{}')
    res=jsonify(result)
    return res

@app.route('/category/search/<cat_name>', methods=['GET'])
def get_category(cat_name):
    result = cu.get_category(cat_name)
    if result is None:
        return jsonify('{}')
    res=jsonify(result)
    return res



if __name__ == '__main__':
    app.run(debug=True)
