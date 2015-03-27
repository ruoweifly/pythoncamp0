# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# helper function to start and restart the game
def new_game():
    global count
    count = 0
    pass
    
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global n
    n = 7
    global secret_num
    secret_num = random.randint(0, 100)
    print "New game.", "Range is from 0 to 100"
    print "Number of remaining guess is ", n, '\n'
    new_game() 
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global n
    n = 10
    global secret_num
    secret_num = random.randint(0, 1000)
    print "new game"
    print "Range is from 0 to 1000"
    print "Number of remaining guess is ", n, '\n'
    new_game()    
    
def input_guess(guess):
    # main game logic goes here	
    global count
    count = count + 1
    if count < n:
        print "Guess is", guess
        print "Number of remaining guess is ", 7-count
        if int(guess) < secret_num:
            print "higher!"'\n'
        elif int(guess) == secret_num:
            print "correct!"'\n'
            range100()
        else: 
            print "lower!"'\n'
    else:
        print "You ran out of guesses. The number is ", secret_num
    
    
# create frame
frame = simplegui.create_frame("", 300, 300)

# register event handlers for control elements and start frame
frame.add_button("range is [0,100)", range100, 200)
frame.add_button("range is [0,1000)", range1000, 200)
frame.add_input("enter a guess", input_guess, 200)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric

