import traceback

from com.eurekamw_mg.utils import WordListUtils as wu
from com.eurekamw_mg.db import DBConstant as DC, DBUtils as dbu
from com.eurekamw_mg.model import JSONCostants as JC, QueryConstants as QC

def export_list(listname):
    try:
        word_list = wu.get_list(listname)
        # for word in self.list:
        #     is_valid = su.search(word)
        #     if not is_valid:
        #         in_valid_word_list.append(word)
        #         self.list.remove(word)
        #
        # if len(in_valid_word_list) > 0:
        #     print('Unable to find following words: {0}'.format(in_valid_word_list))

        client = dbu.get_client()

        db = client[DC.DB_NAME]
        words_coll = db[DC.WORDS_COLL]

        list_search_query = {}
        list_search_query[JC.ID] = {JC.IN: word_list}
        result = words_coll.find(list_search_query)
        for words in result:
            print(words['shortdef'])
    except:
        traceback.print_exc()
    finally:
        client.close()

export_list('testlist')