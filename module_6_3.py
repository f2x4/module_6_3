import random


class Animal:
    """ Класс описывающий животных"""
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        """ Изменяет соответствующие координаты в _cords на dx, dy и dz в том же порядке,
        где множителем будет являться speed. Если при попытке изменения координаты z в
        _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" ,
        при этом изменения не вносятся. """
        if dz < 0:
            print("It's too deep, i can't dive :(")
            return self._cords
        else:
            new_cords = []
            *cords, = dx, dy, dz,
            for i in range(0, len(cords)):
                new_cords.append(self._cords[i] + cords[i] * self.speed)
            self._cords = new_cords

    def get_cords(self):
        """ Выводит координаты """
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    def attack(self):
        """ Выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5
        и "Be careful, i'm attacking you 0_0" , если равно или больше. """
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    """ Птицы """
    beak = True
    def lay_eggs(self):
        """ Выводит строку 'Here are(is) <случайное число от 1 до 4> eggs for you' """
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    """ Водные животные """
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        """ Должен изменять в отрицательную сторону координату z уменьшенную в 2
        раза с учётом скорости. """
        self._cords[2] = self._cords[2] - abs(self.speed * (dz / 2))


class PoisonousAnimal(Animal):
    """ Ядовитые животные """
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    """ Утконос """
    sound = 'Click-click-click'
    def speak(self):
        """ Выводит на консоль атрибут sound """
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()