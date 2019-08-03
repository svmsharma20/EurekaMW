
from com.eurekamw_mg.model import UserFile as uf

def test_get_json():
    user = uf.User('administrator', 'Admin', 'password')
    print(user.get_json())

def run_test_suite():
    test_get_json()


run_test_suite()