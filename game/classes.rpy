init python:
    import os

    class Actor:
        def __init__(self, name, hp = 20, max_hp = 20):
            self.name = name
            self.hp = hp
            self.max_hp = max_hp
            self.isDefending = False
            self.damage = 0
            self.Defense = 0
            

        def Attack(self, DiceNo, Actor):
            dice = Dice()
            self.isDefending = False
            self.damage = dice.roll(DiceNo)
            if Actor.isDefending:
                self.damage = self.damage - Actor.Defense    
            if self.damage < 0:
                self.damage = 0
                      
            Actor.TakeDamage(self.damage)
           

        def TakeDamage(self, Damage):
            self.hp -= Damage
            if self.hp < 0:
                self.hp = 0
        
        def Defend(self, DiceNo):
            dice = Dice()
            self.isDefending = True
            self.Defense = dice.roll(DiceNo)


        
        
    
    class Player(Actor):

        def __init__(self):
            player_max_hp = 10
            super().__init__("The Guy", player_max_hp, player_max_hp)
            
            
    
    class Enemy(Actor):
      
        def __init__(self): 
            Enemy_max_hp = 6
            super().__init__("Enemy", Enemy_max_hp, Enemy_max_hp)


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


    player = Player()
    enemy = Enemy()
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


