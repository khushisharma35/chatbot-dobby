# importing module
from pymongo import MongoClient
from datetime import datetime

# creation of MongoClient
client = MongoClient()


client = MongoClient('mongodb://localhost:27017/')

#inserting the data
def store_data(speaker, text):

    collection1 = client['mongotest2']
    mycollection= collection1['test1']
    conversation = {
        'speaker': speaker,
        'text': text,
        'datetime': datetime.now()
    }
    mycollection.insert_one(conversation)