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

if playing != "y":
        quit()
else:

    print(f"Great! ^_^, let`s beggin!\n")

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
            "Which country holds the world`s greatest pyramid and what is the name ?",
            "How many languages are officially spoken throughout Mexico? ",
            "What animals appear on Mexico`s flag? ", 
            "What is the capital of Mexico and one of the largest cities in the world?", 
            "This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often.", 
            "From which country did Mexico get its independence? ",
            "What countries border Mexico? ", 
            "From the list below, name the most prominent native civilization in the Yucatan peninsula.", 
            "Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?", 
            "The Xoloitzcuintli is the national [what] of Mexico? "
            )
# Here i add the double tuple with the possible multiple choices 
multiple_choices = (
    ("1.El Castillo, Chichen Itza. Mexico ", "2.Prang Temple, Kol Ker. Cambodia ", "3.Giza Pyramid, Cairo. Egypt ", "4.Cholula Pyramid, Puebla. Mexico "), 
    ("1. 10 ", "2. 1 ", "3. 69", "4. 20"), 
    ("1.Bull and Eagle", "2.Eagle and Snake ", "3.Rabbit and Leopard", "4.Snake and Puma"), 
    ("1.Quito ", "2.Monterey ", "3.Buenos Aires", "4.CdMx "),
    ("1.Iztacihuatl", "2.Popocatepetl ", "3.Paricutin ", "4.Krakatoa "),
    ("1.United Kingdom ", "2.Germany ", "3.Spain ", "4.Argentina"),
    ("1.United States & Guatemala ", "2.United States, Guatemala & El Salvador ", "3.United States & Belize ", "4.United States, Guatemala & Belize "),
    ("1.Aztec/Mexica ", "2.Maya ", "3.Tolteca ", "4.Inca "),
    ("1.Hermosillo ", "2.CdMx ", "3.Guadalajara ", "4.Puebla "),
    ("1.Drink", "2.Food ", "3.Dog", "4.Flower "),
    )

answers = ()
guesses = []
socre = 0
question_num = 0 








"""###------[
    {
        'question':
        -'Which country holds the world`s greatest pyramid and what is the name ? ',
        'answers':
        ['El Castillo, Chichen Itza. Mexico', '', '', ''],
        'correct answer': 'Cholula Pyramid, Puebla. Mexico '

    },
    {
        'question':
        -'How many languages are officially spoken throughout Mexico?',
        'answers':,
        'correct answer': '69'
    },
    {
        'question':
        -'What animals appear on Mexico`s flag?',
        'answers':
        
        'correct answer': 'Eagle and Snake'
    },
    {
        'question':
        -'What is the capital of Mexico and one of the largest cities in the world?',
        'answers':
        'correct answer': 'CDMX'

    },
    {
        'question':
        -'This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often.',
        'answers':
        ['', '', '', ''],
        'correct answer': 'Popocatepetl'
    },
    {
        'question':
        -'From which country did Mexico get its independence?'
        'answers'
        ['', '', '', ''],
        'correct answer': 'Spain'
    },
    {
        'question':
        -'What countries border Mexico?',
        'answers':
        ['', '', '', ''],
        'correct answer': 'United States, Guatemala & Belize'
    },
    {
        'question':
        -'From the list below, name the most prominent native civilization in the Yucatan peninsula.',
        'answers':
        ['', 'Maya', 'Toltec', 'Inca'],
        'correct answer': 'Maya'
    },
    {
        'question':
        -'Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?',
        'answers':
        ['Guadalajara', 'Hermosillo', 'Monterrey','CDMX'],
    },
    {
        'question':
        -'The Xoloitzcuintli is the national [what] of Mexico?',
        'answers':
        ['Drink', 'Food', 'Dog', 'Flower'],
        'correct answer': 'Dog'
    }
]
"""
