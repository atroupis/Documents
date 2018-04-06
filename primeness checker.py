#This program checks numbers for primeness and lists divisors, if any.
import sys
print('Enter the number you would like to check for primeness.')
number = input()
check = 2
divisorfound = False
while check <= (int(number)/2):  #This loop checks whether remainder of number and check is 0 or not.
    if(int(number)%check == 0):
        print('The number is not prime because it is divisible by ' + str(check) + '.')  #Prints all found divisors.
        divisorfound = True  #If a divisor is found, divisorfound changes from true to false during the loop.
    check = check + 1
if divisorfound == False:
    print('The number is prime.')
else:
    sys.exit()
