import random
from collections import Counter
import string


# Part A: Number Guessing Game
def number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                score = max(0, 100 - (attempts - 1) * 10)
                print("Congratulations! You guessed correctly.")
                print("Number of attempts:", attempts)
                print("Your score:", score)
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# Part B: Word Counter
def word_counter():
    print("\n===== WORD COUNTER =====")

    filename = input("Enter the text file name (example: sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove punctuation and convert to lowercase
        words = [
            word.strip(string.punctuation).lower()
            for word in text.split()
        ]
        words = [word for word in words if word]

        print("\nTotal words:", len(words))

        frequency = Counter(words)

        print("\nWord Frequency:")
        for word, count in frequency.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found! Please check the file name.")
    except OSError:
        print("Unable to read the file.")


# Main Menu
def main():
    while True:
        print("\n===== PYTHON PROJECT =====")
        print("1. Number Guessing Game")
        print("2. Word Counter")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            word_counter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()