print("Задание 1")

'''
Задание 1
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: 
красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, 
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. 
При его нарушении выводить соответствующее сообщение и завершать скрипт.
'''

from time import sleep


class TrafficLight:
    __states = {'красный': 7, 'желтый': 2, 'зеленый': 3}
    __color = ''

    def running(self):
        for color, sw_time in self.__states.items():
            self.__color = color

            print(f"Режим '{self.__color}' "
                  f" на {sw_time} секунд")
            sleep(sw_time)


tl = TrafficLight()
tl.running()

print("Задание 2")

'''
Задание 2
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        int = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Масса асфальта, необходимого для покрытия дороги {int} т.')


weight = Road(20, 5000)
weight.intake()

print("Задание 3")

'''
Задание 3
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса 
Position, передать данные, проверить значения атрибутов, вызвать методы 
экземпляров.
'''


class Worker:

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_full_profit(self):
        print(f'Доход {sum(self._income.values())}')


manager = Position('Petr', 'Petrov', 'manager', 500, 100)

manager.get_full_name()
manager.get_full_profit()

print("Задание 4")

'''
Задание 4
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police 
(булево). А также методы: go, stop, turn(direction), которые должны сообщать,
 что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую 
скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении 
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о 
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ 
к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''


class Cars:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return "Машина едет"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return "Машина повернула на " + direction

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')


class TownCar(Cars):
    family = None

    def __init__(self, name, speed, color, family=True):
        super().__init__(name, speed, color)
        self.family = family

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на  {self.speed - 60} км/ч')
        else:
            print(f'Скорость машины {self.speed} км/ч')


class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на  {self.speed - 40} км/ч')
        else:
            print(f'Скорость машины {self.speed} км/ч')


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)


ford = TownCar('Ford', 160, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('лево'), ford.stop(), ford.show_speed())
sport = SportCar('Ford', 180, 'red')
print(sport.go(), sport.turn('право'), sport.stop(), sport.show_speed())
work = WorkCar('Ford', 90, 'white', True)
print(work.go(), work.turn('город'), work.stop(), work.show_speed())
police = PoliceCar('Ford', 180, 'red')

print("Задание 5")

'''
Задание 5
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), 
Handle (маркер);
в каждом классе реализовать переопределение метода draw. 
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод 
для каждого экземпляра.
'''

class Stationery:
    atr_title = 'Title'
    def draw(self):
        print('Запуск отрисовки.')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
