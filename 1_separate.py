import pickle

# Open Scream Script
with open('scream.txt', 'r') as f:
    lines = f.readlines()

# Every Character name is preceded by 35 spaces (and not tabs like I thought for a while)
character_line = " "*35
# Every line of dialogue is preceded by 25 spaces
dialogue_line = " "*25

# This will make a version of the script with no stage directions, just diaglogue
# I am starting each character name with a tab, in case I want to use this later
# This is the file turned in for the assignment

# At the same time, I'm going to enter each of the lines in a list of lists
# Where the list starts with a character name, and all their lines of dialogue follow
script_lines = []
with open('scream_dialogue.txt', 'w') as f:
    new_line = []
    for line in lines:
        if line.startswith(character_line):
            f.write("\t" + line.strip()+"\n")
            script_lines.append(new_line)
            new_line = [line.strip()]
        elif line.startswith(dialogue_line):
            f.write(line.strip()+"\n")
            new_line.append(line.strip())
    script_lines.append(new_line)
    script_lines = script_lines[1:]

# put the character and dialogue as a tuple by combining all the lines into one
paired_lines = []
for entry in script_lines:
    # Removing off screen (O.S.) from the character name
    if "(O.S.)" in entry[0]:
        entry[0] = entry[0].replace("(O.S.)", "")
    (person, line) = (entry[0], ' '.join(entry[1:]))
    paired_lines.append((person, line))

print(paired_lines[:10])
with open('paired_lines', 'wb') as f:
    pickle.dump(paired_lines, f)

with open('scream_dialogue_pairs.txt', 'w') as f:
    for entry in paired_lines:
        f.write(str(entry))
        f.write("\n")

# Here's a list of all the characters in the script that will make it easier 
# for me to pick which bots I want to train later
# I'll probably just do the main characters: Sidney, Billy, Gale, Dewey, Stu, and Randy
# but it'd be funny to combine the 8 different "teen" characters into one bot.
cast = []
for (person, line) in paired_lines:
    person = person.strip()
    if person not in cast:
        cast.append(person) 
print("Cast: ", cast)

