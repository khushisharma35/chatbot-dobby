import response as rs
import input as i
import random
from database import insertdata

def xyz(message):
    if message in i.movieinput:
        print("DOBBgY:", random.choice(rs.movies))
        insertdata.insert_detail("DOBBY", random.choice(rs.movies))