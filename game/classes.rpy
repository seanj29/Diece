init python:
    import os
    class Actor:
        def __init__(self, name, hp = 20, max_hp = 20, mp = 20, max_mp = 20):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.mp = mp
            self.max_mp = max_mp
            self.state = "None"
            self.damage = 0
            self.Defense = 0
            self.initiative = 0
            self.target = "None"
            self.isOverHealed = False
            self.SpecialState = "None"
            self.DiceisEnabled = {
                "d4" : True,
                "d6" : False,
                "d8" : False,
                "d10" : False,
                "d12" : False,
                "d20" : False,
            }
            
        
        def Attack(self, DiceNo, target = None):
            dice = Dice()
            target = self.target
            original_roll = dice.roll(DiceNo)
            if self.SpecialState == "None":
                self.damage = original_roll
            elif self.SpecialState == "Explode":
                original_roll = dice.autoExplode(DiceNo)
                self.damage = original_roll
                self.SpecialState = "None"
            elif self.SpecialState == "Double Down":
                second_roll = dice.roll(DiceNo)
                self.damage = original_roll + second_roll
                if dice.crit:
                    self.damage += self.CriticallyAttack(DiceNo, dice)
                original_roll = f"{original_roll} on the first and {second_roll} on the second dice"
                self.SpecialState = "None"
            if self.target.state == "Defending" and dice.crit == False:
                self.damage -= self.target.Defense
                if self.damage < 0:
                    self.damage = 0 
            elif dice.crit:
                self.damage += self.CriticallyAttack(DiceNo, dice)
                original_roll = "a Critical Hit"
            self.target.TakeDamage(self.damage)

            return original_roll
            
       
        def CriticallyAttack(self, DiceNo, DiceThatCrit):
            next = DiceThatCrit.getNext(DiceNo)
            while next != None:
                res = DiceThatCrit.roll(next)
                if DiceThatCrit.crit == True:
                    res += self.CriticallyAttack(DiceNo, DiceThatCrit)
                return res
        

        def Target(self, Actor):
            self.target = Actor


        def TakeDamage(self, Damage):
            self.hp -= Damage
            if self.hp < 0:
                self.hp = 0
        #  todo #3 Defending disables dice @seanj29 
        def Defend(self, DiceNo):
            dice = Dice()
            original_roll = dice.roll(DiceNo)
            if self.SpecialState == "None":
                self.Defense = original_roll
            elif self.SpecialState == "Explode":
                original_roll = dice.autoExplode(DiceNo)
                self.Defense = original_roll
                self.SpecialState = "None"
            elif self.SpecialState == "Double Down":
                second_roll = dice.roll(DiceNo)
                self.Defense = original_roll + second_roll
                if dice.crit:
                    self.Heal(second_roll//2, self)
                original_roll = f"{original_roll} on the first and {second_roll} on the second dice"
                self.SpecialState = "None"
            if dice.crit == True:
                self.Heal(original_roll//2, self)
                original_roll = f"A crit and healed {self.Defense//2} damage"
            return original_roll
        
        def DisableDice(self, DiceNo):
            self.DiceisEnabled[DiceNo] = False
    
        def EnableDice(self, DiceNo):
            self.DiceisEnabled[DiceNo] = True

        def Heal (self, amount, Actor):
            Actor.hp += amount
            if Actor.hp > Actor.max_hp:
                Actor.isOverHealed = True
            return amount
        
        def Special(self, SpecialName, EnableDices = None):
            dice = Dice()
            if SpecialName == "Explode":
                self.SpecialState = "Explode"
                self.mp -= 4
            elif SpecialName == "Double Down":
                self.SpecialState = "Double Down"
                self.mp -= 8
            elif SpecialName == "Enable Dice":
                self.EnableDice(EnableDices)
                self.mp -= dice.DiceDict[EnableDices]

        def initialize(self):
            self.hp = self.max_hp 
            self.mp = self.max_mp
            self.state = "None"
            self.damage = 0
            self.Defense = 0
            self.target = "None"
            self.isOverHealed = False
            self.SpecialState = "None"
            self.DiceisEnabled = {
                "d4" : True,
                "d6" : False,
                "d8" : False,
                "d10" : False,
                "d12" : False,
                "d20" : False,
            }










        
        
    
    class Player(Actor):

        def __init__(self):
            player_max_hp = 10
            player_max_mp = 20
            super().__init__("The Guy", player_max_hp, player_max_hp, player_max_mp, player_max_mp)
            self.initiative = 20

        def roll(self, DiceNo):
            if self.state == "Attacking":
                return self.Attack(DiceNo)
            elif self.state == "Defending":
                return self.Defend(DiceNo)
            
            
    
    class Enemy(Actor):
      
        def __init__(self): 
            Enemy_max_hp = 6
            Enemy_max_mp = 10
            super().__init__("Enemy", Enemy_max_hp, Enemy_max_hp, Enemy_max_mp, Enemy_max_mp)
            self.initiative = 1

        def takeTurn(self):
            dice = Dice()
            if dice.roll("d4") == 1:
                self.state = "Defending" 
                self.Defend("d4")    
            else:
                self.state = "Attacking"



    class Anim():

        def __init__(self, AnimName, Actor, frames = 1):
            self.AnimName = AnimName
            self.frames = frames
            self.Actor = Actor
            self.image_dir = f"images/{self.Actor.name}/{self.AnimName}/{self.Actor.name} {self.AnimName}"
            ## Path will need to be changed in shipped .exe binary
            root = os.path.join(os.getcwd(),"../Projects/Diece/game/images", self.Actor.name, self.AnimName)
            self.framesmax = len(os.listdir(root))
            

        def Animate(self, t,st,at):
            if self.frames < self.framesmax:
                self.frames += 1
            else:
                self.frames = 1
            
    
    # class TurnHandler():
    #     def __init__(self, ActorArray):
    #         self.ActorArray = ActorArray

    #     def handle_turn(self, NumberValue):
    #         for Actor in self.ActorArray:
    #             if Actor.name == "Enemy":
    #                     Actor.takeTurn()
           
    #         for Actor in self.ActorArray:                        
    #             if Actor.state == "Defending":
    #                 Actor.Defend(NumberValue)
    #                 if Actor.name == "The Guy":
    #                     narrator("You are defending for [player.Defense] damage")
    #                 else:
    #                     narrator("[enemy.name] defending for [enemy.Defense] damage")

    #         for Actor in self.ActorArray:                
    #             if Actor.state == "Attacking":
    #                 Actor.Attack(NumberValue) 
    #                 if Actor.name == "The Guy":
    #                     narrator("You rolled [result] and did [player.damage] damage to [player.target.name]!")    
    #                 else:
    #                     narrator("You got hit for [enemy.damage] damage??")
                    

    #     def InitInitiative(self):
    #         self.ActorArray.sort(key=lambda Actor: Actor.initiative, reverse = True)

    #     def Add_turn(self, Actor):
    #         self.ActorArray.append(Actor)
    #         self.InitInitiative()
    #     def Remove_turn(self, Actor):
    #         self.ActorArray.remove(Actor)






    player = Player()
    enemy = Enemy()
    # TurnHandler = TurnHandler([player, enemy])
    EnemyIdle = Anim("Idle", enemy, 1)
    TheGuyIdle = Anim("Idle", player, 1)
    EnemyDeath = Anim("Death", enemy, 1)
    TheGuyDeath = Anim("Die", player, 1)
    EnemyAttack = Anim("Attack", enemy, 1)
    TheGuyAttack = Anim("Attack", player, 1)
    EnemyHurt = Anim("Hurt", enemy, 1)
    TheGuyHurt = Anim("Teleport", player, 1)
    EnemyRun = Anim("Run", enemy, 1)
    TheGuyRun = Anim("Run", player, 1)
    TheGuyWalk = Anim("Walk", player, 1)


