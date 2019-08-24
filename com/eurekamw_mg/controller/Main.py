
from flask import Flask, render_template, jsonify, request, redirect, url_for
from com.eurekamw_mg.utils import SearchUtils as su, CategoryUtils as cu, WordListUtils as wlu, WordUtils as wu
from com.eurekamw_mg.model import JSONCostants as JC, CategoryFile as cf
from com.eurekamw_mg.REST import RESTConstant as RC

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

@app.route('/category/add')
def add_view():
    return render_template('add.html', result={})

@app.route('/category/addcat')
def add_category():
    cat_name = request.args['listname'].strip().lower()
    liststr = request.args['list']

    result = {}
    result['name'] = cat_name
    result['list'] = liststr

    if len(cat_name)==0 or len(liststr)==0:
        result['error'] = RC.MISSING_DATA
        return render_template('add.html', result=result)

    if cu.is_category_present(cat_name):
        result['error'] = RC.CATEGORY_ALREADY_PRESENT
        return render_template('add.html',result=result)

    list=[]
    for word in liststr.split(','):
        list.append(word.strip().lower())

    validatelist = wu.validate_wordlist(list)
    if len(validatelist[JC.INVALID_LIST]) > 0:
        result['error']= ['Invalid words: {0}'.format(validatelist[JC.INVALID_LIST])]
        return render_template('add.html', result=result)

    c = cf.Category(cat_name,list)
    result = c.create()
    if result is None:
        result['error'] = RC.UNSUCCESSFUL_OPERATION
        return render_template('add.html', result=result)

    return redirect(url_for('category'))


@app.route('/test')
def test():
    result = wlu.get_compl_list("testlist")
    return render_template('test.html', test=result)

if __name__ == '__main__':
    app.run(debug = True)
