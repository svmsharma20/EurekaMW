
from com.eurekamw.utils import UserUtils as uutils

def search(name):
    if uutils.is_present_in_db(name):
        return True
    return False