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
    def __init__(self, max_capacity: int, max_speed: int, surf_type_support: str, car_model: str):
        super().__init__(max_capacity, max_speed, surf_type_support)
        self.car_model = car_model
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine

    def __rpow__(self, x_val):
        print('behavior was changed!')

    def __contains__(self, item):
        return item * 2

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
        super().__init__(max_capacity, max_speed, surf_type_support)
        self.engine = None
        self.i_depth = i_depth

    def going_depth(self, depth: float):
        """call when we going deep"""
        self.i_depth = depth
        print("We are goin on: ", self.i_depth)

    def set_engine(self, engine):
        self.engine = engine


class Wunderwaffle(Car, TransportSubmarine):
    """mad creation made by mad scientist"""
    def __init__(self, max_capacity: int, max_speed: int, surf_tsup: str, possible_depth: float):
        super(Car, self).__init__(max_capacity, max_speed, surf_tsup, possible_depth)
        super(TransportSubmarine, self).__init__(max_capacity, max_speed, surf_tsup)

    def going_depth(self, depth: float):
        print('We are allready in:', depth)
