from com.eurekamw.model.WordFile import Word
from com.eurekamw.utils import DBUtils as dbu


def test_insert_word():
    test_word  = Word('testword', 'testcategory', 'test stems', 'test shortdef', 'test xdef')
    dbu.insert_word(test_word)


def main_test_suite():
    test_insert_word()


main_test_suite()