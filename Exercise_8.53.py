# “Guess the Number” game
def Guess_the_num():
  Guessnum = 66
  attempts = 0
  print("Welcome to the guess the number game")
  while True:
    guess = input("Guess the number: ")
    try:
      guess = int(guess)
    except ValueError:
      print("Please enter a valid number!")
      continue
    attempts +=1
    
    if guess < Guessnum:
      print("Too low")
    elif guess > Guessnum:
      print("Too high")
    else:
      print("Correct guess!!!")
      break   
      
Guess_the_num()