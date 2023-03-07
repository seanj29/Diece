init python:
    class Dice:
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(Dice, cls).__new__(cls)
            return cls.instance

        def roll(self, DiceNumber):

            DictDice = {
            "d4" : 4,
            "d6" : 6,
            "d8" : 8,
            "d10" : 10,
            "d12" : 12,
            "d20" : 20,
            }
            return renpy.random.randint(1, DictDice[DiceNumber])


            