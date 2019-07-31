"""
    Prerequisites :
        1. Install mysql server. Use following command to install:
            sudo apt-get install mysql-server
        2. Install mysql-connector library in python

    Note:- Please create 'eureka' user before running this file. Use following commands to create the user and grant all the privileges to it.
            1. CREATE USER 'eureka' IDENTIFIED BY 'eurek@';
            2. CREATE DATABASE eureka;
            3. GRANT ALL PRIVILEGES ON eureka.* TO eureka;

    Use following command to check whether user is created or not
        select USER FROM mysql.user;

"""
import mysql.connector
from com.eurekamw.utils import DBConstants as DC, DBUtils as dbu

dbQueries = 'SHOW DATABASES'

sqlQueries = ('CREATE TABLE users (username VARCHAR(255), name VARCHAR(255), password VARCHAR(255), PRIMARY KEY(username))',
              'CREATE TABLE list (username VARCHAR(255), listname VARCHAR(255), description TEXT, wordlist TEXT, PRIMARY KEY(username, listname))',
              'CREATE TABLE words (word VARCHAR(255), category VARCHAR(255), shortdef TEXT, xdef TEXT PRIMARY KEY(word))')

def createSchema():
    # mydb = mysql.connector.connect(host=DC.HOSTNAME, user=DC.DB_USERNAME, passwd=DC.DB_PASSWORD)
    #
    # if mydb==None :
    #     print("Unable to get mysql db object")
    #     return
    #
    # mycursor = mydb.cursor()
    #
    # # Initialize database and schema
    # for query in dbQueries:
    #     print("Executing: %1s" %(dbQueries))
    #     mycursor.execute(dbQueries)
    #     for x in mycursor:
    #         print(x)
    #
    # mycursor.close()
    # mydb.close()

    mycursor = dbu.getConnection().cursor()

    for query in sqlQueries:
        print("Executing: %1s" %(query))
        mycursor.execute(query)

    # Insert raw data
    sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
    val = ("administrator", "Admin", "password")
    mycursor.execute(sql, val)

    mycursor.close()

def __init__():
    createSchema()

__init__()