from abc import ABC, abstractmethod


class Place(ABC):
    name = 'Place'
    
    @abstractmethod
    def get_anthagonist(self):
        pass


class Kostroma(Place):
    name = 'Кострома'
    
    def get_anthagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Токио'

    def get_anthagonist(self):
        print('Godzilla stands near a skyscraper')

        