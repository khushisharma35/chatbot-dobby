
import conversation
import response as rs
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
        conversation.user(user_message.lower())
    except:
        print("DOBBY: Sorry I didn't get you")
