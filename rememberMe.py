global notes
notes = []
def remember(user_message):
    user_message=user_message.split("remember")
    global notes
    notes.append(user_message[1])
    print("DOBBY: OK, noted")

def notesStored():
    global notes
    print("DOBBY:")
    for note in notes:
        print( note)


