class Warrior:
    def __init__(self,name, strength, hp):
        self.name = name
        self.strength = strength
        self.hp = hp

    def info(self):
        print(f'name: {self.name}')
        print(f'strength: {self.strength}')
        print(f'hp: {self.hp}')