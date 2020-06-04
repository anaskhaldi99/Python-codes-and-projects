# STUDENT NAME: ANAS ALKHALDI
# STUDENT ID : 217882737
import random
print "----- First Hero -----"
hero1 = raw_input("please type your hero's name:")
# in case hero 1 had no name
while hero1 == "":
    print "error"
    print "----- First Hero -----"
    hero1 = raw_input("please type your hero's name:")

print "----- Second Hero -----"
hero2 = raw_input("please type your hero's name:")
# in case hero 2 had no name
while hero2 == "":
    print "error"
    print "----- Second Hero -----"
    hero2 = raw_input("please type your hero's name:")
# in case second name was same as first name
while hero2 == hero1:
    print hero1, "is taken, please choose another name!"
    print "----- Second Hero -----"
    hero2 = raw_input("Please write Your hero's name:")
    while hero2 == "": # not to return back to the same error
        print "error"
        print "----- Second Hero -----"
        hero2 = raw_input("please type your hero's name:")
def inquire(): # function for inquiring about a rematch or not
    q = raw_input("Do you want to play another round (Yes or No)?:")
    while q != "Yes" and q != "No": # in case the player typed other than whats between parenthesis
        q = raw_input("Do you want to play another round (Yes or No)?:")
    if q == "No":
        print "Thanks for playing! See you again!"
        quit() # for finishing the code process and ending the game
    elif q == "Yes":
        game() # for starting the game again from the coin toss
# second part: (random start)
def game(): # the main game function starting from coin toss
    option = [hero1, hero2]
    outcome = random.choice(option) # to choose between the two possibilities in the list
    print "coin toss result: ", outcome, "starts first!" # for showing the FIRST player
    hp1 = 100 # initial health points for player1
    hp2 = 100 # initial health points for player 2
    while hp1 > 1 or hp2 > 1: # loop for repeating the game until one of the players' health points become less than 1
        Distinguishing_Factor = 0 # assigning a number to a variable just for distinguishing between hero1 and hero2
        if outcome == hero1: # in case hero1 started first
            print hero1, 55 * " ", hero2
            print "HP[" + str(hp1) + "]:" + (hp1/2)*"|",(4 + (100-hp1)/2) * " ", "HP[" + str(hp2) + "]:" + (hp2/2)*"|"
            print 15 * "-", hero1, "Attacks!!", 15 * "-"
            Distinguishing_Factor +=1 # updating the variable to one (which is hero ONE's assigned number)
            outcome = hero2 # for changing the turn to hero 2
        else:
            print hero2, 55 * " ", hero1
            print "HP[" + str(hp2) + "]:" + (hp2/2)*"|", (4 + (100-hp2)/2) *" ", "HP[" + str(hp1) + "]:" + (hp1/2)*"|"
            print 15 * "-", hero2, "Attacks!!", 15 * "-"
            Distinguishing_Factor += 2 # # updating the variable to two (which is hero TWO's assigned number)
            outcome = hero1 # for changing the turn to hero 1
        m = int(raw_input("choose your attack magnitude between 1 and 50:"))
        while m < 1 or m > 50:  # to correct the magnitude (if more than 50 or less than 1)
            print "The attack magnitude must be between 1 and 50."
            m = int(raw_input("choose your attack magnitude between 1 and 50:"))
        pick = random.randint(0, 100)
        attack_chance = (100 - m)  # success probability
        if Distinguishing_Factor == 1: # in case it was hero ONE's turn
            if attack_chance > pick:# success case
                print hero1, "hits", m, "damage"
                hp2-=m # for subtracting from hero 2
            else: # failing probability
                print "Ooopsy!", hero1, "missed the attack!"
        elif Distinguishing_Factor == 2: # in case it was hero TWO's turn
            if attack_chance > pick: # success
                print hero2, "hits", m, "damage"
                hp1-=m
            else: # failing probability
                print "Ooopsy!", hero2, "missed the attack!"
        if hp1 < 1: # in case of hero2 winning
            print 70 * "#"
            print 30 * "#", hero2, "Wins!!", 30 * "#"
            print 70 * "#"
            inquire() # calling the function of inquiring for a rematch or not
        elif hp2 < 1: # in case of hero1 winning
            print 70 * "#"
            print 30 * "#", hero1, "Wins!!", 30 * "#"
            print 70 * "#"
            inquire() # calling the function of inquiring for a rematch or not

game()














