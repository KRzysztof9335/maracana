"""This module is responsible for database interaction"""
from dataclasses import dataclass
import pymongo
from datetime import datetime
from typing import List

from .models import Match

HOST = "mongodb://localhost:27017/"
DB_NAME = "MyDataBase"
COLLECTION = "Fixtures"


@dataclass
class Example:
    date: datetime
    num: int
    played: bool


def get_matches_previous(last_days: int = 10) -> List[Match]:
    """Get data from db from last X days"""
    out: List[Match] = []
    return out


aaaa = Example(datetime.strptime("2023-10-13", "%Y-%m-%d"), 1, False)
b = Example(datetime.strptime("2023-10-14", "%Y-%m-%d"), 2, True)

def update_document():
    pass

def get_documents():
    pass

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
    { "name": "Amy", "address": "Apple st 652"}]


    x = mycol.insert_many([aaaa.__dict__,
                           b.__dict__])

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)

    ccc = mycol.find({"date": {'$lt': datetime.strptime('2024-03-31', "%Y-%m-%d")}, "played": False})
    for item in ccc:
        print(item)
    pass


if __name__ == "__main__":
    main()