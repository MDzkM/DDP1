from animation import *
from monsters import *
from customException import *
import random

class Main():
    def __init__(self):
        try:
            player_name = input("Hey, gimme yer name (A-Z, a-z): ")
            age = input("Now tell me, how many years you live in Earth (int): ")
            pet_name = input("I wanna give u a pet, name it (A-Za-z): ")
            opp_name = input("Whats the thing u hate most, name it (A-Za-z): ")

            if not(player_name.isalpha() and pet_name.isalpha() and age.isnumeric() and opp_name.isalpha()):
                raise InvalidInputError

            monster = random.randint(0,1)
            pet = None
            opponent = None

            '''
            Initiate the class, make a new Object of the class, given that:
            age = your pet level (age from input)
            pet_name = your pet name (pet_name from input)
            '''
            # Choosing the monster for player and opponent
            if monster == 0:
                pet = Ghost(pet_name, int(age), 'team')
                # Randomizing the opponent's monster
                opponent_monster = random.randint(0,1)
                if opponent_monster == 0:
                    opponent = Juggernaut(opp_name, int(age), 'opponent')
                else:
                    opponent = Robber(opp_name, int(age), 'opponent')
                '''
                clue:
                monster = random.randInt(0,2)
                if monster == 0:
                else:
                '''
            else:
                pet = Juggernaut(pet_name, int(age), 'team')
                # Randomizing the opponent's monster
                opponent_monster = random.randint(0,1)
                if opponent_monster == 0:
                    opponent = Ghost(opp_name, int(age), 'opponent')
                else:
                    opponent = Robber(opp_name, int(age), 'opponent')


            print("WARNING!!!\nYou are about to enter the arena, " + player_name + "!")
            print('''
            =============================================
                        WELCOME TO THE ARENA!
            =============================================\n
            ''')

            # Starting the battle animation
            animation = Animation(pet, opponent)

            # Showing the player and opponent's pet
            animation.showFigure(pet)
            animation.showFigure(opponent)

            #Executing battle until either one dies
            while(pet.isAlive() and opponent.isAlive()):

                # Move pet forward to attack
                animation.animateAttack(pet)

                # Storing damage value and critical status
                damage, critical = pet.attack(opponent)

                # Prints critical message on critical hit
                if critical == 1:
                    print("{} got a critical attack on {}".format(pet.name, opponent.name))

                # Print damage dealt status
                print("{} dealt {} damage to {}".format(pet.name, int(damage) , opponent.name))

                # Move pet backward after attack
                animation.animateMoveBack(pet)

                # Ends battle if opponent is already dead
                if opponent.isAlive() == False:
                    break

                # Move opponent forward to attack
                animation.animateAttack(opponent)

                # Storing damage value and critical status
                damage, critical = opponent.attack(pet)

                # Prints critical message on critical status
                if critical == 1:
                    print("{} got a critical attack on {}".format(opponent.name, pet.name))

                # Prints damage dealt status
                print("{} dealt {} damage to {}".format(opponent.name, int(damage), pet.name))

                # Move opponent backward after attack
                animation.animateMoveBack(opponent)
                '''
                CLUE: read thoroughly class animation and class monsters, understand it, and use it!

                this is important, READ and UNDERSTAND both Animation dan Monsters class!
                and ONLY after that do this part!
                '''


            if pet.isAlive():
                print("Well done, " + player_name + " together with " + pet_name + ", You dominate the arena!")
                print("Congratulations on winning!")
            else:
                print("Well, what a noob you are!")
                print("Get out of my way!")


        except InvalidInputError:
            print("You entered wrong input!")







if __name__ == "__main__":
    Main()
