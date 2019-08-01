
from com.eurekamw.utils.DBUtils import is_present_in_db

def search(name):
    if is_present_in_db(name):
        return True
    return False