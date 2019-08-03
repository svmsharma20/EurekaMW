"""
    Prerequisites :
        1. Install mongodb server. Use below link to install:
            https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
        2. Install pymongo library in python
"""
from com.eurekamw_mg.db import DBUtils as dbu


def __init__():
    dbu.initialize_db()

__init__()