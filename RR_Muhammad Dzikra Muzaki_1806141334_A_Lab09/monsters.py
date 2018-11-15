import random
'''
Class Monster, defining a monster in general and can be inherited by several other classes
In this Lab, Monster() is the super class of Juggernaut Class, Ghost class, and Robber class.
These classes (juggernaut, ghost, robber) is inheriting all methods and variables defined in its super class.
In this case, they all inherit Monsters' methods and variables.
'''
class Monster():
    def __init__(self, name:str, hp:int, atk:int, arm:int, lvl:int, role:str, imageAsOpponent:list, imageAsTeam:list):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.arm = arm # arm = armor
        self.lvl = lvl
        self.role = role # role = team or opponent (useful in animation)
        self.imageAsTeam = imageAsTeam # You don't need to understand this (useful in animation)
        self.imageAsOpponent = imageAsOpponent # You don't need to understand this (useful in animation)

    '''
    Return the appropriate imageList for the Monster's preferences
    (whether as a team or as an opponent, the List is different)
    '''
    def getImageList(self):
        if self.role == "opponent":
            return self.imageAsOpponent
        elif self.role == "team":
            return self.imageAsTeam

    '''
    Method handling the event of attacking other Monster
    It returns a list [(damage dealt):int, (critical hit or not):int]
    '''
    def attack(self, other):
         attacking = other.attacked(self.atk)
         return attacking

    '''
    Method handling the event of being attacked by other Monster (+decreasing the HP)
    It returns a list [(damage taken):int, (critical hit or not):int]
    ++ determine whether the attack is a critical hit
    '''
    def attacked(self, damage:int):
        critical = random.randint(0,1)
        damage = self.evalDamage(damage, critical) # remember: 0 == False, 1 or > == True
        self.hp -= damage
        return [damage, critical]

    '''
    Method for evaluating damage when attacked
    it returns the damage dealt by attacker to the target
    '''
    def evalDamage(self, damage:int, critical:int):
        if critical: damage = damage - self.arm * 0.2
        else: damage = damage - self.arm
        if(damage < 0): damage = 0
        return int(damage)

    '''
    Method used to check if the monster is alive
    '''
    def isAlive(self):
        alive = True
        if self.hp <= 0: alive = False
        return alive

    '''
    Method for generating status when initiated (grows as level goes up)
    base = the base status
    '''
    def generateStatus(self, base:int, scaler:int, lvl:int):
        return scaler * lvl + base



'''
Class Juggernaut, inheriting all methods and variables from Class Monster above
An offensive type monster, low HP and defense, high damage
'''
class Juggernaut(Monster): # Juggernaut(X) -> X is the class inheriting methods & vars to Juggernaut (you can call it: super class)
    '''
    baseHp = 7, lvlUp -> base + 6*lvl
    baseAtk = 3, lvlUp -> base + 0.6*lvl
    baseArm = 1, lvlUp -> base + 0.25*lvl

    note: for imageAsOpponent and imageAsTeam, You don't need to understand it! It's just me :)
    '''
    def __init__(self, name:str, lvl:int, role:str):
        baseHp, baseAtk, baseArm = 7, 3, 1
        scalerHp, scalerAtk, scalerArm = 6, 0.6, 0.25
        # hp = super().method(...) indicates that hp is equal to return value of method(...) from X(the super class)
        hp = super().generateStatus(baseHp, scalerHp, lvl)
        atk = super().generateStatus(baseAtk, scalerAtk, lvl)
        arm = super().generateStatus(baseArm, scalerArm, lvl)
        imageAsOpponent = ['     ____/|', '    ["____|', '<(*)> | |  ', '  \\ \\ |_|  ', '   \\--|-|   ', '     /.__\\ ', '    |`| |=|', '    |_| |_|']
        imageAsTeam = ['|\\____     ', '|____"]    ', '  | | <(*)>', '  |_|_/ /  ', '  |-|--/   ', ' /__.\\     ', '|=| |`|    ', '|_| |_|    ']
        super().__init__(name, hp, atk, arm, lvl, role, imageAsOpponent, imageAsTeam)

'''
Class Ghost, inheriting all methods and variables from Class Monster above
A defensive type monster, high HP and defense, low damage
'''
class Ghost(Monster):
    '''
    baseHp = 12, lvlUp -> base + 6*lvl
    baseAtk = 1, lvlUp -> base + 0.2*lvl
    baseArm = 4, lvlUp -> base + 0.8*lvl

    note: for imageAsOpponent and imageAsTeam, You don't need to understand it! It's just me :)
    '''
    def __init__(self, name:str, lvl:int, role:str):
        baseHp, baseAtk, baseArm = 12, 1, 4
        scalerHp, scalerAtk, scalerArm = 6, 0.2, 0.8
        hp = super().generateStatus(baseHp, scalerHp, lvl)
        atk = super().generateStatus(baseAtk, scalerAtk, lvl)
        arm = super().generateStatus(baseArm, scalerArm, lvl)
        imageAsOpponent = [' dx._  _.dy', '  : `\\/` : ', ' :  _oo_  :', '  : ~..~  :', ' dy._""_.dz', '    /<>\\   ', ' |e=exp(1)|', ' ==========  ']
        imageAsTeam = imageAsOpponent
        super().__init__(name, hp, atk, arm, lvl, role, imageAsOpponent, imageAsTeam)


'''
Class Robber, inheriting all methods and variables from Class Monster above
An allrounder type monster, medium HP, defense, and attack
TODO: Create the class, you can try making it with the example classes above (Juggernaut and Ghost)

specifications:
    baseHp = 10, lvlUp -> base + 5*lvl
    baseAtk = 2, lvlUp -> base + 0.4*lvl
    baseArm = 2, lvlUp -> base + 0.5*lvl

    imageAsOpponent = ['$$$$$$$$','$$    $$','$$ ^^ $$','$ ~..~ $', '$  __  $', '$      $','$$$$$$$$', '        ']
    imageAsTeam = imageAsOpponent
'''
class Robber(Monster):
    def __init__(self, name:str, lvl:int, role:str):
        baseHp, baseAtk, baseArm = 10, 2, 2
        scalerHp, scalerAtk, scalerArm = 5, 0.4, 0.5
        # hp = super().method(...) indicates that hp is equal to return value of method(...) from X(the super class)
        hp = super().generateStatus(baseHp, scalerHp, lvl)
        atk = super().generateStatus(baseAtk, scalerAtk, lvl)
        arm = super().generateStatus(baseArm, scalerArm, lvl)
        imageAsOpponent = ['$$$$$$$$','$$    $$','$$ ^^ $$','$ ~..~ $', '$  __  $', '$      $','$$$$$$$$', '        ']
        imageAsTeam = imageAsOpponent
        super().__init__(name, hp, atk, arm, lvl, role, imageAsOpponent, imageAsTeam)
