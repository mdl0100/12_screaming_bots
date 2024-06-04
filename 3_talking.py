# Marcos Lopez
# NLP Program 2
# loads up the bots and you can talk to any of them

from chatterbot import ChatBot
from random import randint
import time

#This is the line that fixes chatterbot not working with later python versions
time.clock = time.time

# Load up the bots
casey = ChatBot("Casey",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///casey.sqlite3")
sidney = ChatBot("Sidney",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///sidney.sqlite3")
billy = ChatBot("Billy",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///billy.sqlite3")
gale = ChatBot("Gale",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///gale.sqlite3")
dewey = ChatBot("Dewey",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///dewey.sqlite3")
stu = ChatBot("Stu",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///stu.sqlite3")
randy = ChatBot("Randy",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///randy.sqlite3")
tatum = ChatBot("Tatum",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///tatum.sqlite3")
killer = ChatBot("Killer",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///killer.sqlite3")
teen = ChatBot("Teen",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///teen.sqlite3")
male = ChatBot("Male",
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///male.sqlite3")
female = ChatBot("Female",
                 storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///female.sqlite3")


exit_conditions = (":quit", "quit", "exit", "Let me leave!")

print('\n\n\n')
print("SCREAM (1994) Chatbot\nType ':quit', 'quit', 'exit', or 'Let me leave!' to exit")
print()
print("You can talk to the following characters:")
print("Casey", "Sidney", "Billy", "Gale", "Dewey", "Stu", "Randy", "Tatum", "Ghostface", sep=", ")
print("Otherwise, it'll just be a random background person: Teen, Male, or Female")
while True:
    query = input("YOU 🗣️ : " )
    if query in exit_conditions:
        break
    else:
        if "CASEY" in query.upper():
            print("CASEY : ", casey.get_response(query))
        elif "SIDNEY" in query.upper():
            print("SIDNEY : ", sidney.get_response(query))
        elif "BILLY" in query.upper():
            print("BILLY : ", billy.get_response(query))
        elif "GALE" in query.upper():
            print("GALE : ", gale.get_response(query))
        elif "DEWEY" in query.upper():
            print("DEWEY : ", dewey.get_response(query))
        elif "STU" in query.upper():
            print("STU : ", stu.get_response(query))
        elif "RANDY" in query.upper():
            print("RANDY : ", randy.get_response(query))
        elif "TATUM" in query.upper():
            print("TATUM : ", tatum.get_response(query))
        elif "GHOST FACE" in query.upper() or "KILLER" in query.upper() or "GHOSTFACE" in query.upper():
            print("GHOST FACE 👻: ", killer.get_response(query))
        else:
            choice = randint(0, 2) % 3
            if choice == 0:
                print("TEEN : ", teen.get_response(query))
            elif choice == 1:
                print("SOME GUY : ", male.get_response(query))
            elif choice == 2:
                print("SOME LADY : ", female.get_response(query))
