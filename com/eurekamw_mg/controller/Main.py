
from flask import Flask, render_template, jsonify, request
from com.eurekamw_mg.utils import SearchUtils as su, CategoryUtils as cu, WordListUtils as wlu
from com.eurekamw_mg.model import JSONCostants as JC
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/word', methods=['GET'])
def word():
    word_name=request.args['name'].strip().lower()
    result = su.search(word_name)
    if result is None:
        return jsonify('{}')

    res = jsonify(result)
    # print(result)  #40,43,52
    return render_template('word.html', res=result)

@app.route('/category')
def category():
    list=cu.get_category_names()
    return render_template('category.html', list=list)

@app.route('/xcategory/<cat_name>')
def xcategory(cat_name):
    catlist = cu.get_compl_list(cat_name)
    print(catlist)
    return render_template('xcategory.html', list=catlist, name=cat_name)

@app.route('/lists')
def lists():
    list=wlu.get_lists()
    return render_template('lists.html', list=list)

@app.route('/xlists/<list_name>')
def xlists(list_name):
    result=wlu.get_compl_list(list_name)
    name=result[JC.NAME]
    list=result[JC.LIST]
    res=(name,list)
    return render_template('xlists.html', result=result)

@app.route('/list/update')
def updatelist():
    return render_template('updatelist.html')

@app.route('/test')
def test():
    result = wlu.get_compl_list("testlist")
    return render_template('test.html', test=result)

if __name__ == '__main__':
    app.run(debug = True)
