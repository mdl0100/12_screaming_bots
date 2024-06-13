# Summary
This project idea is to build and train several chatbots based on the characters from 1996 Wes Craven film Scream. 

### Files
| name  |file   |
|---|---|
| 1_separate.py  | Used to clean the script to be used for chatbots, separating each line of dialogue into it's character, and tracking the previous line said by someone else  |
| 2_chatbots.py  | Used for initial setup of each character, including background story and initial training on the Scream script  |
| 3_talking.py  | The actual file to run to start speaking to each chacter. If none of the following files are present, first run the above to generate the .sqlite3 files  |
| *.sqlite3 | Each of these is the character break down lines that chatterbot uses to make the bot. There should be 12 (one for each character). 
| scream.txt| The Scream script|

### Summary of Actions
You can talk with any of the main and supporting characters from the movie, or one of 3 amalgamations from the unnamed or ancillary characters. 
You simply use their name in your querery or response, and that character will answer.
If you use more than one character's name in your input line, the first character named will respond. 
If you use **no** characters name, then one of the three amalgamated characters will respond at random. 

### Characters
- **Casey** - A high-schooler, dies pretty quickly, not a lot of dialogue to work with
- **Sidney** - A strong and resilient high-schooler traumatized by the murder of her mother
- **Billy** - Sidney's boyfriend, who possesses a passion for horror movies
- **Gale** - A snarky and ruthless investigative journalist
- **Dewey** - The goofy and hapless deputy sheriff
- **Tatum** - Sidney's spunky best friend and Dewey's sister
- **Stu** - The eccentric and clumsy boyfriend of Tatum, and Billy's best friend
- **Randy** - A horror film fanatic
- **Ghostface** - The murderer and (spoilers!) one (or two!) of the above characters. Will answer to "Ghostface" "Ghost Face" or "Killer", case-insensitive
- **Teen** - Combination of 12 characters in script with few lines (teen #1, teen #2, teen #3, bored teen, boy teen, other guys, girl #1, girl #2, ghost #1, ghost #2, some teen, and bored teen)
- **MALE#** - Combination of 8 characters that didn't rise to prominent roles (man, father, mr. prescott, disc jokey, sheriff burk, mr. himbry, mr. loomis, kenny)
- **Female** - Combination of 6 characters that didn't rise to prominent roles (mother, mrs. tate, reported #1, reporter #2, check out lady, mama riley)

#### Backgrounds
Each character also has a prewritten background that can be accessed usually by typing one of the following inputs:
- Hi {person's name}
- What do you do here {name}?
- Where are you from {name}?
- What do you like to do {name}?
- What should we talk about {name}?

Note: It is not guaranteed that the character responds exactly to that line with the intended response, as the chatbot will change it's inputs as you interact with it over time. 

#### Example 
<img width="968" alt="ConversationPt1" src="https://github.com/mdl0100/12_screaming_bots/assets/7751091/90677e91-3932-4617-ae24-dc524a40dad5">
<img width="968" alt="ConversationPt2" src="https://github.com/mdl0100/12_screaming_bots/assets/7751091/1b3701ca-a52c-477d-aad7-b3f20ad19c11">

### Resources
- The script was pulled from [dailyscript.com](http://dailyscript.com/scripts/Scream.txt)
- The python package [chatterbot](https://chatterbot.readthedocs.io/en/stable) was used to make the chat bots. 
