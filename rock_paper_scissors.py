# Project Title: Rock, Paper, Scissors

rockpaperscissor = """

██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                    
"""
scissor = """
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
"""
paper = """
            ___..__
____..--'''' ._ __.'
              "-..__
            '"--..__";
____        '--...__"";
    `-..__ '"---..._;"
          ''''----

"""

rock = """

       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""

GAMEOVER = """
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                       
"""

LOADINGNEWGAME = """

 _   __   __  __  _ __  _  __   __  _ ___  _   _    __  __  __ __ ___  
| | /__\ /  \| _\| |  \| |/ _] |  \| | __|| | | |  / _]/  \|  V  | __| 
| || \/ | /\ | v | | | ' | [/\ | | ' | _| | 'V' | | [/\ /\ | \_/ | _|  
|___\__/|_||_|__/|_|_|\__|\__/ |_|\__|___|!_/ \_!  \__/_||_|_| |_|___| 
 """  

WIN = """
    ██╗    ██╗██╗███╗   ██╗
    ██║    ██║██║████╗  ██║
    ██║ █╗ ██║██║██╔██╗ ██║
    ██║███╗██║██║██║╚██╗██║
    ╚███╔███╔╝██║██║ ╚████║

"""

LOSE = """
    ██╗     ██████╗ ██████ ████████╗
    ██║    ██╔═══██ ██╔════██ ╔════╝
    ██║    ██║   ██ ██████ ██████╗  
    ██║    ██║   ██╚════██ ██ ╔══╝  
    ███████╚██████ ╔██████ ████████
"""                                                                                       

TIE = """

    ██████╗ ██████╗  █████╗ ██╗    ██╗
    ██╔══██╗██╔══██╗██╔══██╗██║    ██║
    ██║  ██║██████╔╝███████║██║ █╗ ██║
    ██║  ██║██╔══██╗██╔══██║██║███╗██║
    ██████╔╝██║  ██║██║  ██║╚███╔███╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝

"""
VS = """
   
     ▌ ▐·.▄▄ · 
    ▪█·█▌▐█ ▀. 
    ▐█▐█•▄▀▀▀█▄
     ███ ▐█▄▪▐█
    . ▀   ▀▀▀▀ 

 """

###################
               
import random 
import time  
                
##################
print()
print(rockpaperscissor)
print("- - " * 36)
print()


# Game setup:  
INSTRUCTIONS = """
    Please choose one of the following:
    >>> [R]ock  
    >>> [P]aper
    >>> [S]cissors

    Best out of three wins.
    Are you ready?!
    """
    

def greeting():
    """Greets player, returns username"""
    
    print("Challenger, please enter your name: ")
    username = input("> ")
    print()
   
    username = username.title()
    print("Welcome,  " + username + " !")
   
    print()
    print(INSTRUCTIONS)
    return username



def player_choice():
    """Aks for user's choice and returns it """
   
    user_choice = input("> ")
    user_choice = user_choice.title()
    
    print()

    return user_choice


def print_player_choice(user_choice, rounds):
    """prints player choice"""
   
    if user_choice == "R" or user_choice.startswith("R"):
        user_choice = "Rock"
        print("="*15)
        print(" R O U N D :", rounds)
        print("="*15)
        print()
        print("Player:")
        print(rock)
       
        

    elif user_choice == "P" or user_choice.startswith("P"):
        user_choice = "Paper"
        print("="*15)
        print(" R O U N D :", rounds)
        print("="*15)
        print()
        print("Player:")
        print(paper)
        
        
    elif user_choice == "S" or user_choice.startswith("S"):
        user_choice = "Scissor"
        print("="*15)
        print(" R O U N D :", rounds)
        print("="*15)
        print()
        print("Player:")
        print(scissor)
       
    
    else:
        print("Invalid response")
        
            

def computer_choice():
    """computer's choice"""
    
    comp_choice = random.choice(rps)
    return comp_choice



def print_computer_choice(user_choice, comp_choice):
    print()
    if not (user_choice.startswith("R") or user_choice.startswith("P") or user_choice.startswith("S")):
        print()
        
    elif comp_choice.startswith("R"):
        print("Computer:")
        print(rock)
   
    elif comp_choice.startswith("P"):
        print("Computer:")
        print(paper)
   
    elif comp_choice.startswith("S"):
        print("Computer:")
        print(scissor)

    


def versus(user_choice):
    """DISPLAYS VERSUS"""
    if not (user_choice.startswith("R") or user_choice.startswith("P") or user_choice.startswith("S")):
        print()
    
    else: 
        print()
        print(VS)
        print()
        print()



# def inc_score(current_score):
#     """Returns updated score increased each win"""

#     current_score = current_score + 1
#     return current_score




def display_win():
    """Displays win statements"""
    win = ["You WIN!", "W I N N E R", "Winner winner chicken dinner!, Genius!"]
    print(random.choice(win))
    print(WIN)

def display_draw():
    """displays draw statements"""
    print("It's a draw!")
    print(TIE)

def display_lose():
    """Displays lose statements"""
    lose = ["You LOSE!", "L O S E R ", "Better luck next time."]
    print(random.choice(lose))
    print(LOSE)


# SCORE/POINTS SYSTEM 
# def display_scores(user_score, comp_score):
#     """ Displays user/comp scores"""
#     print()
#     print("Player score:", user_score)
#     print("Computer:", comp_score)



def rps_scoring(user_choice, comp_choice):
    """Keeps track of score """

    # DRAW
    if user_choice == "S" and comp_choice =="Scissors":
       display_draw()
      
    # Scissors > Paper : WIN
    elif user_choice == "S" and comp_choice == "Paper":
        display_win()

    # Scissors < Rock : LOSE
    elif user_choice == "S" and comp_choice == "Rock":
        display_lose()
        

       
  
    # DRAW
    elif user_choice == "P" and comp_choice == "Paper":
        display_draw()
        
    # Paper > Rock : WIN
    elif user_choice == "P" and comp_choice =="Rock":
        display_win()
           
    # Paper < Scissors : LOSE
    elif user_choice == "P" and comp_choice == "Scissors":
        display_lose()
       

        
    # DRAW
    elif user_choice =="R" and comp_choice =="Rock":
        display_draw()

    # Rock < Paper : LOSE    
    elif user_choice =="R" and comp_choice =="Paper":
        display_lose()   
    
    # Rock > Scissors : WIN 
    elif user_choice =="R" and comp_choice =="Scissors":
        display_win()



def play_again(username, rounds):
    """Takes player input to decide whether or not to restart or quit game"""

    # GAME OVER
    print()
    print("- - " * 36)
    print()
    print(GAMEOVER)
    print()

    while True:
        # ask player if they want to play again after three rounds
        print("Play again? [ Yes / No ]")

        play_again = input(">> ")
        play_again = play_again.title()

        # to play again
        if play_again.startswith("Y"):
            print()
            print(LOADINGNEWGAME)
            print()
            time.sleep(1)
            print("             .")
            time.sleep(1)
            print("            . .")
            time.sleep(1)
            print("          . . . . ")
            time.sleep(1)
            print("       ...loading...")
            time.sleep(1)
            print("          . . . . ")
            time.sleep(1)
            print("            . . ")
            time.sleep(1)
            print("             .")
            time.sleep(1)
            
            # restarts the main_loop (the game)
            main_loop(username,rounds)

        # to quit game
        elif play_again.startswith("N"):
            print("Goodbye", username, "!")
            break
        
        else:
            print("Sorry, I didn't understand that.")
            print()
            print()
            print()
            
    

def main_loop(username, rounds):
    """ Game loop """

    # user_score = 0
    # comp_score = 0
    # rounds = 1

    # repeat game for three rounds
    while rounds <=3:
        print()
        print()
        print("Rock, paper or scissors?")
        
        # asks for user's input & display it
        user_choice = player_choice()
        print("//" * 30)
        print()
        
        print_player_choice(user_choice, rounds)
        
        # display vs.
        versus(user_choice)

        # computer's choice via RNG & displays it
        comp_choice = computer_choice()
        print_computer_choice(user_choice, comp_choice)
        print("\\" * 60)
        print()
        # displays win/lose
        rps_scoring(user_choice, comp_choice)
       

        # valid input from user will increase counter by one
        if (user_choice.startswith("R") or user_choice.startswith("S") or user_choice.startswith("P")) and (comp_choice.startswith("R") or comp_choice.startswith("S") or comp_choice.startswith("P")):
            rounds +=1

  
               
rps = ["Rock", "Paper", "Scissors"]

def play_game():
    """Starts the game"""
    
    rounds = 1

    # greeting
    username = greeting()

    # main game loop - 3 rounds
    main_loop(username, rounds)

    # asks player if they want to play again or quit game
    play_again(username, rounds)
               
play_game()        


        



    
