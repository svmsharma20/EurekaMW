
import mysql.connector
from com.eurekamw.utils import DBConstants as DC, DBUtils as dbu, SQLQueries as sqlq


def is_present_in_db(name):
    return False

def get_connection():
        return mysql.connector.connect(host=DC.HOSTNAME,
                                       user=DC.DB_USERNAME,
                                       passwd=DC.DB_PASSWORD,
                                       database=DC.DB_NAME)


def insert_word(word):
    name = word.name
    xdef = word.xdef

    if name is None or xdef is None:
        print("Invalid word: name/xdef cannot be None")
        return

    category = word.category
    shortdef = word.shortdef
    stems = word.stems

    connection = dbu.get_connection()
    if connection is None:
        print("Unable to get mysql db object")
        return

    cursor = connection.cursor()
    values = (name, category, stems, shortdef, xdef)
    cursor.execute(sqlq.INSERT_WORD,values)
    connection.commit()

    cursor.close()
    connection.close()