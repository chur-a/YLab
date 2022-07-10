from heroes import ChackNorris, SuperHero, Superman
from media import MassMedia
from places import Kostroma, Place, Tokyo


def save_the_place(hero: SuperHero, place: Place, media: MassMedia):
    place.get_anthagonist()
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), MassMedia(TV=True, newspapers=True))
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), MassMedia(planet_coord=[2, 4]))