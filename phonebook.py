phonebook = {'Nick': '2622154016', 'Andrew': '2622150994', 'Dad': '2622156625', 'Mom': '2622150016'}

while True:
    print('Whose phone number would you like? (space to quit)')
    name = input()
    if name == ' ':
        break
    elif name in phonebook: #retrieves number from phonebook
        print(phonebook[name] + ' is ' + name + '\'s phone number.')
    else:
        print('I don\'t have that number.')
        print('Would you like to enter their number? (yes or no)')
        for i in range (0, 4):  #Gives user four chances to answer yes or no
            response = str(input())
            if response.lower() == 'yes':
                print('Okay, enter the number:')
                newnumber = input()
                if newnumber.isdecimal() == True:
                    if len(newnumber) == 10:  #Tests whether entry is a ten-digit number.
                        phonebook[name] = newnumber  #adds number to dictionary called "phonebook"
                        print('Phone number added!')
                else:
                    print('Enter a ten-digit number with no hyphens.')
                break
            elif response.lower() == 'no':
                print('Okay!')
                break
            elif response == ' ':
                break
            else:
                print('I don\'t understand.  Would you like to add that number?')
    print('Back to main menu.')
        

        
    
