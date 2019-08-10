import traceback

from com.eurekamw_mg.db import DBConstant as DC, DBUtils as dbu
from com.eurekamw_mg.model import JSONCostants as JC
from com.eurekamw_mg.utils import SearchUtils as su


def add_categories(categories):
    full_result={}
    for category in categories:
        result = category.add_category()
        full_result[category.name] = result


def delete_category(category_name):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]
        category_coll = db[DC.CATEGORY_COLL]
        # words_coll = db[DC.WORDS_COLL]
        #
        # word_update_query = {}
        # word_update_query[JC.CATEGORY] = category_name
        #
        # new_values = {}
        # new_values[JC.CATEGORY] = ""
        #
        # set_query = {}
        # set_query[JC.SET] = new_values
        # words_coll.update_one(word_update_query,set_query)

        delete_query={}
        delete_query[JC.ID] = category_name

        category_coll.delete_one(delete_query)
    except:
        traceback.print_exc()
    finally:
        client.close()


def update_category_name(from_name,to_name):
    if not is_category_present(from_name):
        print("No category with name '{0}' is present in DB.".format(from_name))
        return False
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]
        category_coll = db[DC.CATEGORY_COLL]
        # words_coll = db[DC.WORDS_COLL]
        #
        # word_update_query = {}
        # word_update_query[JC.CATEGORY] = from_name
        #
        # new_values_for_words = {}
        # new_values_for_words[JC.CATEGORY] = to_name
        #
        # set_query = {}
        # set_query[JC.SET] = new_values_for_words
        # words_coll.update_many(word_update_query,set_query)

        category_update_query={}
        category_update_query[JC.ID] = from_name

        new_values_for_category = {}
        new_values_for_category[JC.ID] = to_name
        new_values_for_category[JC.NAME] = to_name

        set_query = {}
        set_query[JC.SET] = new_values_for_category

        category_coll.update_one(category_update_query,set_query)
    except:
        traceback.print_exc()
    finally:
        client.close()

def remove_words_from_category(category_name, word_list):
    if not is_category_present(category_name):
        print("No category with name '{0}' is present in DB.".format(category_name))
        return False

    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]
        category_coll = db[DC.CATEGORY_COLL]

        category_update_query={}
        category_update_query[JC.NAME] = category_name

        set_query = {}
        set_query[JC.PULL] = {JC.LIST: {JC.IN : word_list}}

        category_coll.update_one(category_update_query,set_query)
    except:
        traceback.print_exc()
    finally:
        client.close()

def add_words_to_category(category_name, word_list):
    if not is_category_present(category_name):
        print("No category with name '{0}' is present in DB.".format(category_name))
        return False
    try:
        in_valid_word_list=[]
        for word in word_list:
            is_valid = su.search(word)
            if not is_valid:
               in_valid_word_list.append(word)
               word_list.remove(word)

        if len(in_valid_word_list) > 0:
            print('Unable to find following words: {0}'.format(in_valid_word_list))

        client = dbu.get_client()

        db = client[DC.DB_NAME]
        category_coll = db[DC.CATEGORY_COLL]

        category_update_query={}
        category_update_query[JC.NAME] = category_name

        set_query = {}
        set_query[JC.PUSH] = {JC.LIST: {JC.EACH: word_list}}

        category_coll.update_one(category_update_query,set_query)
    except:
        traceback.print_exc()
    finally:
        client.close()

def is_category_present(category_name):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]
        category_coll = db[DC.CATEGORY_COLL]

        category_search_query={}
        category_search_query[JC.NAME] = category_name

        result = category_coll.count_documents(category_search_query)
        if result == 0:
            return False

        return True
    except:
        traceback.print_exc()
    finally:
        client.close()

def is_word_present(wordname):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        cat_coll = db[DC.CATEGORY_COLL]
        search_data = {}
        search_data[JC.LIST] = wordname
        if cat_coll.count_documents(search_data) == 0:
            return False
        return True
    except Exception as exception:
        traceback.print_exc()
        return False
    finally:
        client.close()


