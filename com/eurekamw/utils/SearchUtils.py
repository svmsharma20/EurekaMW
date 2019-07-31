
from com.eurekamw.utils.DBUtils import isPresentInDB

def search(name):
    if isPresentInDB(name):
        return True
    return False