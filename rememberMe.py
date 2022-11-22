from database import insertdata
from database2 import mongotest
global notes
notes = []
def remember(user_message):
    user_message=user_message.split("remember")
    global notes
    notes.append(user_message[1])
    # print("DOBBY: OK,added to your Reminders")
    print("DOBBY: OK,added to your Reminders")
    insertdata.insert_detail("DOBBY:","OK,added to your Reminders" )
    # mongotest.store_data("DOBBY:", "OK,added to your Reminders")
def notesStored():
    global notes
    print("DOBBY:")
    for note in notes:
        print(note)


