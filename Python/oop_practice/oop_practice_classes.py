""""best module for oop practice"""
from abc import ABC, abstractmethod


class Engine(ABC):
    """Engine abstract class"""
    engine = 'v6'

    @abstractmethod
    def set_engine(self, engine):
        """set engine in machine"""

    def has_engine(self, obj, engine):
        """verify engine existance"""
        self.engine = engine
        if obj.engine:
            return engine
        return None


class Transport:
    """superclass transport"""
    _transport_machines = 0

    def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str):
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.surf_type_support = surf_type_support
        self._color = None
        Transport._transport_machines += 1
        print("Transport __init__ method was called")

    @classmethod
    def amount_machines(cls):
        """calculate machines"""
        print(cls._transport_machines)

    @property
    def color(self):
        """color of transport"""
        if not self._color:
            self._color = 'white'
        return self._color

    @color.setter
    def color(self, new_color):
        if self.color != new_color and self.c_list(new_color):  # new_color in self.color_list:
            self._color = new_color

    @staticmethod
    def c_list(curr_clr):
        """verify right color"""
        color_list = ['black', 'yellow', 'red']
        return curr_clr in color_list


class Car(Transport, Engine):
    """Car class"""
    def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str):
        Transport.__init__(self, max_capacity, max_speed, surf_type_support)
        print("I am Car.__init__")
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

    def __rpow__(self, x_val):
        print('behavior was changed!')

    def __contains__(self, item):
        return False

    def __hash__(self):
        return 1

    def __len__(self):
        return 69

    def __neg__(self):
        print("Behavior was changed!")


class Bycicle(Transport, Engine):
    """best byciles"""
    def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str):
        super().__init__(max_capacity, max_speed, surf_type_support)
        self._wheels_amount = None
        self.engine = None

    @property
    def wheels_num(self):
        """amount of wheels somewhere inside machine"""
        if not self._wheels_amount:
            self._wheels_amount = 4
        return self._wheels_amount

    def set_engine(self, engine):
        self.engine = engine


class TransportSubmarine(Transport, Engine):
    """very rare water transport"""
    def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str, i_depth: float):
        Transport.__init__(self, max_capacity, max_speed, surf_type_support)
        self.i_depth = i_depth
        self.engine = None

    def going_depth(self, depth: float):
        """call when we going deep"""
        self.i_depth = depth
        print("We are goin on: ", self.i_depth)

    def set_engine(self, engine):
        self.engine = engine


class Wunderwaffle(Car, TransportSubmarine):
    """mad creation made by mad scientist"""

    def __init__(self, max_capacity, max_speed, surf_type_support, i_depth):
        Car.__init__(self, max_capacity, max_speed, surf_type_support)
        TransportSubmarine.__init__(self, max_capacity, max_speed, surf_type_support, i_depth)

    def going_depth(self, depth: float):
        print('We are allready in:', depth)


# - использовать декораторы @staticmethod, @classmethod, @property
# @classmethod use example


Transport(10, 20, 'Undefined')
Transport(10, 20, 'Undefined')
Transport(10, 20, 'Undefined')

Transport.amount_machines()

# @property use example as setter/validator
a = Transport(12, 22, 'Undefined')
print(a.color)
a.color = 'blackestblackoftheblackestnight'
print(a.color)
a.color = 'yellow'  # aviable in list
print(a.color)

# @staticmethod : boolean
print(a.c_list('black'))
#  return True
print(a.c_list('blackestblackoftheblackestnight'))
#  return True

# - использовать абстрактные классы в своей иерархии, переопределить или
# реализовать 5 магических методов (любые кроме __str__, __repr__, ___new__, __init__)
# - чем экзотичнее тем лучше

car = Car(4, 160, 'asfalt')

RPOW = 5 ** car
#  return behavior was changed __rpow__
print('a' in car)
#  return False __contains__
print(hash(car))
#  your hash = 1 from now __hash__
print(len(car))
#  len is 69 from now __len__
car.__neg__()
#  behavior was changed __neg__
#  abstract class is Engine

ferari = Car(4, 320, 'asfalt')
bycicle = Bycicle(1, 10, 'asfalt')
poplavock = TransportSubmarine(13000, 45, 'water', 1000.52)

#  self, max_capacity: int, max_speed: int, surf_type_support: str
#  def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str, i_depth: float):
thing = Wunderwaffle(100, 150, 'asfalt', 22.8)
thing.going_depth(34.233)  # Method inherited from TransportSubmarine
print(hash(thing))  # magic method __hash__ from inherited Car class
