#Welcome message and introduction to the game
"""
In the intruduction of the game, i ask the user weather if they are interested on playing, 
their username and weather they would like to know the instructions
"""

print("Welcome to the magic of Mexico Quiz!\n")

"""
Here the user name is asked weather they would like to play or not. 
If yes they are redirected to the next input request, if not, the program quits.
"""
playing = (input("Would you like to play? ('y' or 'n') \n"))

if playing == 'y':
    print(f"Great! ^_^, let`s beggin!\n")

elif playing == "n":
    print("See you another time!")
    quit()
    

"""
User is asked to introduce their prefered username, if they enter other input that letters, 
the program requests the user to input their name again. Also, the user is asked weather to read or not the instructions. 
when requested, instructions appear and then is asked to press enter to start the game. If the user doesnt want to read the  instructions ,
they can procede directly to the game.
"""

username = input("Tell me then, what is your name?\n")

while username.isnumeric():
    print(f"Please enter a valid name\n")
    username = input("Tell me then, what is your name?\n")
    

else:
    print(f"Welcome {username}!\n")

username_instructions = input("Would you like to know the instructions? ('y' or 'n') \n")

if username_instructions == 'y':
    print("Instructions are really simple, when a question pops up, you need to choose from the options available. You can input the answer with the numbers 1,2,3 or 4. The result will be shown to you, and if it is correct, it will be added to your score.")
    print("In the end, you will know if you were aware of these amazing facts about Mexico.")
    print("Press Enter to begin!")
    input()
else :
    print("Press Enter to begin!")
    input()



#Defining my list of questions
"""
List of quesions for the program to iterate through while running the game
"""

questions = (
            "Which country holds the world`s greatest pyramid and what is the name ?\n",
            "How many languages are officially spoken throughout Mexico? \n",
            "What animals appear on Mexico`s flag? \n", 
            "What is the capital of Mexico and one of the largest cities in the world?\n", 
            "This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often.\n", 
            "From which country did Mexico get its independence? \n",
            "What countries border Mexico?\n ", 
            "From the list below, name the most prominent native civilization in the Yucatan peninsula.\n", 
            "Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?\n", 
            "The Xoloitzcuintli is the national [what] of Mexico? \n"
            )
# Here i add the double tuple with the possible multiple choices 
choices = (
    ("A.El Castillo, Chichen Itza. Mexico ", "B.Prang Temple, Kol Ker. Cambodia ", "C.Giza Pyramid, Cairo. Egypt ", "D.Cholula Pyramid, Puebla. Mexico \n"), 
    ("A. 10 ", "B. 1 ", "C. 69", "D. 20\n"), 
    ("A.Bull and Eagle", "B.Eagle and Snake ", "C.Rabbit and Leopard", "D.Snake and Puma\n"), 
    ("A.Quito ", "B.Monterey ", "C.Buenos Aires", "D.CdMx\n "),
    ("A.Iztacihuatl", "B.Popocatepetl ", "C.Paricutin ", "D.Krakatoa \n"),
    ("A.United Kingdom ", "B.Germany ", "C.Spain ", "D.Argentina\n"),
    ("A.United States & Guatemala ", "B.United States, Guatemala & El Salvador ", "C.United States & Belize ", "D.United States, Guatemala & Belize\n "),
    ("A.Aztec/Mexica ", "B.Maya ", "C.Tolteca ", "D.Inca \n"),
    ("A.Hermosillo ", "B.CdMx ", "C.Guadalajara ", "D.Puebla\n "),
    ("A.Drink", "B.Food ", "C.Dog", "D.Flower \n"),
    )

answers = ("D", "C", "B", "D", "B", "C", "D", "B", "B", "C")
guesses = []
socre = 0
question_num = 0 

for question in questions:
    print('*******************************************************************\n')
    print(question)
    for choice in choices[question_num]:
        print(choice)

    guess = input("Enter ( A, B, C, D): ")
    question_num += 1
    guesses.append(guess)

    if guess == answers[question_num]:
        score =+ 1
        print("Correct! you got 1 point")
    else :
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer! Better luck next time.")

