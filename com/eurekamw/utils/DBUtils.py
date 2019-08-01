from operator import is_not

import mysql.connector
from com.eurekamw.utils import DBConstants as DC, DBUtils as dbu, SQLQueries as sqlq


def get_connection():
    return mysql.connector.connect(host=DC.HOSTNAME, user=DC.DB_USERNAME, passwd=DC.DB_PASSWORD, database=DC.DB_NAME)


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
            print('MySQL connection is closed')


def add_user(user):
    username = user.username

    if not dbu.is_username_unique(username):
        print("Username is not available")
        return False

    try:
        name = user.name
        password = user.password

        connection = dbu.get_connection()
        if connection is None:
            print("Unable to get mysql db object")
            return False

        cursor = connection.cursor()
        values = (username, name, password)
        cursor.execute(sqlq.INSERT_USER,values)
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
            print('MySQL connection is closed')


def is_username_unique(username):
    try:
        connection = dbu.get_connection()
        if connection is None:
            print("Unable to get mysql db object")
            return False

        cursor = connection.cursor()
        cursor.execute(sqlq.GET_USER.format(username))
        record = cursor.fetchall()

        if len(record) > 0:
            return False
        return True
    except mysql.connector.Error as error:
        print('Failed to get record from database: {}'.format(error))

    finally:
        # Closing database connection
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
