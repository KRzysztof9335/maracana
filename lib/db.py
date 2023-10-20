"""This module is responsible for database interaction"""
import logging
from pymongo import MongoClient
# from datetime import datetime
from typing import Any, Dict, List

from .models import Match

HOST = "localhost"
PORT = 27017
DB_NAME = "MyDataBase"
COLLECTION = "Fixtures"


def is_client_alive(client: MongoClient[Dict[str, Any]]) -> bool:
    timeout_prev = client.options.server_selection_timeout
    client.options.server_selection_timeout = 0.005  # type: ignore
    try:
        client.server_info()
        return True
    except:
        logging.error(f"Pymongo client {client.address} is not alive")
        return False
    finally:
        client.options.server_selection_timeout = timeout_prev  # type: ignore


def create_client(host: str = HOST, port: int = PORT, timeout: int = 1) -> MongoClient[Dict[str, Any]]:
    return MongoClient(host, port, serverSelectionTimeoutMS=timeout)


def create_db(client: MongoClient[Dict[str, Any]], db_name: str) -> None:
    if not is_client_alive(client):
        logging.critical("Cannot create db")
    client[db_name]


def create_collection(client: MongoClient[Dict[str, Any]], db_name: str, name: str):
    pass

def get_matches_previous(last_days: int = 10) -> List[Match]:
    """Get data from db from last X days"""
    out: List[Match] = []
    return out


# aaaa = Example(datetime.strptime("2023-10-13", "%Y-%m-%d"), 1, False)
# b = Example(datetime.strptime("2023-10-14", "%Y-%m-%d"), 2, True)



# def create_database(client: pymongo.MongoClient()):
#     pass

def update_document():
    pass


def insert_document():
    pass

def get_documents():
    pass

# def main():
#     myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#     mydb = myclient["mydatabase"]
#     mycol = mydb["customers"]

#     mylist = [
#     { "name": "Amy", "address": "Apple st 652"}]


#     x = mycol.insert_many([aaaa.__dict__,
#                            b.__dict__])

#     #print list of the _id values of the inserted documents:
#     print(x.inserted_ids)

#     ccc = mycol.find({"date": {'$lt': datetime.strptime('2024-03-31', "%Y-%m-%d")}, "played": False})
#     for item in ccc:
#         print(item)
#     pass


if __name__ == "__main__":
    main()