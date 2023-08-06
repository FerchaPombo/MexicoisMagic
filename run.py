# Welcome message and introduction to the game
"""
In this function the welcome message displays to the user. The user is asked 
weather they want to play. There is a while loop created to validate the users
input as correctly.
"""

def welcome_message():
    print("Welcome to the magic of Mexico Quiz!\n")


while True:
    playing = (input("Would you like to play? ('y' or 'n') \n"))
    
    if playing == 'y':
        print(f"Great! ^_^, let`s beggin!\n")
        break

    elif playing == "n":
        print("See you another time!")
        quit()
    else:
        print("Not a valid option, please choose 'y' o r 'n'")

# Request users name before we can begin the game

"""
In this function the user will be asked for their name. Any caracters that are not numerical, 
will cause the program to reask the question to the user. 
"""


def player_username():

while True 
    username = input("Tell me then, what is your name?\n")
  
    if username.isnumeric() :
        print("Please enter a valid alphabetic character name \n")
        break   
    else :
        print(f"Welcome {username}!\n") 


"""
# Display instructions function 


 User will be asked if they want to see the instructions dispayed or they want to procede directly to the game.
 The function will proove the caracters inserted are correct and if the option 'n' is selected. the program will quit. 
 Otherwise the game will prodcede to the questions.
    
username_instructions = input("Would you like to know the instructions? ('y' or 'n') \n")

def display_instructions():
    
    while True:
        username_instructions = input("Would you like to know the instructions? ('y' or 'n') \n")

        if username_instructions == 'y':
            print("Instructions are really simple, when a question pops up, you need to choose from the options available. You can input the answer with the numbers 1,2,3 or 4. The result will be shown to you, and if it is correct, it will be added to your score.")
            print("In the end, you will know if you were aware of these amazing facts about Mexico.")
            print("Press Enter to begin!")
            input()
        else:
            print("Press Enter to begin!")
            input()


# Defining my list of questions

List of quesions for the program to iterate through while running the game


data = [
    {
        'question': "Which country holds the world`s greatest pyramid and what is the name ?",
        'choices': ["1.El Castillo, Chichen Itza. Mexico ", "2.Prang Temple, Kol Ker. Cambodia ", "3.Giza Pyramid, Cairo. Egypt ", "4.Cholula Pyramid, Puebla. Mexico"],
        'answer': "4",

    },
    {
        "question": "How many languages are officially spoken throughout Mexico?",
        "choices": ["1. 10 ", "2. 1 ", "3. 69", "4. 20"],
        "answer" : "3",

    },
    {
        "question": "What animals appear on Mexico`s flag?",
        "choices": ["1.Bull and Eagle", "2.Eagle and Snake ", "3.Rabbit and Leopard", "4.Snake and Puma"],
        "answer": "2",
    },
    {
        "question": "What is the capital of Mexico and one of the largest cities in the world?",
        "choices": ["1.Quito ", "2.Monterey ", "3.Buenos Aires", "4.CdMx"],
        "answer": "4",
    },
    {
        "question": "This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often",
        "choices": ["1.Iztacihuatl", "2.Popocatepetl ", "3.Paricutin ", "4.Krakatoa"],
        "answers": "2",
    },
    {
        "question": "From which country did Mexico get its independence?",
        "coices": ["1.United Kingdom ", "2.Germany ", "3.Spain ", "4.Argentina"],
        "answer": "3",
    },
    {
        "question": "What countries border Mexico?",
        "choices": ["1.United States & Guatemala ", "2.United States, Guatemala & El Salvador ", "3.United States & Belize ", "4.United States, Guatemala & Belize"],
        "answer": "4"
    },
    {
        "question": "From the list below, name the most prominent native civilization in the Yucatan peninsula.",
        "choices": ["1.Aztec/Mexica ", "2.Maya ", "3.Tolteca ", "4.Inca"],
        "answer": "2",
    },
    {
        "question": "Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?",
        "choices": ["1.Hermosillo ", "2.CdMx ", "3.Guadalajara ", "4.Puebla"],
        "answer": "2",
    },
    {
        "question": "The Xoloitzcuintli is the national [what] of Mexico?",
        "choices": ["1.Drink", "2.Food ", "3.Dog", "4.Flower"],
        "answer": "3",
    }
]

def get_questions():
    pass
def show_question():
    answer = 1 
    return answer
def check_answer(choice):
    pass
def update_score():
    pass
def restart_game():
    pass


def run():
    display_welcome_message()
    display_player_username()
    display_instructions()
    questions = get_questions()

    for question in questions:
        answer = show_questions
        check_answer(answer)



guesses = []
score = 0
question_num = 0

for question in questions:
    print('*******************************************************************\n')
    print(question)
    for choice in choices[question_num]:
        print(choice)

    guess = input("Enter ( 1, 2, 3, 4): ")
    guesses.append(guess)

    if guess == answers[question_num]:
        score =+ 1
        print("^_^Correct! you got 1 point^_^")
    else:
        print(":'‑( Incorrect :'‑(")
        print(f"{answers[question_num]} is the correct answer! Better luck next time.")
    question_num += 1



print('*******************************************************************\n')
print('*******(ᗒ ᗨᗕ)***********RESULTS************(ᗒᗨ ᗕ)****************\n')
print('*******************************************************************\n')

print("Correct answers: ")
for answer in answers :
    print(answer, end=" ")
    print()

print("This were your guesses: ")
for guess in guesses:
    print(guess, end=" ")
    print()


score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
"""