
import traceback

from com.eurekamw_mg.utils import SearchUtils as su
from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC
from com.eurekamw_mg.model import JSONCostants as JC

def add_words_to_list(list_name, word_list):
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
        list_coll = db[DC.LIST_COLL]

        list_update_query={}
        list_update_query[JC.NAME] = list_name

        set_query = {}
        set_query[JC.PUSH] = {JC.LIST: {JC.EACH: word_list}}

        list_coll.update_one(list_update_query,set_query)
    except:
        traceback.print_exc()
    finally:
        client.close()


def remove_words_from_category(list_name, word_list):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]
        list_coll = db[DC.LISTS_COLL]

        list_update_query={}
        list_update_query[JC.NAME] = list_name

        set_query = {}
        set_query[JC.PULL] = {JC.LIST: {JC.IN : word_list}}

        list_coll.update_one(list_update_query,set_query)
    except:
        traceback.print_exc()
    finally:
        client.close()
