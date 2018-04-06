# Magic 8 ball
import random
def answer(number):
    if number == 1:
        return 'HMM, TRY ASKING AGAIN.'
    elif number == 2:
        return 'YOUR FUTURE IS MURKY.'
    elif number == 3:
        return 'THIS WILL BE AN AUSPICOUS WEEK IN YOUR LIFE.'
    elif number == 4:
        return 'YOU\'RE FUCKED, BUDDY.'
    elif number == 5:
        return 'JUST RUN WHILE YOU CAN, FAR, FAR AWAY.'
    elif number == 6:
        return 'YOU ARE THE DESCENDANT OF A GREAT PHARAOH OR SOME SHIT.'
    elif number == 7:
        return 'YOU ARE A TRUE BADASS.'
    elif number == 8:
        return 'BAD LUCK AND MISFORTUNE WILL INFEST YOUR PATHETIC SOUL FOR ALL ETERNITY.'
    elif number == 9:
        return 'A PLAGUE BE UPON YOUR HOUSES.'
while True:
    x = random.randint(1,9)  # The number x is a random integer from the randint function in the random module.
    ballanswer = answer(x) # The ball answer is returned by the answer function defined earlier, with input x.
    print('Say presto to shake my magic 8 ball.')
    words = input()  # This if/else loop asks for the magic word.
    if words == 'presto' or words == 'Presto' or words == 'PRESTO' or words == 'presto!' or words == 'Presto!' or words == 'PRESTO!':
        print(ballanswer)
    else:
        print('That is not the magic word.')
    


