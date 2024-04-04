#Playing Wordle with Cowsay
##This is an implementation of the Wordle game in python using the cowsay library.

I have been playing Wordle for a while via the [Wordle](https://www.nytimes.com/games/wordle/index.html) nytimes website.
Wordle is a daily word game that involves figuring out a secret five-letter word.
You play by guessing different five-letter words to see how close they are to the secret word. When you submit a guess, the game will tell you how close your guess is by color-coding each letter in your guess like this:
If a letter is in the correct place, it lights up in green.
If it's not in the correct place, but still in the word, it lights up in yellow.
If a letter is not in the secret word at all, the letter stays the same.


One thing to keep in mind though, is that you can only play once a day, so I thought myself what about making a python game that does exactly that!
So that's what I did, and I added a cow displaying the letters using the cowsay library to make it look more fun and interactive.


In my project, I have 6 files:
- five-letter-words.txt : Which contains all the five-letter words that the player could potentially guess (roughly 5700)
- answers.txt : Which contains all the possible answers. Which means the secret word will be generated in this file using random.choice() method (roughly 2300)
- requirements.txt : Shows the pip-installable module that I used, in this case the cowsay one for aesthetic reasons.
- project.py : Which basically runs the game. It has a main function and 5 other functions:
get_answers() : This function generate all the possible secret word in the answers.txt file and returns a list containing all those words.
get_words() : This function generate all the possible words that the player can guess in the five-letter-words.txt file and returns a list containing all those words.
is_valid_word(guess, words) : this function takes two parameters: guess and words. It checks if the guess parameter is in the words parameter. It is useful to check if the player's input is indeed in the get_answers() list. It returns a boolean.
check_guess(guess, secret_word) : this function takes two parameters: guess and secret_word. It checks if the player's guess is the secret word. It returns a boolean.
check_guess(guess, secret_word): this function takes two parameters as well: guess and secret_word. It adds the color (green or yellow or default color) according to the guess and the secret word that the player has to guess.
wordle(): this function implements the core logic of the game. It generates the secret word, tracks the attemps of the player...

- test_project.py : Which tests 3 of the 5 functions of the project.py file. It has a main() and three other functions (test_get_answers(), test_get_words(),test_is_valid_word())
- README.md : The one you are reading right now!

The game is playable via the terminal, you just have to run the project.py file.
You can play as much as you want, a new secret word is generated every time the project file runs thanks to the the random module.

Thank you to David Malan and CS50P staff.
THIS was CS50P.
