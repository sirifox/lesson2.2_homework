class Farm_animal:
    instances = []
    satiety = 50 # сытость по шкале 0-100
    max_satiety = 100
    character = 'neutral'
    mood = 5 # настроение по шкале 1-10
    condition = 'standing in the pen'


    def __init__(self, weight, name='unnamed'):
        self.instances.append(self)
        self.weight = weight
        self.name = name

    def give_name(self, name):
        self.name = name

    def caress(self):
        if self.condition == 'walking in the yard':
            return 'нельзя погладить животное издалека'
        if mood < 10:
            mood += 1

    def feed(self, points):
        if self.condition == 'walking in the yard':
            return 'нельзя кормить животное издалека'
        self.satiety += points
        if self.satiety >= self.max_satiety:
            self.satiety = self.max_satiety

    def call_anim(self, name):
        if self.name == 'unnamed':
            return 'у животного нет имени, назовите его'
        if name == self.name:
            condition = 'standing in the pen'
        return self.sound

class Birds(Farm_animal):
    def eggs_farming(self):
        if self.satiety >= 30:
            self.satiety /= 2
            return 'eggs!'
        else:
            return 'you need to feed'

class Milky(Farm_animal):
    def milk_farming(self):
        if self.satiety >= 30:
            self.satiety /= 2
            return 'miiilk!'
        else:
            return 'you need to feed'

class Goose(Birds):
    character = 'angry'
    sound = 'gaga'


class Chicken(Birds):
    sound = 'coco'


class Duck(Birds):
    character = 'good'
    sound = 'crya-crya'


class Cow(Milky):
    sound = 'mu-mu'


class Sheep(Farm_animal):
    sound = 'me-me'

    def wool_farming(self):
        if self.satiety >= 30:
            self.satiety /= 2
            return 'wool'
        else:
            return 'you need to feed'

class Goat(Milky):
    sound = 'be-be'


goose_one = Goose(10, 'Серый')
goose_two = Goose(12, 'Белый')
cow_one = Cow(1000, 'Манька')
sheep_one = Sheep(50, 'Барашек')
sheep_two = Sheep(60, 'Кудрявый')
chicken_one = Chicken(6, 'Ко-Ко')
chicken_two = Chicken(7, 'Кукареку')
goat_one = Goat(35, 'Рога')
goat_two = Goat(45, 'Копыта')
duck_one = Duck(9, 'Кряква')

max_weight = 0
total_weight = 0
for instant in Farm_animal.instances:
    total_weight += instant.weight
    if instant.weight > max_weight:
        max_weight = instant.weight
        heavyweight = instant.name
print('Вес всех животных равен {}'.format(str(total_weight)))
print('Кличка самого тяжёлого животного - {}'.format(heavyweight))

