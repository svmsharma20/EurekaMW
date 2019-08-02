
import mysql.connector

from com.eurekamw.utils import DBUtils as dbu, SQLQueries as sqlq

def generate_list(words):

    # Create a list from the input by splitting based on comma and trimming the whitespaces
    wordList = [word.strip().lower() for word in words.split(',')]
    #return the wordlist
    return wordList


def insert_word(word):
    try:
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
            return False

        cursor = connection.cursor()
        values = (name, category, stems, shortdef, xdef)
        cursor.execute(sqlq.INSERT_WORD,values)
        connection.commit()
        return True
    except mysql.connector.Error as error:
        print('Failed to get record from database: {}'.format(error))
        return False
    finally:
        # Closing database connection
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            #print('MySQL connection is closed')


def is_word_present_in_DB(word):
    try:
        connection = dbu.get_connection()
        if connection is None:
            print("Unable to get mysql db object")
            return False

        cursor = connection.cursor()

        return True

    except mysql.connector.Error as error:
        print('Failed to get record from database:{}'.format(error))
        return False

    finally:
        # Closing database connection
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            # print('MySQL connection is closed')
