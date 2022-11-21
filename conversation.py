import input as i
import response as rs
import rememberMe as rememberMe
import mathematics
import movie
import random


def user(user_message):
    user_msg = user_message.split(" ")
    for message in user_msg:
        if message in i.movieinput:
            return movie.xyz(message)
        elif message in i.hello:
            print("DOBBY :",random.choice(rs.helloreply))
            return
        elif message in i.operations:
            return mathematics.cal(user_message)
        elif message == "remember":
            return rememberMe.remember(user_message)
        elif message == "reminders":
            return rememberMe.notesStored()
        elif message == "thankyou"  or message == "thanks":
            print("DOBBY:", random.choice(rs.feedback))
            ans = input()
            if ans == "yes":
                print("DOBBY:How may I help you")

            elif ans == "no":
                print("DOBBY: If you don't need further help type exit")
            break
    else:
        raise Exception("Sorry")












