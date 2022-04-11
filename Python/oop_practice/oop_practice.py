#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Class diagram for restaurant"""


class Person:

    """superclass for Customer/Employee/Supplier"""

    id = 0
    name = ''
    type = ''
    address = ''
    phone = 0


class Customer(Person):

    """physical client which can interact with site"""

    bank_card = 0
    mail = ''

    def checkin(self):
        pass

    def checkout(self):
        pass


class Employee(Person):

    """Employees of restaurant"""

    salary = 0
    lenght_of_work = 0
    position = ''


class Supplier(Person):

    """Supplier of restaurant"""

    mail = ''

    def give_pricelist(self):
        pass

    def deliver_products(self):
        pass


class Site:

    """website of restaurant"""

    address = ''

    def form_order(self, order):
        pass

    def reserve_table(self, id, date):
        pass


class RecepionistOperator:

    """manage orders from website and physical orders"""

    def reserve_table(self):
        pass

    def verify_order(self):
        pass


class Tables:

    """table reservation"""

    id = 0
    is_reserved = False

    def add_reservation(self, id, date):
        pass

    def remove_reservation(self, id):
        pass


class Waiter(Employee):

    """waiters bring food from kitchen by id_order"""

    id_order = 0

    def bring_food(self):
        pass


class Chef(Employee):

    """Chef can manage employees and buy products from Suppliers"""

    def add_new_worker(self, position):
        pass

    def fire_worker(self, id):
        pass

    def buy_products(self, supplier, products):
        pass


class Kitchen:

    """there cook orders for tables and delivery"""

    def cook_food(self):
        pass

    def form_delivery_pkgs(self):
        pass

    def bring_ready_orders(self):
        pass


class Delivery:

    """delivery service"""

    client_id = 0

    def deliver(self, id):
        pass
