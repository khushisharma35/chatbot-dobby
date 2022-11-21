import response as rs
import input as i
import random

def xyz(message):
    # if message in i.input1:
    #     return rs.reply2
    if message in i.movieinput:
        print("DOBBY:", random.choice(rs.movies))
    # elif message in i.input2:
    #     return rs.movies
    # elif message in i.input2:
    #     return rs.feedback
    # elif message in i.positive:
    #     return rs.postivefeedback
