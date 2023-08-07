import random
import textwrap

# Defining my list of questions
"""
List of quesions for the program to iterate through while running the game
"""

data = [
    {
        'question': 
        "Which country holds the world`s greatest pyramid and what is the name ?",
        "choices": ["El Castillo, Chichen Itza. Mexico ", "Prang Temple, Kol Ker. Cambodia ", "Giza Pyramid, Cairo. Egypt ", "Cholula Pyramid, Puebla. Mexico"],
        'answer': "4",

    },
    {
        "question": 
        "How many languages are officially spoken throughout Mexico?",
        "choices" : [" 10 ", " 1 ", " 69", " 20"],
        "answer" : "3",

    },
    {
        "question": 
        "What animals appear on Mexico`s flag?",
        "choices" :["Bull and Eagle", "Eagle and Snake ", "Rabbit and Leopard", "Snake and Puma"],
        "answer": "2",
    },
    {
        "question": "What is the capital of Mexico and one of the largest cities in the world?",
        "choices" : ["Quito ", "Monterey ", "Buenos Aires", "CdMx"],
        "answer" : "4",
    },
    {
        "question": 
        "This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often",
        "choices" : ["Iztacihuatl", "Popocatepetl ", "Paricutin ", "Krakatoa"],
        "answer" : "2",
    },
    {
        "question":
        "From which country did Mexico get its independence?",
        "choices": ["United Kingdom ", "Germany ", "Spain ", "Argentina"],
        "answer": "3",
    
    },
    {
        "question":
        "What countries border Mexico?",
        "choices" : ["United States & Guatemala ", "United States, Guatemala & El Salvador ", "United States & Belize ", "United States, Guatemala & Belize"],
        "answer" : "4"
    },
    {
        "question": 
        "From the list below, name the most prominent native civilization in the Yucatan peninsula.",
        "choices" : ["Aztec/Mexica ", "Maya ", "Tolteca ", "Inca"],
        "answer": "2",
    },
    {
        "question": 
        "Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?",
        "choices" : ["Hermosillo ", "CdMx ", "Guadalajara ", "Puebla"],
        "answer": "2",
    },
    {
        "question": 
        "The Xoloitzcuintli is the national [what] of Mexico?",
        "choices" : ["Drink", "Food ", "Dog", "Flower"],
        "answer" : "3",
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
            print()
            print(line)
        for j, choice in enumerate(question['choices']):
            # make the question text to a max of 100 with 
            small_choice = textwrap.wrap(choice, width=100)
            for line in small_choice:
                print(f"{j + 1}. {line}")

                """
                Up until this point, the questions are displayed on the terminal, randomly and sincronized with their choices
                thanks to the enumerate function.
                """

        while True:
            players_choice = input(Take a guess, answer '1','2','3' or '4':    \n")

            if int[players_choice] in [1,2,3,4]:
                break
            print(""ᕕ( ᐛ )ᕗ Only answer numbers from '1' to '4', try again!")

            





            """
            inside the try we convert the string entered by the player into an integer. 
            If the value can not be converted into string raises a ValueError, 
            or if the values entered is no 1,2,3, or 4.
            """
            






    
    
    """
    try: 
        [int(value) for value in value]
        if value != int.range(0,5):
            raise ValueError(
                f"Please provide a valid number: '1','2','3','4'"
        )
    """








    """
        while True:
            print()
            player_choice = input(")
            
            here is use a if statement that checks two conditions, if the player chioce is a digit and 
            if it is one of the following. 1,2,3,4.
            
            if player_choice.isdigit() and int(player_choice) in [1,2,3,4]:
                break
                print("ᕕ( ᐛ )ᕗ Only answer numbers from '1' to '4', try again!")
            
            elif player_choice == str(question['choices'].index(question['answer'])+1):
                print("٩(ˊᗜˋ*)و CORRECT! ٩(ˊᗜˋ*)و")
                score += 1
                break
            else: 
                print("（◞‸◟） INCORRECT （◞‸◟）")
                print(f"The right answer is {question['answer']}")

    """         
            
def run():

    welcome_message()
    player_username()
    display_instructions()
    start_game()

run()