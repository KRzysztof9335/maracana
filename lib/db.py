"""This module is responsible for database interaction"""
import pymongo

HOST = "mongodb://localhost:27017/"
DB_NAME = "MyDataBase"
COLLECTION = "Fixtures"

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

    x = mycol.insert_many(mylist)

    #print list of the _id values of the inserted documents:
    print(x.inserted_ids)


if __name__ == "__main__":
    main()