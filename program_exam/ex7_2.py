import random


class Warrior:
    def __init__(self,name, strength, hp):
        self.__name = name
        self.__strength = strength
        self.__hp = hp
        self.__luc = random.Random()

    @property
    def name(self):
        return self.__name

    @property
    def strength(self):
        return self.__strength

    @property
    def hp(self):
        return self.__hp

    @strength.setter
    def strength(self,strength):
        if strength == '':
            raise ValueError('strength is empty')
        self.__strength = strength

    @hp.setter
    def hp(self,hp):
        self.__hp = hp

    @property
    def luc(self):
        return self.__luc

    @luc.setter
    def luc(self,luc):
        self.__luc = luc

    def info(self):
        print(f'name: {self.__name}')
        print(f'strength: {self.__strength}')
        print(f'hp: {self.__hp}')
        print(f'luc; {self.__luc}')