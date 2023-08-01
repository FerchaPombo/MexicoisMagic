#Welcome message and introduction to the game
"""
In the intruduction of the game, i ask the user weather if they are interested om playing, their username and weather they would like to know the instructions
"""

print("Welcome to the magic of Mexico Quiz!\n")

playing = (input("Would you like to play? ('y' or 'n') \n"))

if playing != "y":
        quit()
else:

    print(f"Great! ^_^, let`s beggin!\n")

username = input("Tell me,then, what is your name?\n")

if username.isdigit():
    print(f"Please enter a valid name")
else:
    print(f"Welcome {username}!")
    
username_instructions = input("Would you like to know the instructions? ('y' or 'n') \n")

if username_instructions == 'y':
    print("Instructions are really simple, when a question pops up, you need to choose from the options available. You can input the answer with the numbers 1,2,3 or 4. The result will be shown to you, and if it is correct, it will be added to your score.")
    print("In the end, you will know if you were aware of these amazing facts about Mexico.")
else: 
    quit()

 


#List of questions and possible answers for the quiz game 
"""
questions = [
    {
        'question':
        'Which country holds the world`s greatest pyramid and what is the name ? ',
        'answers':
        ['El Castillo, Chichen Itza. Mexico', 'Prang Temple, Kol Ker. Cambodia', 'Giza Pyramid, Cairo. Egypt', 'Cholula Pyramid, Puebla. Mexico'],
        'correct answer': 'Cholula Pyramid, Puebla. Mexico '

    },
    {
        'question':
        'How many languages are officially spoken throughout Mexico?',
        'answers':
        ['1', '10', '69','20'],
        'correct answer': '69'
    },
    {
        'question':
        'What animals appear on Mexico`s flag?',
        'answers':
        ['Bull and Eagle', 'Eagle and Snake', 'Rabbit and Leopard', 'Snake and Puma'],
        'correct answer': 'Eagle and Snake'
    },
    {
        'question':
        'What is the capital of Mexico and one of the largest cities in the world?',
        'answers':
        ['Quito', 'Bogota', 'Buenos Aires', 'CDMX'],
        'correct answer': 'CDMX'

    },
    {
        'question':
        'This volcano, Located in Puebla, is an active volcano that covers the city in ash relatively often.',
        'answers':
        ['Iztacihuatl', 'Popocatepetl', 'Paricutin', 'Krakatoa'],
        'correct answer': 'Popocatepetl'
    },
    {
        'question':
        'From which country did Mexico get its independence?'
        'answers'
        ['United Kingdom', 'Germany', 'Spain', 'Netherlands'],
        'correct answer': 'Spain'
    },
    {
        'question':
        'What countries border Mexico?',
        'answers':
        ['United States & Guatemala', 'United States, Guatemala & El Salvador', 'United States & Belize', 'United States, Guatemala & Belize'],
        'correct answer': 'United States, Guatemala & Belize'
    },
    {
        'question':
        'From the list below, name the most prominent native civilization in the Yucatan peninsula.',
        'answers':
        ['Aztec/Mexica', 'Maya', 'Toltec', 'Inca'],
        'correct answer': 'Maya'
    },
    {
        'question':
        'Which Mexican city is built on an ancient lakebed, causing it to sink a few inches each year?',
        'answers':
        ['Guadalajara', 'Hermosillo', 'Monterrey','CDMX'],
    },
    {
        'question':
        'The Xoloitzcuintli is the national [what] of Mexico?',
        'answers':
        ['Drink', 'Food', 'Dog', 'Flower'],
        'correct answer': 'Dog'
    }
]
"""
