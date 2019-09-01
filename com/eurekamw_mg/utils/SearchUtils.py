"""
    Search related utilities.
"""
import requests, traceback

from com.eurekamw_mg.model import AuthConstants as SC, JSONCostants as JC
from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC

# Fetch the word from merrian webster and also store it in local db
def get_word_from_mw(wordname):
    print('Fetching word {0} from MW db.'.format(wordname))
    search_url = get_url(wordname)

    resp = requests.get(search_url)
    resp_data = resp.json()
    if len(resp_data) is not 0:
        if JC.META not in resp_data[0]:
            return None
    else:
        return None

    word = resp.json()[0]
    word[JC.ID] = wordname

    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        words_schema = db[DC.WORDS_COLL]

        words_schema.insert_one(word)
        return word
    except Exception as exception:
        traceback.print_exc()
        return None
    finally:
        client.close()

# Prepares URL for search
def get_url(word):
    searchURL = SC.KEY_INTERMEDIATE_URL.format(word, SC.KEY_INTERMEDIATE_1)
    return searchURL

def get_word_from_db(wordname):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        words_schema = db[DC.WORDS_COLL]
        search_data = {}
        search_data[JC.STEMS] = wordname
        if words_schema.count_documents(search_data) == 0:
            return False, None
        result = words_schema.find(search_data)
        return True, result[0]
    except Exception as exception:
        traceback.print_exc()
        return False, None
    finally:
        client.close()


def search(wordname):
    is_word_present_in_db, word = get_word_from_db(wordname)
    if is_word_present_in_db:
        print('Word: {0} found in the local db'.format(wordname))
        return word
    return get_word_from_mw(wordname)

def get_selected_word_from_db(wordname,filter=""):
    if filter == None or len(filter) == 0:
        return get_word_from_db(wordname)

    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        words_schema = db[DC.WORDS_COLL]
        search_data = {}
        search_data[JC.STEMS] = wordname

        filter_query={}
        filter_query[JC.ID] = 0
        for field in filter:
            filter_query[field]=1

        if words_schema.count_documents(search_data) == 0:
            return None
        result = words_schema.find(search_data,filter_query)
        return result[0]
    except Exception as exception:
        traceback.print_exc()
        return  None
    finally:
        client.close()


def is_word_present_in_mw(wordname):
    search_url = get_url(wordname)

    resp = requests.get(search_url)
    resp_data = resp.json()
    if len(resp_data) is not 0:
        if JC.META in resp_data[0]:
            return True
    return False