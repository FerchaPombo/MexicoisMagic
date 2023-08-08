# **Mexico is Magic Quiz**

Mexico is Magic is a simple Python quiz game that deploys to a console.

This quiz game starts running with a welcome message, where the user is asked to provide input like their username, and whether they want to play or not.  This is followed by 10 questions, each, with 4 possible choices and just one answer to choose from. 

All the data is stored in the run.py file and nothing is imported or exported to any external file. 
it includes functions that help the program get data from the user, validate the input of the player so we have just the right values, calculate a score and restart the program if needed. 

## **Features**

### How to play

*The empty screen opens with a Welcome message.

*The player is asked whether they want to play, and if the answer is 'y' they are asked what is their name. If the answer is 'n' the program quits.

*The username can not be left empty and the program will ask again for their name and validate the data in alphabetical characters. 

*The player is then, asked whether they want to read the instructions or skip that step. when the answer is 'n' the program goes directly to the option "Press Enter to continue". If the player answers 'y' the instructions display and they need to press " enter" to continue. If they input data other than 'y' or 'n' they are asked to enter valid data.

*After this, the multiple choice questions display randomly,  selected by the program, and the user is prompted to select an answer from the list numbered 1-4. the goal is for the user to guess correctly as many as possible.

*After answering all 10 questions, the score of the player is displayed in an x/10 format.

*The player then has the option to restart the game or quit the program.

## Game elements 

### _1 - Player username_

 *After the welcome message, the player is asked to enter their username. 
*The player must enter a valid data type, that means any alphabetical character, and at least 1, otherwise they will receive an error message. 

!insert image of username asked 

!add image when it was incorrectly inputed 

### _2 - Instructions_

 * After the player enters their name, they are offered the possibility of reading the instructions of the game or continuing without it. 

!add image of instructions asked ,plus instructions

*After any of the two choices they are asked to press enter to continue to the quiz. 
*If they enter something other than 'y' or 'n', the player is asked to answer again the question.
!imagen de press enter to continue 

### _3 - Quiz Questions_

* The player is presented with the first randomized quiz question.
this is achieved by the import random function at the beginning of the run.py file. 
image 'random.shuffle(data)'
* After the first question is printed in the console, the 4 possible choices appear, but only one is correct.  This is achieved by using the enumerate() function. this function itinerates through the items in the 'data' dictionary with all the 'questions', 'choices', and 'answer'.

* The console displays instructions on how to answer, and requests the player to input their answer via one of these numbers:  '1', '2', '3', or '4'.

 * This loop is repeated until the 10th question is answered.

!add image of the questions 

### _4 - Correct Answer_

 * When the player answered the question correctly, a message letting them know the answer was CORRECT will appear in the console.
!image correct 

 * When the answer is correct, the player's score will increase by one point. This variable is defined inside the same run_game() and the score will only be displayed at the end of the quiz. 

!add image of correct answer 

### _5 - Incorrect Answer_

*When the player answered the question correctly, a message letting them know the answer was INCORRECT will appear in the console. when this happens, the player's score will not be incremented.
!image incorrect 

!add image of incorrect answer 

### _6 - Invalid input verification_

 * If the player enters anything other than the digits 1-4 as an answer, the player will receive this message: " ᕕ( ᐛ )ᕗ Only answer numbers from '1' to '4', try again!"
the verification of the input is made by a while loop  that: 
1 converts any input into an integer.
2 checks whether the data is inside the range 1-4  

!image of invalid entries 

### _7 - Final Score_

 * When all 10 questions are answered, the console displays the score. The number of correct answers is compared to the number of total questions.

* When the player gets all 10 answers correctly, a unique message appears: " YEY! {player_username}, you are almost Mexican!"

!image of top score 

### _8 - Play Again_

 * The console will display a message asking the player if they would like to play again. 

!asking the player to play again 

 * If the player enters 'y' the game will start again. If the player enters 'n' they will receive a closing message and the program will quit.

!closing message

 * If the User presses 'y', the game will be restarted.
 * If the User presses 'n', they will receive a closing message, and the game ends.





## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
