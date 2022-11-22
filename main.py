
import conversation
import response as rs
import random
# from database import insertdata
from database2 import insertdata

print("You are talking to chatbot DOBBY")
print("DOBBY:", random.choice(rs.greeting))
name = input()
print("DOBBY :", (random.choice(rs.reply)).format(name))

while True:
    user_message = input(f"{name}:")
    # insertdata.insert_detail(name, user_message)
    insertdata.store_data(name,user_message)

    if "exit"  in user_message:
        break
    try:
        conversation.user(user_message.lower())
    except:
        print("DOBBY: Sorry I didn't get you")
