import random
secretnumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20.')
for guesscount in range(1,7):  #The range 1 to 7 loops only six times because the last number is not included. "guesscount" is just the counting index.
      print('Take a guess.')
      guess = int(input())
      if guess >= 21 or guess <= 0:
            print('A number between 1 and 20, please.')
      elif guess > secretnumber:
          print('Your guess is too high.')
      elif guess < secretnumber:
          print('Your guess is too low.')
      else:
            break

if guess == secretnumber:
    print('Yeah, it was ' + str(secretnumber) + '!')
else:
    print('No, I was thinking of ' + str(secretnumber) + '.')
