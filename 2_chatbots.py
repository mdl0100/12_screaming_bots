# Marcos Lopez
# NLP Program 2
# This file trains the chatbots on the Scream script
# Each of the 12 bots will have a basic starting 
# set up of 5 lines and responses, that are similar in nature
# but unique to the character (or character amalgamation)

import pickle
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from random import randint

import time 

#This is the line that fixes chatterbot not working with later python versions
time.clock = time.time

# Separate.py was the file that processed the scream script
# I used pickle to dump the paired lines list into a file
# But now I can load back the list as a list using pickle.load
with open('paired_lines', 'rb') as f:
    paired_lines = pickle.load(f)

# 9 Main Characters, and 3 Generic Characters
casey = ChatBot('CASEY', 
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///casey.sqlite3")
killer = ChatBot('Ghost Face',
                 storage_adapter="chatterbot.storage.SQLStorageAdapter",
                 database_uri="sqlite:///killer.sqlite3")
sidney = ChatBot('Sidney',
                 storage_adapter="chatterbot.storage.SQLStorageAdapter",
                 database_uri="sqlite:///sidney.sqlite3")
billy = ChatBot('Billy',
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///billy.sqlite3")
gale = ChatBot('Gale',
               storage_adapter="chatterbot.storage.SQLStorageAdapter",
               database_uri="sqlite:///gale.sqlite3")
dewey = ChatBot('Dewey',
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///dewey.sqlite3")
stu = ChatBot('Stu',
              storage_adapter="chatterbot.storage.SQLStorageAdapter",
              database_uri="sqlite:///stu.sqlite3")
randy = ChatBot('Randy',
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///randy.sqlite3")
tatum = ChatBot('Tatum',
                storage_adapter="chatterbot.storage.SQLStorageAdapter",
                database_uri="sqlite:///tatum.sqlite3")
teen = ChatBot('Teen',
               storage_adapter="chatterbot.storage.SQLStorageAdapter",
               database_uri="sqlite:///teen.sqlite3")
male = ChatBot('male',
                     storage_adapter="chatterbot.storage.SQLStorageAdapter",
                     database_uri="sqlite:///male.sqlite3")
female = ChatBot('female',
                       storage_adapter="chatterbot.storage.SQLStorageAdapter",
                       database_uri="sqlite:///female.sqlite3")

# There are 5 lines in the scream that look like roles, but are not characters
non_characters = ['THE END', '9-1-1 SEND', 'FAX MODEM', 'HELP KILLER', '34 ELM ST']

# The killer is referred to as the following in the script, since you only hear his voice
# And you don't know which characters are the killers (SPOILER ALERT: It's Billy and Stu)
mans_voice = ['MAN', 'VOICE', "MAN'S VOICE"]

# The rest of these are just slotting the remaining cast into three categories
teen_characters = ["TEEN #1", "TEEN #2", "TEEN #3", "BORED TEEN", "BOY TEEN", "OTHER GUYS", "GIRL #1", "GIRL #2", "GHOST #1", "GHOST #2", "SOME TEEN", "ANOTHER TEEN"]
other_males = ["MAN", "FATHER", "MR. PRESCOTT", "DISC JOKEY", "SHERIFF BURKE", "MR. HIMBRY", "MR. LOOMIS", "KENNY"]
other_females = ["MOTHER", "MRS. TATE", "REPORTER #1", "REPORTER #2", "CHECK OUT LADY", "MAMA RILEY"]

# We need starter lines for each character, where they respond to common questions
starter_lines = {
    'CASEY':  {
        'greeting': "Hello, can you hear me?",
        'name': "Casey",
        'occupation': "highschool student at Woodsboro High",
        'location': 'at my house', 
        'hobbies': 'watching scary movies',
        'random sentence': "We can talk about all kinds of cool stuff!"
    }, 
    'GHOST FACE': {
        'greeting': "...Hi",
        'name': "Ghost Face",
        'occupation': "killer", 
        'location': 'right behind you',
        'hobbies': 'killing those who anger me',
        'random sentence': "I guess we can talk about movies, but I may have to kill you soon."
    },
    'SIDNEY': {
        'greeting': "Hi!",
        'name': "Sidney", 
        'occupation': 'highschool student at Woodsboro High, but... I guess I\'m kind of the lead here too',
        'location': 'in Woodsboro',
        'hobbies': '...actually I haven\'t had that much time for hobbies lately',
        'random sentence': "I really don't think I can talk for very long. Can we move this along?"
    },
    'BILLY': {
        'greeting': "What do you want?",
        'name': "Billy",
        'occupation': 'normal boy in some small town',
        'location': 'here, unfortunately', 
        'hobbies': 'not kill people, definitely. I\'m absolutely trust worthy',
        'random sentence': "I have an alibi for whatever you're about to ask me."
    }, 
    'STU': {
        'greeting': "Hiiiiiiya", 
        'name': 'Stu', 
        'occupation': 'professional accomplice',
        'location': 'in plain sight of a bunch of witnesses', 
        'hobbies': 'help billy not kill people',
        'random sentence': "I just want to be famous."
    },
    'RANDY': {
        'greeting': "Hey, what's up?",
        'name': 'Randy',
        'occupation': 'scary movie expert',
        'location': 'in the middle of the party telling everyone what not to do', 
        'hobbies': 'staying alive',
        'random sentence': "I'm going to live until the second movie."
    },
    'GALE':{
        'greeting': "Hello, young sleuth",
        'name': 'Gale',
        'occupation': 'reporter for Top Story',
        'location': 'wherever the story is',
        'hobbies': 'getting the scoop',
        'random sentence': "Did you know that I'm basically the hero of this story?"
    },
    'DEWEY': {
        'greeting': "Hey there",
        'name': 'Dewey',
        'occupation': 'Sheriff of Woodsboro',
        'location': 'with Sidney, trying to keep her safe',
        'hobbies': 'protecting the town',
        'random sentence': "Don't mind Gale, she's nicer than she seems."
    },
    'TATUM': {
        'greeting': "What do you want?",
        'name': 'Tatum',
        'occupation': 'highschool student at Woodsboro High',
        'location': 'with my brother Dewey, and my best friend Sidney',
        'hobbies': 'doing watever I want in the moment', 
        'random sentence': "I am so over this whole serial killer thing. Can we talk about something else?"
    },
    'OTHER': {
        'greeting': "Hi",
        'name': "I'm actually like 8 different people amalgamated into one", 
        'occupation': "resident of Woodsboro",
        'location': 'in the background of the scene', 
        'hobbies': 'moving the plot along or reacting to the main characteres', 
        'random sentence': "I don't know. You pick something."
    }
}

# Here are the five lines that each character will start with
def initialize(name):
    person = starter_lines[name]
    return [f"Hi {person['name']}", 
                f"{person['greeting']}. I'm {person['name']}",
            f"What do you do here? {person['name']}", 
                f"I'm a {person['occupation']}",
            f"Where are you {person['name']}?", 
                f"I'm {person['location']}", 
            f"What do you like to do {person['name']}?", 
                f"I like {person['hobbies']}",
            f"What should we talk about {person['name']}?", 
                f"{person['random sentence']}"]

# These lists will be used to train the bots by adding in their lines
casey_list = initialize('CASEY')
killer_list = initialize('GHOST FACE')
sidney_list = initialize('SIDNEY')
billy_list = initialize('BILLY')
gale_list = initialize('GALE')
dewey_list = initialize('DEWEY')
stu_list = initialize('STU')
randy_list = initialize('RANDY')
tatum_list = initialize('TATUM')
teen_list = initialize('OTHER')
male_list = initialize('OTHER')
female_list = initialize('OTHER')

# print(paired_lines[:10])

# Adding the previous line spoken, plus the character 
# line into a list for them to be trained later
for i in range(len(paired_lines)):
    if i != 0:
        prev_line = paired_lines[i-1][1]
    person = paired_lines[i][0]
    line = paired_lines[i][1]
    if person in non_characters:
        continue
    if person == 'CASEY':
        if len(casey_list) <=12:
            casey_list.append(" ")
        else:
            casey_list.append(prev_line)
        casey_list.append(line)
    elif person in mans_voice:
        killer_list.append(prev_line)
        killer_list.append(line)
    elif person == 'SIDNEY':
        sidney_list.append(prev_line)
        sidney_list.append(line)
    elif person == 'BILLY':
        billy_list.append(prev_line)
        billy_list.append(line)
    elif person == 'GALE':
        gale_list.append(prev_line)
        gale_list.append(line)
    elif person == 'DEWEY':
        dewey_list.append(prev_line)
        dewey_list.append(line)
    elif person == 'STU':
        stu_list.append(prev_line)
        stu_list.append(line)
    elif person == "TATUM":
        tatum_list.append(prev_line)
        tatum_list.append(line)
    elif person == 'RANDY':
        randy_list.append(prev_line)
        randy_list.append(line)
    elif person in teen_characters:
        teen_list.append(prev_line)
        teen_list.append(line)
    elif person in other_males:
        male_list.append(prev_line)
        male_list.append(line)
    elif person in other_females:
        female_list.append(prev_line)
        female_list.append(line)

# # Sanity Check - How many lines each character has (Should be > 0)
# print("\nCasey: ", len(casey_list))
# print("\nKiller: ", len(killer_list))
# print("\nSidney: ", len(sidney_list))
# print("\nBilly: ", len(billy_list))
# print("\nGale: ", len(gale_list))
# print("\nDewey: ", len(dewey_list))
# print("\nStu: ", len(stu_list))
# print("\nRandy: ", len(randy_list))
# print("\nTatum: ", len(tatum_list))
# print("\nTeen: ", len(teen_list))
# print("\nMale: ", len(male_list))
# print("\nFemale: ", len(female_list))


# Add the script to the ListTrainers
casey_trainer = ListTrainer(casey)
killer_trainer = ListTrainer(killer)
sidney_trainer = ListTrainer(sidney)
billy_trainer = ListTrainer(billy)
gale_trainer = ListTrainer(gale)
dewey_trainer = ListTrainer(dewey)
stu_trainer = ListTrainer(stu)
randy_trainer = ListTrainer(randy)
tatum_trainer = ListTrainer(tatum)
teen_trainer = ListTrainer(teen)
male_trainer = ListTrainer(male)
female_trainer = ListTrainer(female)

# Training the chatbots
casey_trainer.train(casey_list)
killer_trainer.train(killer_list)
sidney_trainer.train(sidney_list)
billy_trainer.train(billy_list)
gale_trainer.train(gale_list)
dewey_trainer.train(dewey_list)
stu_trainer.train(stu_list)
randy_trainer.train(randy_list)
tatum_trainer.train(tatum_list)
teen_trainer.train(teen_list)
male_trainer.train(male_list)
female_trainer.train(female_list)

# Done