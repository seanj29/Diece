init python:
    import os

    class Actor:
        def __init__(self, name, hp = 20, max_hp = 20):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.state = "None"
            self.damage = 0
            self.Defense = 0
            self.initiative = 0
            self.target = 0
            

        def Attack(self, DiceNo):
            dice = Dice()
            self.damage = dice.roll(DiceNo)
            if self.target.state == "Defending" and dice.crit == False:
                self.damage = self.damage - self.target.Defense
                if self.damage < 0:
                    self.damage = 0    
            elif dice.crit:
                self.target.TakeDamage(2 * self.damage)
            else:
                self.target.TakeDamage(self.damage)
            return dice.rolled

        def Target(self, Actor):
            self.target = Actor


        def TakeDamage(self, Damage):
            self.hp -= Damage
            if self.hp < 0:
                self.hp = 0
        #  todo #3 Defending disables dice @seanj29
        def Defend(self, DiceNo):
            dice = Dice()
            self.Defense = dice.roll(DiceNo)
            return dice.rolled


        
        
    
    class Player(Actor):

        def __init__(self):
            player_max_hp = 10
            super().__init__("The Guy", player_max_hp, player_max_hp)
            self.initiative = 20

        def roll(self, DiceNo):
            if self.state == "Attacking":
                return self.Attack(DiceNo)
            elif self.state == "Defending":
                return self.Defend(DiceNo)
            
            
    
    class Enemy(Actor):
      
        def __init__(self): 
            Enemy_max_hp = 6
            super().__init__("Enemy", Enemy_max_hp, Enemy_max_hp)
            self.initiative = 1

        def takeTurn(self):
            dice = Dice()
            if dice.roll("d4") > 4:
                self.state = "Defending"     
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


