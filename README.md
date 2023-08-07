# Mexico is Magic Quiz

Mexico is Magic is a simple Python quiz game that deploys to a console.
 
This quiz game starts running with a welcome message, where the user is asked to provide input like their username, and whether they want to play or not.  This is followed by 10 questions, each, with 4 possible choices and just one answer to choose from. 

All the data is stored in the run.py file and nothing is imported or exported to any external file. 
it includes functions that help the program get data from the user, validate the input of the player so we have just the right values, calculate a score and restart the program if needed. 



## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

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
