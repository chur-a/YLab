from typing import List


class MassMedia:
    
    def __init__(self, TV=False, newspapers=False, planet_coord: List[float] = None):
        self.TV = TV
        self.newspapers = newspapers
        self.planet_coord = planet_coord
    
    def create_news(self, hero, place):
        if self.TV:
            self.tv_news()
        if self.newspapers:
            self.newspapers_news(hero, place)
        self.simple_news(hero, place)
        if self.planet_coord:
            self.message_to_planet(hero, place, self.planet_coord)
        
    def tv_news(self):
        print("Владимир Путин спас нашу планету. Жители Земли ему благодарны."
              " Это новости на канале Россия, меня зовут Дмитрий Киселёв, главное к этому часу...")
        
    def newspapers_news(self, hero, place):
        print(f"TheGuardian: Victory!{hero.name} saved the {place.name}",
              f"New York Times: Unbelievable. {hero.name} did it. World is thankful to him.", sep='\n')
    
    def simple_news(self, hero, place):
        print(f'{hero.name} saved the {place.name}!')
        
    def message_to_planet(self, hero, place, planet_coord):
        print(f"Message to the planet with coordinates: {planet_coord}. {hero.name} saved the {place.name}! "
              "It's time to celebrate")
    
    
    