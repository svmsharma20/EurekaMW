"""
    Word collection related utilities.
"""

import traceback

from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC
from com.eurekamw_mg.model import JSONCostants as JC
from com.eurekamw_mg.utils import SearchUtils as su

class WordList:
    def __init__(self, name, list):
        self.name = name
        self.description = ""
        self.list = list

    def __init__(self, name, description, list):
        self.name = name
        self.description = description
        self.list = list

    def create(self):
        try:
            in_valid_word_list = []
            for word in self.list:
                is_valid = su.search(word)
                if not is_valid:
                    in_valid_word_list.append(word)
                    self.list.remove(word)

            if len(in_valid_word_list) > 0:
                print('Unable to find following words: {0}'.format(in_valid_word_list))

            client = dbu.get_client()

            db = client[DC.DB_NAME]
            list_coll = db[DC.LISTS_COLL]

            list_create_query = {}
            list_create_query[JC.NAME] = self.name
            list_create_query[JC.DESCRIPTION] = self.description
            list_create_query[JC.LIST] = self.list

            list_coll.insert_one(list_create_query)
        except:
            traceback.print_exc()
        finally:
            client.close()


list=WordList('testlist','description.....',['abate','abash','bohemian','ggkggg','indifferent', 'impassive'])
list.create()