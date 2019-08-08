"""
    Db related utilities.
"""
import traceback

from pymongo import MongoClient, errors
from com.eurekamw_mg.db import DBConstant as DC
from com.eurekamw_mg.model import UserFile as uf, JSONCostants as JC

def get_client():
    hostname = DC.HOSTNAME
    port = DC.PORT
    client = MongoClient(hostname, port)
    if client is None:
        raise Exception('Unable to get mongodb client got server: {0}; port:{1}'.format(hostname,port))
        return None
    return client


#   Initialize the db to create eureka database and users collection. Also add an admin user in it.
def initialize_db():
    try:
        client = get_client()

        db = client[DC.DB_NAME]

        user_schema = db[DC.USER_COLL]
        admin_user = uf.User('administrator', 'Admin', 'password')
        if is_id_present(admin_user.loginid):
            print("Login Id is not available")
            return False

        result = user_schema.insert_one(admin_user.get_dict())
        print('Adding admin user: {0}'.format(result.inserted_id))
        return True
    except Exception as exception:
        traceback.print_exc()
    finally:
        client.close()


def is_id_present(loginid):
    try:
        client = get_client()

        db = client[DC.DB_NAME]

        user_schema = db[DC.USER_COLL]
        user={}
        user[JC.ID] = loginid
        results = user_schema.find(user)
        count = results.count()

        if count > 0:
            return True
        return False
    except Exception as exception:
        traceback.print_exc()
    finally:
        client.close()

