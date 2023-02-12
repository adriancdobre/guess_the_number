#Obiectivele jocului de ghicire a numărului:
import random
from art import logo



numbers = []

for n in range(1,101):
  numbers.append(n)
  
print(logo)
print("Welcome to the Number Guessing Game:")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. types 'easy' or 'hard': ")

if (difficulty == "hard"):
  number_of_guess = 5 
else:
  number_of_guess = 10
  
random_number = random.choice(numbers)
number = int(input("Make a guess: "))

while number_of_guess > 0:
  if (number != random_number):
    if(number > random_number):
      print("To high.")
      number_of_guess -= 1
      print(f"You have {number_of_guess} attempts remaining to guess the number")  
      number = int(input("Make a guess: "))
    else:
      print("To low.")
      number_of_guess -= 1
      print(f"You have {number_of_guess} attempts remaining to guess the number")  
      number = int(input("Make a guess: "))
  else:
     print(f"You got it.The answer was:{number} ")
     number_of_guess = 0 

  
    
  

  





