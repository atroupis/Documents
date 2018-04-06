#This program asks the user a bunch of questions to decide whether the user is Kiki or not.
import sys
print('Hello unknown computer user.  What is your first name?')
name = input()
if name == 'Kiki' or name == 'kiki' or name == 'Kristen' or name == 'kristen':
    print('You are Kiki? Prove it. What month did you start dating Andrew last year?')
else:
    print('I don\'t know you. Goodbye!')
    sys.exit()
month = input()
if month == 'October' or month == 'october' or month == 'oct' or month == 'Oct':
    print('That sounds right. What month were you born?')
else:
    print('No, that\'s not right. You must not be her. Goodbye.')
    sys.exit()
month2 = input()
if month2 == 'March' or month2 == 'march' or month2 == 'Mar'or month2 == 'mar':
    print('Yes, Kiki was born in March. What is your house number on Lafayette Street?')
else:
    print('No, Kiki was born in March. I don\'t know you. Goodbye!')
house = input()
if house == str(159):
    print('Well you could have looked that up somewhere.  I\'m gonna need more proof. What words did he say just before he kissed you for the first time?')
else:
    print('Kiki would know her own address. You must not be her. Goodbye!')
words = input()
if words == 'fuck it' or words == 'Fuck it' or words == "Fuck it!" or words == "Fuck it.":
    print('Oh it really must be you, darling! I hope you liked this lame little program I wrote for you.')
else:
    print('Kiki would know. You are an impostor! Goodbye.')
          
