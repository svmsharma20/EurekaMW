"""
    Category collection related utilities.
"""

import traceback

from com.eurekamw_mg.utils import WordListUtils as wlu, WordUtils as wu, CategoryUtils as cu
from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC
from com.eurekamw_mg.model import JSONCostants as JC, ListConstants as LC


class Category:
    def __init__(self, name, list):
        self.name = str.lower(name)
        self.list = wlu.sanatize_List(list)

    def add_word(self):
        valid_wordlist = []
        invalid_wordlist = []
        for wordname in self.list:
            if cu.is_word_present(wordname):
                print("Word '{0}' is already present in some other category".format(wordname))
            is_valid_word = wu.is_valid_word(wordname)
            if is_valid_word:
                valid_wordlist.append(wordname)
            else:
                invalid_wordlist.append(wordname)

        self.list = valid_wordlist
        # self.add_category()
        result={}
        result[LC.VALID_LIST] = valid_wordlist
        result[LC.INVALID_LIST] = invalid_wordlist
        return result

    def create(self):
        result = self.add_word()
        try:
            client = dbu.get_client()

            db = client[DC.DB_NAME]

            category_coll = db[DC.CATEGORY_COLL]

            search_query = {}
            search_query[JC.NAME] = self.name

            category_data = {}
            # category_data[JC.ID] = self.name
            category_data[JC.NAME] = self.name
            category_data[JC.LIST] = self.list

            if category_coll.count_documents(search_query) == 0:
                category_coll.insert_one(category_data)
                return True, result

            category_coll.replace_one(search_query, category_data)
            return True, result
        except Exception as exception:
            traceback.print_exc()
            return False, result
        finally:
            client.close()
