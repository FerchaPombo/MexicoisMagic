import random
import textwrap

# Defining my list of questions
"""
List of quesions for the program to iterate through while running the game
"""

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
        "choices":["1.Bull and Eagle", "2.Eagle and Snake ", "3.Rabbit and Leopard", "4.Snake and Puma"],
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

# Welcome message and introduction to the game
"""
In this function the welcome message displays to the user. The user is asked 
weather they want to play. There is a while loop created to validate the users
input as correctly.
"""
print("Welcome to the magic of Mexico Quiz!\n")

def welcome_message():
    playing = None
    
    while  True:
        playing = (input("Would you like to play? ('y' or 'n') \n"))
    
        if playing == 'y':
            print(f"Great! ^_^, let`s beggin!\n")
            break

        elif playing == "n":
            print("See you another time!")
            quit()
            break
        else:
            print("Not a valid option, please choose 'y' o r 'n'")

# Request users name before we can begin the game

"""
In this function the user will be asked for their name. Any caracters that are not numerical, 
will cause the program to reask the question to the user. 
"""

def player_username():
    username = input("Tell me then, what is your name?\n")
    
    while username.isnumeric():
        print("Please enter a valid name \n")
        username = input("Tell me then, what is your name?\n")

    else: 
        print(f"Welcome {username}!\n")

 
# Display instructions function 

"""
 User will be asked if they want to see the instructions dispayed or they want to procede directly to the game.
 The function will proove the caracters inserted are correct and if the option 'n' is selected. the program will quit. 
 Otherwise the game will prodcede to the questions.
"""     

def display_instructions():

    username_instructions = (input("Would you like to know the instructions? ('y' or 'n') \n"))

    while True:

        if username_instructions == 'y':
            print("Instructions are really simple, when a question pops up, you need to choose from the options available. You can input the answer with the numbers 1,2,3 or 4. The result will be shown to you, and if it is correct, it will be added to your score.")
            print("In the end, you will know if you were aware of these amazing facts about Mexico.\n")
            print("Press Enter to begin!")
            input()
            break
        else:
            print("Press Enter to begin!")
            input()
            break


# Start the game function 
def start_game():
    """
    This function will start the game when the user presses Enter. tshe random import willrandomly sort the questions.
    the initial score will be set up to 0.
    """
    # Randomly shuffle the questions
    random.shuffle(data)
    # Set up the initial score 
    score = 0 
    for i, question in enumerate(data):
        # make the question text to a max of 100 with 
        small_question = textwrap.wrap(question['question'],width=100)
        # print each line for the small question.
        for line in small_question:
            print(line)
        for j, choice in enumerate(question['choices']):
            # make the question text to a max of 100 with 
            small_choice = textwrap.wrap(choice, width=100)
            for line in small_choice:
                print(f"{j + 1}. {line}")

                """
                Up until this point, the questions are displayed on the terminal 
                """
        while True:
            player_choice = input("Take a guess, answer '1','2','3' or '4':    \n")

            if player_choice.isdigit() and int(player_choice) in [1,2,3,4]:
                break

            print("ᕕ( ᐛ )ᕗ Only answer numbers from '1' to '4', try again!")

def run():

    welcome_message()
    player_username()
    display_instructions()
    start_game()

run()