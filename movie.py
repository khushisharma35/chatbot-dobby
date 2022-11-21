import response as rs
import input as i
import random

def xyz(message):
    if message in i.movieinput:
        print("DOBBY:", random.choice(rs.movies))
