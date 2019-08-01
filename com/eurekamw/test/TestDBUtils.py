from com.eurekamw.model.WordFile import Word
from com.eurekamw.utils import DBUtils as dbu


def test_insert_word():
    test_word  = Word('testword', 'testcategory', 'test stems', 'test shortdef', 'test xdef')
    result = dbu.insert_word(test_word)
    if result is True:
        print("Word inserted in the db successfully")
    else:
        print("Problem in inserting the word")


def test_is_username_unique():
    test_username = 'administrator'
    result = dbu.is_username_unique(test_username)
    if result is True:
        print("Username is available")
    else:
        print("Username is not available")

def main_test_suite():
    test_insert_word()
    #test_is_username_unique()


main_test_suite()