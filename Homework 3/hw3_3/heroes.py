from abc import ABC, abstractmethod
import weapons as wp


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    @abstractmethod
    def attack(self):
        pass


class Superman(SuperHero, wp.LazerMixin):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        print('Kick')
        
    def ultimate(self):
        self.incinerate_with_lasers()


class ChackNorris(SuperHero, wp.GunMixin):
    
    def __init__(self):
        super(ChackNorris, self).__init__('Chack Norris', False)
        
    def attack(self):
        self.fire_a_gun()
        
    