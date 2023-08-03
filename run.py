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
    ("1.El Castillo, Chichen Itza. Mexico ", "2.Prang Temple, Kol Ker. Cambodia ", "3.Giza Pyramid, Cairo. Egypt ", "4.Cholula Pyramid, Puebla. Mexico \n"), 
    ("1. 10 ", "2. 1 ", "3. 69", "4. 20\n"), 
    ("1.Bull and Eagle", "2.Eagle and Snake ", "3.Rabbit and Leopard", "4.Snake and Puma\n"), 
    ("1.Quito ", "2.Monterey ", "3.Buenos Aires", "4.CdMx\n "),
    ("1.Iztacihuatl", "2.Popocatepetl ", "3.Paricutin ", "4.Krakatoa \n"),
    ("1.United Kingdom ", "2.Germany ", "3.Spain ", "4.Argentina\n"),
    ("1.United States & Guatemala ", "2.United States, Guatemala & El Salvador ", "3.United States & Belize ", "4.United States, Guatemala & Belize\n "),
    ("1.Aztec/Mexica ", "2.Maya ", "3.Tolteca ", "4.Inca \n"),
    ("1.Hermosillo ", "2.CdMx ", "3.Guadalajara ", "4.Puebla\n "),
    ("1.Drink", "2.Food ", "3.Dog", "4.Flower \n"),
    )

answers = ("4", "3", "2", "4", "2", "3", "4", "2", "2", "3")
guesses = []
socre = 0
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
    else :
        print(":'‑( Incorrect :'‑(")
        print(f"{answers[question_num]} is the correct answer! Better luck next time.")
    question_num += 1

"""
now we need to start displaying the results of the game, as well as the score, in numbers and in percentages.
make sure to redo format of the answers and guesess.
"""

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

# calculating the score function
"""
This function is used to calculate the score of the game. It will return a number of correct answers,
as well as a percentage of how much knowledge. This percentage will be given as an integer. rounding the number so it doesnt come out in a decimal.
"""

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")