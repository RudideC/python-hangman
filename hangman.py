import random
import json

def choose_word():
    with open("words.json", "r") as file:
        words = json.load(file)
    return random.choice(words)

def get_custom_word():
    custom_word = input("Enter a custom word for Hangman: ").lower()
    return custom_word

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters or not letter.isalpha():
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("Welcome to Hangman!")

    custom_word = input("Do you want to use a custom word? (y/n): ").lower()

    if custom_word == 'y':
        try:
            secret_word = get_custom_word()
        except ValueError:
            print("Invalid input. The custom word should only contain letters.")
            return
    else:
        try:
            secret_word = choose_word()
        except FileNotFoundError:
            print("Error: Unable to find the 'words.json' file.")
            return

    guessed_letters = []
    attempts_left = len(secret_word)

    while attempts_left > 0:
        print("\nAttempts left:", attempts_left)
        print(display_word(secret_word, guessed_letters))

        guess = input("Enter a letter or the entire word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                attempts_left -= 1
                print("Incorrect guess. Try again.")
            else:
                print("Good guess!")

        elif len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print("\nCongratulations! You've guessed the word:", secret_word)
                break
            else:
                attempts_left -= 1
                print("Incorrect guess. Try again.")

        else:
            print("Invalid input. Please enter a single letter or the entire word.")

        if all(letter in guessed_letters or not letter.isalpha() for letter in secret_word):
            print("\nCongratulations! You've guessed the word:", secret_word)
            break

    if attempts_left == 0:
        print("\nSorry, you're out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
