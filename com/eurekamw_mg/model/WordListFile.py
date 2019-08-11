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

# list=WordList('testlist','description.....',['abate','abash','bohemian','ggkggg','indifferent', 'impassive'])
# list.create()