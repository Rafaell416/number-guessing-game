import random

def display_welcome_message():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  print("You have limited number of chances to guess the correct number")
  print("Good luck cachón!\n")

def select_random_number():
  random_number = random.randint(1,100) 
  return random_number

def select_difficulty():
  print("Please select the difficulty level:")
  print("1. Easy (10 chances)")
  print("2. Medium (5 chances)")
  print("3. Hard (3 chances)")

  difficulty = int(input("Enter your choice: "))

  if difficulty == 1:
    return {"level":  "Easy", "chances": 10 }
  elif difficulty == 2:
    return {"level":  "Medium", "chances": 5 }
  elif difficulty == 3:
    return {"level": "Hard", "chances": 3}
  else: 
    print("Invalide choice, plase select 1, 2 or 3")


def play_round():
  random_number = select_random_number()
  level, chances = select_difficulty().values()

  attempts_left = chances

  print(f"Great! You have have picked the {level} level, You have {attempts_left} attempts to guess the correct number")
  print("Let's start the game!\n")

  attempts = 0

  while attempts_left > 0:
    try:
      guess = int(input("Enter your guess: "))
    except ValueError:
      print("Invalid input! Please enter a number. ")
      continue

    attempts += 1
    attempts_left -= 1

    if guess == random_number:
      print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
      break
    elif guess > random_number:
      print(f"Incorrect! The number is less than {guess}.")
    else:
      print(f"Incorrect! The number is greater than {guess}.")

    if attempts_left == 0:
      print(f"Thanks for playing, no more attempts my love. The correct number was {random_number} mor") 
    else:
      print(f"You have {attempts_left} attempts left")  


def main():
  display_welcome_message()

  while True:
    play_round()
    play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
    if play_again != "yes":
      print("Thnk you for playing! Goodbye!")
      break


if __name__ == "__main__":
  main()


# Display welcome message ✅
# Select random number between 1 and 100 ✅
# User should be allowed to pick dificulty level ✅
# User should be allowed to enter the guess ✅
# Game logic to continue or end the game ✅