"""
    Search related utilities.
"""
import requests, traceback

from com.eurekamw_mg.model import AuthConstants as SC, JSONCostants as JC
from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC

# Fetch the word from merrian webster and also store it in local db
def get_word_from_mw(wordname):
    search_url = get_url(wordname)
    print(search_url)

    resp = requests.get(search_url)
    resp_data = resp.json()
    print(resp_data)
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

        words_schema = db[DC.WORDS_SCHEMA]

        words_schema.insert_one(word)
        return word
    except Exception as exception:
        traceback.print_exc()
    finally:
        client.close()

# Prepares URL for search
def get_url(word):
    searchURL = SC.URL.format(word,SC.KEY_DICTIONARY_1)
    return searchURL

def get_word_from_db(wordname):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        words_schema = db[DC.WORDS_SCHEMA]
        search_data = {}
        search_data[JC.STEMS] = wordname
        result = words_schema.find(search_data)
        return result[0]
    except Exception as exception:
        traceback.print_exc()
    finally:
        client.close()
