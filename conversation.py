import input as i
import response as rs
import rememberMe as rememberMe
import mathematics
import movie
import random
from database import insertdata
from database2 import mongotest


def user(user_message):
    user_msg = user_message.split(" ")
    # insert_detail({user}, text)
    for message in user_msg:
        if message in i.movieinput:
            return movie.xyz(message)
            # break
        elif message in i.hello:
            print("DOBBY :",random.choice(rs.helloreply))
            # insertdata.insert_detail("DOBBY",random.choice(rs.helloreply))
            mongotest.store_data("DOBBY",random.choice(rs.helloreply))
        elif message in i.operations:
            return mathematics.cal(user_message)

        elif message == "remember":
            return rememberMe.remember(user_message)

        elif message == "reminders":
            return  rememberMe.notesStored()
            break
        elif message == "thankyou" or message == "thanks":
            print("DOBBY:",random.choice(rs.feedback))
            ans = input()
            if ans == "yes":
                print("DOBBY:How may I help you")

            elif ans == "no":
                print("DOBBY: If you don't need further help type exit")
            break

    else:
        raise Exception("Sorry")


