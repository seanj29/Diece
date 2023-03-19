init python:
    class Dice:
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Dice, cls).__new__(cls)
            return cls.instance
        def __init__(self):
            self.DictDice = {
            "d4" : 4,
            "d6" : 6,
            "d8" : 8,
            "d10" : 10,
            "d12" : 12,
            "d20" : 20,
            }
            self.rolled = 0
            self.randbagUsed = False
            self.crit = False;
        def roll(self, DiceNumber):
            randbag = RandomBags()
            if self.randbagUsed:
                self.rolled = renpy.random.choice(randbag.returnBag(DiceNumber))
                randbag.remove(self.rolled)
            else:
                self.rolled = renpy.random.randint(1, self.DictDice[DiceNumber])
                
            if self.rolled == self.DictDice[DiceNumber]:
                self.crit = True
            else:
                self.crit = False
            return self.rolled
        
        def getNext(self, DiceNumber):
            tempD = iter(self.DictDice)
            for key in tempD:
                if key == DiceNumber:
                    return next(tempD, 0)
                else:
                    return None


    class RandomBags:
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(RandomBags, cls).__new__(cls)
            return cls.instance
        def __init__(self):
            self.BagDice = {
            4 : 0,
            6 : 1,
            8 : 2,
            10 : 3,
            12 : 4,
            20 : 5,
            }
            self.bags = []
            self.lastbag = []
            for key in self.BagDice:
                self.bags.insert(self.BagDice[key],2 * list(range(1, (key+1))))

        def returnBag(self, DiceNumber):
            self.isEmpty(DiceNumber)
            self.lastbag = self.bags[self.BagDice[DiceNumber]]
            return self.lastbag
            

        def remove(self, toRemove):
            self.lastbag.remove(toRemove)

        def isEmpty(self, DiceNumber):
            for bag in self.bags:
                if not self.bags[self.BagDice[DiceNumber]]:
                    self.bags.insert(self.BagDice[DiceNumber],2 * list(range(1, (DiceNumber+1))))


            





            