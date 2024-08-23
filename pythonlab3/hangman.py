import random


words = ["python", "django", "odoo", "Conan", "Mariam", "Naruto"]

def hangman():

    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    guessed_letters = set()
    max_attempts = 7
    attempts = 0


    player_name = input("Please enter your name: ")
    print(f"Welcome to Hangman, {player_name}!")
    print("Let's start the game!")


    while attempts < max_attempts:
        print("\nCurrent word: " + " ".join(guessed_word))
        guess = input("Guess a letter or the full word: ").lower()


        if guess == word_to_guess:
            print(f"The word is correct! Congratulations, {player_name}!")
            break

        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'. Try again.")
            elif guess in word_to_guess:
                print(f"Nice! The letter '{guess}' is in the word.")
                guessed_letters.add(guess)
                for i, letter in enumerate(word_to_guess):
                    if letter == guess:
                        guessed_word[i] = guess
                if "_" not in guessed_word:
                    print(f"Congratulations, {player_name}! You've guessed the word: {word_to_guess}")
                    break
            else:
                print(f"No, the letter '{guess}' isn't in the word.")
                guessed_letters.add(guess)
                attempts += 1
                print(f"You have {max_attempts - attempts} attempts left.")
        else:
            print("Invalid input. Please enter a single letter or the full word.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The word was: {word_to_guess}")


hangman()
