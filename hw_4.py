from random import randint, choice
# VU

class GameEntity:
    def __init__(self, name, health, damage, ):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__max_health = health

    @property
    # функция для ведьмака, возвращает ее когда ведьмак использует свою способность
    def max_health(self):
        return self.__max_health

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != 'BLOCK_DAMAGE_AND_REVERT':
                    blocked = randint(1, 2) * 5  # 5, 10
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def choose_defence(self, heroes):
        random_hero: Hero = choice(heroes)
        self.__defence = random_hero.ability

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def hit(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности CRITICAL_DAMAGE
        random_coefficient = randint(2, 5)  # 2,3,4,5
        boss.health -= self.damage * random_coefficient
        print(f'Warrior {self.name} hit critically {self.damage * random_coefficient}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности BOOST
        random_boost = randint(2, 5)
        for hero in heroes:
            if (hero.health > 0):
                hero.damage = hero.damage + random_boost
        print(f"{self.name} BOOST OUR TEMMATES! ")


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности BLOCK_DAMAGE_AND_REVERT
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} to boss.')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности HEAL
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REBORNE')

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности REBORNE
        for hero in heroes:
            if hero.health <= 0 and self != hero:
                hero.health += hero.max_health
                self.health = 0
                print(f"Wither has dead and reborn {hero.name}")
                break


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'HACKING')

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0 or round_number == 0:  # для того чтобы функция работала через раунд
            # здесь будет реализация способности HACKING
            random_hack = randint(20, 70)
            random_hero = choice(heroes)
            boss.health -= random_hack
            if random_hero.health > 0 and self != random_hero:
                random_hero.health += random_hack
                print(f"{self.name} revert {random_hack} health to {random_hero.name} ")


class Bomber(Hero):
    boom = True

    def __init__(self, name, health, damage, ):
        super().__init__(name, health, damage, 'BOOOM')

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности BOOM
        if self.health == 0:
            boss.health -= 10000
            print('BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM')


class Reaper(Hero):
    def __init__(self, name, health, damage, ):
        super().__init__(name, health, damage, 'LAST CHANGE')

    def apply_super_power(self, boss, heroes):
        # здесь будет реализация способности LAST CHANGE
        if self.health < self.max_health // 100 * 30:
            self.damage = self.damage * 2
        if self.health < self.max_health // 100 * 15:
            self.damage = self.damage * 3


class Gamer(Hero):
    def __init__(self, name, health, damage, ):
        super().__init__(name, health, damage, 'ALL OR NOTHING')

    # здесь будет реализация способности ALL OR NOTHING
    def apply_super_power(self, boss, heroes):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        random_hero = choice(heroes)
        if dice1 == dice2:
            boss.health -= dice1 * dice2
            print("BINGO!!!")
        else:
            random_hero.health -= dice1 + dice2
            print("Oh, sorry guy")


# global variable
round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes):
    print(f'ROUND - {round_number} ----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
        elif (type(hero) == Bomber and hero.health == 0 and boss.health > 0 and
              hero.ability != boss.defence and Bomber.boom == True):
            Bomber.boom = False
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Diablo', 2500, 50)
    warrior_1 = Warrior('Rubi', 280, 10)
    warrior_2 = Warrior('Reksar', 270, 15)
    magic = Magic('Hendolf', 290, 10)
    berserk = Berserk('Guts', 260, 5)
    doc = Medic('Jojo', 200, 5, 15)
    assistant = Medic('Lily', 300, 5, 5)
    witcher = Witcher("Gerald", 500, 0)
    hacker = Hacker("Nathanos", 270, 10)
    bomber = Bomber("Gazz", 290, 10)
    reaper = Reaper("Margik", 300, 20)
    gamer = Gamer("Masker",310, 10)
    heroes_list = [warrior_1, warrior_2, doc, magic, berserk, assistant, witcher, hacker,
                   bomber, reaper, gamer]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()