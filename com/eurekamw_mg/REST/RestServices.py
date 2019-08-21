
from flask import Flask, jsonify, request, json

from com.eurekamw_mg.utils import SearchUtils as su, WordListUtils as wlu, CategoryUtils as cu
from com.eurekamw_mg.model import CategoryFile as cf
from com.eurekamw_mg.REST import RESTConstant as RC

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


@app.route('/category/create', methods=['POST'])
def create_category():
    if not (request.headers['Content-Type'] == 'application/json'):
        return RC.INVALID_CONTENT_TYPE

    payload = json.dumps(request.json)
    name=payload['name']
    list=wlu.generate_list(payload['list'])

    cat=cf.Category(name,list)
    is_successfull, result=cat.create()
    if not is_successfull:
        return RC.UNSUCCESSFUL_OPERATION
    return result

@app.route('/category/update', methods=['PUT'])
def update_category():
    if not (request.headers['Content-Type'] == 'application/json'):
        return RC.INVALID_CONTENT_TYPE

    payload = json.dumps(request.json)
    name=payload['name']
    list=wlu.generate_list(payload['list'])

    result=cu.update_category(name,list)
    if not result:
        return RC.UNSUCCESSFUL_OPERATION

    return result


if __name__ == '__main__':
    app.run(debug=True)
