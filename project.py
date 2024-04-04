import random
import cowsay

def main():
    words = get_words()
    answers = get_answers()
    print("This is the wordle game!", end='\n')
    wordle()
    print("Run the project file to play again :)")

def get_answers()->list:
    with open("/workspaces/149331871/final_project/answers.txt", "r") as file:
        return file.readlines()

def get_words()->list:
    words = []
    with open("/workspaces/149331871/final_project/five-letter-words.txt", "r") as file:
        for line in file:
            words.append(line.strip())
    return words


def is_valid_word(guess, words)->bool: #checks if the given guess is a "guessable" word (five-letter-words.txt)
    if guess in words:
        return True
    else: return False
    #use case exemple: is_valid("salad", get_words()) returns True because salad is in there.

def check_guess(guess, secret_word)->str: #this funtion adds the colors
    s = ""
    for i in range(5):
        if guess[i] == secret_word[i]:
            s += "\033[32m" + guess[i] #green
        else:
            if guess[i] in secret_word:
                s += "\033[33m" + guess[i] #yellow
            else:
                s += "\033[0m" + guess[i] #default
    return s + "\033[0m"

def wordle():
    print('Get 6 chances to guess a five-letter word')
    secret_word = random.choice(get_answers())
    attemps = 1


    while attemps <= 6:
        guess = input("Enter your Guess #" + str(attemps) + " :").strip().lower()


        if not is_valid_word(guess.lower(), get_words()):
            print("Not in the words list!")
            continue

        if guess == secret_word:
            print(f"Congratz! You guessed the word {secret_word}")
            break

        else:
            attemps += 1
            feedback = check_guess(guess, secret_word)
            cowsay.cow(feedback)
            continue
    if attemps == 7:
        print(f"You runned out of guesses!\nThe secret word was \033[32m{secret_word}\033[0m")


if __name__ == "__main__":
    main()
