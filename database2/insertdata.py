import sys
sys.path.insert(1, '/Users/apple/PycharmProjects/pythonProject/')
from database2 import mongodb
from datetime import datetime


client = mongodb.get_database()
db = client['Dobby']


def store_data(speaker, text):
    # Access collection of the database

    collection1 = db['talk']

    conversation = {
        'speaker': speaker,
        'text': text,
        'datetime': datetime.now()
    }
    collection1.insert_one(conversation)

store_data('aa','aa')