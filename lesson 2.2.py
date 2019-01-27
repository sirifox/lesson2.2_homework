class FarmAnimal:

    instances = []
    satiety = 10 # сытость по шкале 0-100
    max_satiety = 100
    condition = 'walking in the yard'

    def __init__(self, weight, name='unnamed'):
        self.instances.append(self)
        self.weight = weight
        self.name = name

    def give_name(self, name):
        self.name = name

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
            self.condition = 'standing in the pen'
        return self.sound

    def collect(self):
        pass


class Bird(FarmAnimal):

    def collect(self):
        super().collect()
        if self.satiety >= 30:
            self.satiety /= 2
            return 'eggs!'
        if self.satiety < 30:
            return 'you need to feed'


class Milk(FarmAnimal):

    def collect(self):
        super().collect()
        if self.satiety >= 30:
            self.satiety /= 2
            return 'milk!'
        if self.satiety < 30:
            return 'you need to feed'


class Goose(Bird):

    sound = 'gaga'


class Chicken(Bird):

    sound = 'coco'


class Duck(Bird):

    sound = 'crya-crya'


class Cow(Milk):

    sound = 'mu-mu'


class Sheep(FarmAnimal):

    sound = 'me-me'

    def collect(self):
        super().collect()
        if self.satiety >= 30:
            self.satiety /= 2
            return 'wool!'
        if self.satiety < 30:
            return 'you need to feed'


class Goat(Milk):

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

for instance in FarmAnimal.instances:
    print(instance.call_anim(instance.name))
    instance.feed(40)
    print(instance.collect())
    total_weight += instance.weight
    if instance.weight > max_weight:
        max_weight = instance.weight
        heavyweight = instance.name

print('Вес всех животных равен {}'.format(str(total_weight)))
print('Кличка самого тяжёлого животного - {}'.format(heavyweight))

