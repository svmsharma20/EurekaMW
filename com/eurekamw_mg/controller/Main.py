
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
    # print(catlist)
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
def add_catview():
    return render_template('add.html', result={})

@app.route('/category/addcat', methods=['POST'])
def add_category():
    cat_name = request.form['listname'].strip().lower()
    liststr = request.form['list']

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

@app.route('/category/update/<cat_name>')
def update_catview(cat_name):
    cat = cu.get_category(cat_name)
    catlist = cat[JC.LIST]
    catliststr=catlist[0]
    for word in catlist[1:]:
        catliststr += ', '+word
    result={}
    result['oldname'] = cat_name
    result['newname'] = cat_name
    result['list'] = catliststr
    return render_template('update.html', result=result)

@app.route('/category/updatecat', methods=['POST'])
def update_category():
    cat_name = request.form['listname'].strip().lower()
    liststr = request.form['list']

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

@app.route('/category/delete/<cat_name>')
def delete_cat(cat_name):
    cu.delete_category(cat_name)
    return redirect(url_for('category'))

@app.route('/list/delete/<list_name>')
def delete_list(list_name):
    wlu.delete_list(list_name)
    return redirect(url_for('lists'))

@app.route('/list/add')
def add_listview():
    return render_template('addlist.html', result={})

@app.route('/list/addlist', methods=['POST'])
def add_list():
    list_name = request.form['listname'].strip().lower()
    liststr = request.form['list']

    result = {}
    result['name'] = list_name
    result['list'] = liststr

    if len(list_name)==0 or len(liststr)==0:
        result['error'] = RC.MISSING_DATA
        return render_template('addlist.html', result=result)

    if wlu.is_list_present(list_name):
        result['error'] = RC.LIST_ALREADY_PRESENT
        return render_template('addlist.html',result=result)

    list=[]
    for word in liststr.split(','):
        list.append(word.strip().lower())

    validatelist = wu.validate_wordlist(list)
    if len(validatelist[JC.INVALID_LIST]) > 0:
        result['error']= ['Invalid words: {0}'.format(validatelist[JC.INVALID_LIST])]
        return render_template('addlist.html', result=result)

    result = wlu.create(list_name,validatelist[JC.VALID_LIST])
    if result is False:
        result['error'] = RC.UNSUCCESSFUL_OPERATION
        return render_template('addlist.html', result=result)

    return redirect(url_for('lists'))



@app.route('/test')
def test():
    result = wlu.get_compl_list("testlist")
    return render_template('test.html', test=result)

if __name__ == '__main__':
    app.run(debug = True)
