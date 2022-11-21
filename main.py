import re
import conversation
import response as rs
import input as i
import random

print("You are talking to chatbot DOBBY")
print("DOBBY:", random.choice(rs.greeting))
name = input()
print("DOBBY :", (random.choice(rs.reply)).format(name))

while True:
    user_message = input(f"{name}:")

    if "exit"  in user_message:
        break
    try:
        res = conversation.user(user_message.lower())
        # print("DOBBY: ",res)
        # print("DOBBY:", (random.choice(res)))
        # print("hj")
    except TypeError as e:
        print("DOBBY: Sorry I didn't get you",e)
