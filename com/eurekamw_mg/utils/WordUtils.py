
import traceback

from com.eurekamw_mg.utils import SearchUtils as su
from com.eurekamw_mg.db import DBUtils as dbu, DBConstant as DC
from com.eurekamw_mg.model import JSONCostants as JC

def is_valid_word(wordname):
    word = su.search(wordname)
    if word is None:
        return False
    return True
#
# def update_category(wordname, category_name=''):
#     try:
#         client = dbu.get_client()
#
#         db = client[DC.DB_NAME]
#
#         words_schema = db[DC.WORDS_COLL]
#         search_query = {}
#         search_query[JC.ID] = wordname
#
#         new_values = {}
#         new_values[JC.CATEGORY] = category_name
#
#         set_query={}
#         set_query[JC.SET] = new_values
#         result = words_schema.update_one(search_query,set_query)
#         print(result.modified_count)
#         if result.modified_count is not 0:
#             return True
#         return False
#     except Exception as exception:
#         traceback.print_exc()
#         return False
#     finally:
#         client.close()

# print(update_category('charm','magical charms'))

def get_category_name(wordname):
    try:
        client = dbu.get_client()

        db = client[DC.DB_NAME]

        cat_coll = db[DC.CATEGORY_COLL]
        search_data = {}
        search_data[JC.LIST] = wordname
        if cat_coll.count_documents(search_data) == 0:
            return False, None
        result = cat_coll.find(search_data)
        return True, result[0]
    except Exception as exception:
        traceback.print_exc()
        return False, None
    finally:
        client.close()