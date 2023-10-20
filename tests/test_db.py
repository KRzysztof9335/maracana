import logging
# from typing import Any, Dict
# from pymongo import MongoClient
import sys
import lib.db


# CLIENT = lib.db.create_client()
# if not lib.db.is_client_alive(CLIENT):
#     logging.critical("Cannot run tests, client is not run")
#     sys.exit(1)



# =================================================================================================

def test_create_client_default():
    inst = lib.db.create_client()
    assert inst.HOST == "localhost"
    assert inst.PORT == 27017
    assert inst.options.server_selection_timeout == 0.001

# =================================================================================================

def test_create_db_non_existing():
    client = lib.db.create_client()
    db_to_test = "my_test_db"
    client.drop_database(db_to_test)
    assert db_to_test not in client.list_database_names()


# db = client['mydb']
# print("Database created........")

# #Verification
# print("List of databases after creating new one")
# print(client.list_database_names())