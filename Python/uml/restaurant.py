"""UML class diagram"""
import time


class Person:
    def __init__(self, pers_id: int, pers_name: str, pers_type: str, pers_address: str, pers_phone: int):
        self.pers_id = pers_id
        self.pers_name = pers_name
        self.pers_type = pers_type
        self.pers_address = pers_address
        self.pers_phone = pers_phone
        print("class Person was Initialized")


class Customer(Person):
    def __init__(self, cstmr_id: int, name: str, person_type: str, address: str, phone: int, bank_card, mail):
        super().__init__(cstmr_id, name, person_type, address, phone)
        self.bank_card = bank_card
        self.mail = mail
        print("class Customer was Initialized")

    def gen_order(self, type_call, obj):
        if type_call == 'order_through_site':
            return self.order_site(obj)
        elif type_call == 'irl':
            return self.order_call
        else:
            raise TypeError

    def order_site(self, obj):
        dishes_iwant = ['soup', 'pizza', 'waffles']
        site_menu = obj.get_menu()
        my_order = [i for i in dishes_iwant if i in site_menu]
        if my_order:
            return obj.form_order(my_order, self.pers_id)
        else:
            print('Unfortunately there arent my favourite dishes')

    def order_call(self, order_id, status, item_list, order_type):
        return Order(order_id, status, item_list, order_type)

    def reservation_site(self, obj):
        return obj.reserve_table

    def eat_food(self, food):
        print('Ty! it was delicious')


class Site:
    curr_menu_list = ['milk', 'bread', 'pizza']

    def __init__(self, address: str):
        self.address = address
        print('webiste was created!')

    def get_menu(self):
        return self.curr_menu_list

    def form_order(self, my_order, order_id):
        formed_order = Order(order_id, 'in progress', my_order, 'site')
        return formed_order

    def reserve_table(self, obj_operator, id, date, table_list):
        obj_operator.reserve_table(id, date, table_list)



class ReceptionistOperator:
    def __init__(self):
        print('operator was created!')

    def reserve_table(self, id, date, table_list):
        for i in table_list:
            if i.id == id:
                try:
                    i.add_reservation(date, 'reserved')
                except ValueError:
                    print('Ooops, table reserved')


class Order:
    def __init__(self, order_id: int, status: str, item_list: list, order_type: str):
        self.order_id = order_id
        self.status = status
        self.item_list = item_list
        self.order_type = order_type

    def add_items(self, item):
        self.item_list.append(item)

    def remove_items(self, item):
        self.item_list.remove(item)
#
class Tables:
    def __init__(self, t_id):
        self.id = t_id
        self.date = None
        self.status = 'free'

    def add_reservation(self, date, status):
        if status == 'free':
            self.date = date
            self.status = status
            print('Table was reserved')
        else:
            raise ValueError

    def remove_reservation(self):
        if self.status != 'free':
            self.status = 'free'
#
#
class Kitchen:

    def cook_food(order):
        print('your order cooking!')
        time.sleep(0.5)
        print('almost done!')
        cooked_food = order
        time.sleep(0.5)
        print('ready!')
        return cooked_food

    def form_delivery_pkgs(food):
        food_pkg = food
        return food_pkg

    def bring_ready_orders(cooked_food):
        served_tasty_dish = cooked_food
        return served_tasty_dish


    def kitcher_workers_reg(self, chef, waiter):
        pass

class Delivery:
    def __init__(self, client: object, order: object):
        self.client_id = client
        self.order = order
        print('On my way!')
        time.sleep(0.5)
        self.delivered(client)

    def delivered(self, client):
        print('Delivered.')
        time.sleep(1)
        client.eat_food(self.order)

class Employee(Person):
    def __init__(self, cstmr_id: int, name: str, person_type: str, address: str, phone: int, length_of_work :int,
                 position: str, salary: int):
        super().__init__(cstmr_id, name, person_type, address, phone)
        self.length_of_work = length_of_work
        self.position = position
        self.salary = salary

class Waiter(Employee):
    def __init__(self, cstmr_id: int, name: str, person_type: str, address: str, phone: int, length_of_work :int,
                 position: str, salary: int):
        super().__init__(cstmr_id, name, person_type, address, phone, length_of_work, position, salary)
        self.id_order = None
        self.curr_order = None

    def get_order(self, order):
        print("Waiter got your order and moving to kitchen!")
        return order


    def bring_food(self, id, food):
        food_on_table = food
        return food_on_table

class Chef(Employee):
    worker_list = []
    def add_new_worker(self, position):
        if position:
            self.worker_list.append(Employee)

    def fire_worker(self, id):
        for i in self.worker_list:
            if i.id == id:
                self.worker_list.remove(i)

    def buy_products(self, supplier: object, products: list):
        return supplier.give_pricelist(products)


class Supplier(Person):
    mail = ''
    item_list = []
    def give_pricelist(self, item_list):
        self.item_list = [i for i in item_list if i in self.item_list]
        return self.item_list

    def make_waybill(self, status, shipping_date, sum, weight):
        return Waybill(status, shipping_date, sum, weight)

class Waybill:
    def __init__(self, status, shipping_date, prd_sum, weight):
        self.status = status
        self.shipping_date = shipping_date
        self.prd_sum = prd_sum
        self.weight = weight


while True:
    choose = input("Scenario number:")
    if choose == '1':
        restaurant_website = Site('www.gordonramzi.com')
        Oleg = Customer(0, 'Oleg', 'customer', 'Buchmy 40a', 123, 123, 'oleg@gmail.com')
        order = Oleg.gen_order('order_through_site', restaurant_website)
        cooked_food = Kitchen.cook_food(order)
        ready_package = Kitchen.form_delivery_pkgs(cooked_food)
        Delivery(Oleg, ready_package)
    elif choose == '2':
        restaurant_website = Site('www.gordonramzi.com')
        table_list = []
        for i in range(30):
            table_list.append(Tables(i))
        receptionist = ReceptionistOperator()
        Oleg = Customer(0, 'Oleg', 'customer', 'Buchmy 40a', 123, 123, 'oleg@gmail.com')
        reservation = Oleg.reservation_site(restaurant_website)
        reservation(receptionist, 1, '24.10.2023', table_list)
        waiter = Waiter(1, 'Petro', 'worker', 'Pushkina str', 3355221, 18, 'waiter', 18)
        order = Oleg.gen_order('irl', None)(1, 'in progress', ['bread', 'cheese'], 'type')
        order_on_kitchen = waiter.get_order(order)
        cooked_food = Kitchen.cook_food(order_on_kitchen)
        print(cooked_food)
        served_tasty_dish = Kitchen.bring_ready_orders(cooked_food)
        food_on_table = waiter.bring_food(Oleg.pers_id, served_tasty_dish)
        Oleg.eat_food(food_on_table)
    else:
        break
