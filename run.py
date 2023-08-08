import random
import textwrap

# Defining my list of questions
"""
List of quesions for the program to iterate through while running the game
"""

data = [
    {
        'question':
        "Which country holds the world`s greatest pyramid and what`s its \
             name?",
        "choices": [
            "El Castillo, Chichen Itza. Mexico ",
            "Prang Temple, Kol Ker. Cambodia ",
            "Giza Pyramid, Cairo. Egypt ",
            "Cholula Pyramid, Puebla. Mexico",
        ],
        'answer': "4",

    },
    {
        "question":
        "How many languages are officially spoken throughout Mexico?",
        "choices": [" 10 ", " 1 ", " 69", " 20"],
        "answer": "3",

    },
    {
        "question":
        "What animals appear on Mexico`s flag?",
        "choices": [
            "Bull and Eagle",
            "Eagle and Snake ",
            "Rabbit and Leopard",
            "Snake and Puma",
        ],
        "answer": "2",
    },
    {
        "question":
        "What is the capital of Mexico and one of the largest cities in \
            the world?",
        "choices": ["Quito ", "Monterey ", "Buenos Aires", "CdMx"],
        "answer": "4",
    },
    {
        "question":
        "This volcano, Located in Puebla, is an active volcano that covers \
            the city in ash relatively often",
        "choices": ["Iztacihuatl", "Popocatepetl ", "Paricutin ", "Krakatoa"],
        "answer": "2",
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
        "choices": [
            "United States & Guatemala ",
            "United States, Guatemala & El Salvador ",
            "United States & Belize ",
            "United States, Guatemala & Belize",
        ],
        "answer": "4",
    },
    {
        "question":
        "From the list below, name the most prominent native civilization \
             in the Yucatan peninsula.",
        "choices": ["Aztec/Mexica ", "Maya ", "Tolteca ", "Inca"],
        "answer": "2",
    },
    {
        "question":
        "Which Mexican city is built on an ancient lakebed, causing it \
            to sink a few inches each year?",
        "choices": ["Hermosillo ", "CdMx ", "Guadalajara ", "Puebla"],
        "answer": "2",
    },
    {
        "question":
        "The Xoloitzcuintli is the national [what] of Mexico?",
        "choices": ["Drink", "Food ", "Dog", "Flower"],
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

    while True:
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
In this function the user will be asked for their name.
Any caracters that are not numerical,
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
 User will be asked if they want to see the instructions dispayed or they want\
     to procede directly to the game.
 The function will proove the caracters inserted are correct and if the option\
     'n' is selected. the program will quit.
 Otherwise the game will prodcede to the questions.
"""


def display_instructions():

    while True:
        username_instructions = (input("Would you like to know the\
            instructions?('y' or 'n') \n"))

        if username_instructions == 'y':
            print("Instructions are really simple, when a question pops up,\
                you need to choose from the options available. You can input\
                    the answer with the numbers 1,2,3 or 4. The result will be\
                        shown to you, and if it is correct, it will be added\
                            to your score.")
            print("In the end, you will know if you were aware of these\
                amazing facts about Mexico.\n")
            print("Press Enter to begin!")
            input()
            break
        elif username_instructions == 'n':
            print("Press Enter to begin!")
            input()
            break
        else:
            print("That is not a valid input, try with 'y' or 'n' .")
            print()


# Start the game function
def start_game():
    """
    This function will start the game when the user presses Enter. tshe random\
         import willrandomly sort the questions.
    the initial score will be set up to 0.
    """
    # Randomly shuffle the questions
    random.shuffle(data)
    # Set up the initial score
    score = 0
    for i, question in enumerate(data):
        # make the question text to a max of 100 with
        small_question = textwrap.wrap(question['question'], width=100)
        # print each line for the small question.
        for line in small_question:
            print()
            print(line)
        for j, choice in enumerate(question['choices']):
            # make the question text to a max of 100 width
            small_choice = textwrap.wrap(choice, width=80)
            for line in small_choice:
                print(f"{j + 1}. {line}")

                """
                Up until this point, the questions are displayed on the terminal, randomly and sincronized with their choices
                thanks to the enumerate function.
                """

        while True:
            players_choice = input("Take a guess, answer '1','2','3' or '4': \n")

            if not players_choice.isnumeric():
                print(" ᕕ( ᐛ )ᕗ Only numeric characters are valid!")
            elif int(players_choice) in [1, 2, 3, 4]:
                break
            else:
                print("(－‸ლ) Answer should be a number between '1' and '4'.")

        if str(players_choice) == question['answer']:
            print("٩(ˊᗜˋ*)و CORRECT! ٩(ˊᗜˋ*)و")
            score += 1
        else:
            print("（◞‸◟） INCORRECT （◞‸◟）")
            print(f"The right answer is {question['answer']}")

        print()
    if score == 10:
        print(" YEY! Well done,you answered all correct!")
        print(f"GAME OVER... you scored : {score}/{len(data)}.")
    else:
        print("Almost there!")
        print(f"GAME OVER... you Scored : {score}/{len(data)}.")

        # Ask the player if they want to play again
        """
        this while loops will ask the player if they want to play again,\
             if so , the whole start_game
        function will run from the beggining. if no, the program will end,\
             and if the user inputs
        something else than 'y' or 'n' to the terminal, they will be asked\
             to input the correct data.
        """

    while True:
        restart_game = input("Would you like to play again? 'y' or 'n' ")
        if restart_game == 'y':
            start_game()
            break
        elif restart_game == 'n':
            print("Good bye, see you soon!")
            exit()
        else:
            print("Please enter 'y' or 'n'")


def run():

    welcome_message()
    player_username()
    display_instructions()
    start_game()


run()
