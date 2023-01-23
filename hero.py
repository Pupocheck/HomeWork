class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points = self.health_points * 2

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Inokenti", "Traktorist", "say trista", 300,
                 "Otsosi y Traktorista.")

print(hero.get_name())
hero.double_health()
print(hero.health_points)
print(str(hero))
print(len(hero))


########Дз второго урока

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase,
                 damage=0, fly=False):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = fly

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def fly_phrase(self):
        if self.fly:
            print("I can fly!")


class AerialHero(SuperHero):
    element = "air"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


class EarthHero(SuperHero):
    element = "earth"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


class SpaceHero(SuperHero):
    element = "space"

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


aerial_hero = AerialHero("Горящая Жопа", "Йоба", "Реактивная тяга", 100,
                         "А ПОЧЕМУ ОН, А НЕ Я!!!")
earth_hero = EarthHero("BossOfTheGym", "Billy Herrington", "Fisting ass",
                       300,
                       "Fucking slaves")
space_hero = SpaceHero("Иван", "Сын Маминой Подруги", "Успешный успех", 999,
                       "Все как у людей")

print(aerial_hero.element)
print(earth_hero.element)
print(space_hero.element)

aerial_hero.double_health()
print(aerial_hero.health_points)
aerial_hero.fly_phrase()  # "

class Villain(SuperHero):
    people = "monsters"

    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2


villain = Villain("Batya", "Отец сыча", "Magic Pizdulina", 200,
                  "А ну пшел на улицу, НЕ ЧЕ В КУДАХТАРЕ СИДЕТЬ")
print(villain.people)
villain.crit()
print(villain.damage)
