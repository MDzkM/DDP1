from monsters import *
import sys, time, os
'''
Class for creating animation

You don't need to change anything here, just understand how to initiate this class.
The Hp wont update when attacking, please understand that I created it in < a day.
'''
class Animation():
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def renderAttackMove(self, monster:Monster, size = 20):
        playerImage = self.player.getImageList()
        opponentImage = self.opponent.getImageList()
        image = "  HP: " + str(self.player.hp) + " " *(34-len(str(self.player.hp))) + "HP: " + str(self.opponent.hp) + "\n"
        if monster == self.player:
            for x in range(len(playerImage)):
                image += (" " * size + playerImage[x] + " " * (25-size) + opponentImage[x] + "\n")
        elif monster == self.opponent:
            for x in range(len(opponentImage)):
                image += (playerImage[x] + " " * (25-size) + opponentImage[x] + "\n")
        image += self.player.name + " " *(39-len(str(self.player.name))) + self.opponent.name + "\n"
        return image


    def showFigure(self, monster:Monster, channel=sys.stdout):
        '''
        method showing the figure of monster in @param:monster.
        '''
        os.system('cls||clear')
        imageList = monster.getImageList()
        image = "====" + monster.name + "====\n"
        for i in range(len(imageList)):
            image += imageList[i] + "\n"
        image += "\n====" + monster.name + "===="
        channel.write(image + '\r')
        channel.flush()
        time.sleep(2)


    def animateAttack(self, monster:Monster, channel=sys.stdout, waitTime=0.35):
        '''
        method to animate the attack action of monster in @param:monster
        '''
        time.sleep(waitTime*3)
        os.system('cls||clear')
        animation = self.renderAttackMove(monster, size=0)
        channel.write(animation + '\r')
        channel.flush()
        time.sleep(waitTime)

        os.system('cls||clear')
        animation = self.renderAttackMove(monster, size=20)
        channel.write(animation + '\r')
        channel.flush()
        time.sleep(waitTime)

    def animateMoveBack(self, monster:Monster, channel=sys.stdout, waitTime=0.35):
        '''
        method to animate the after-attack action of monster in @param:monster
        This method animate the move-back action after attacking
        '''
        time.sleep(waitTime*3)
        os.system('cls||clear')
        animation = self.renderAttackMove(monster, size=0)
        channel.write(animation + '\r')
        channel.flush()
        time.sleep(waitTime)

'''
You can test this code:
1. in the directory you saved all the lab files, open your command prompt (terminal or cmd or whatever)
2. try running this "animation.py", for example by typing:

python amination.py

3. You can enjoy some funny things I designed for hours :')

'''
if __name__ == "__main__":
    pet = Juggernaut(name="PET", lvl=0, role="team")
    opp = Juggernaut(name="OPPONENT", lvl=0, role="opponent")
    x = Animation(pet, opp)
    x.showFigure(pet)
    x.showFigure(opp)
    x.animateAttack(pet)
    x.animateMoveBack(pet)
