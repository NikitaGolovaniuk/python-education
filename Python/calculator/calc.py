"""simple module which contain calculator class with 4 methods"""
class Calculator:
    """core calculator class"""
    @classmethod
    def calc_addition(cls, first_val, second_val):
        """return the sum of two values"""
        return first_val+second_val

    @classmethod
    def calc_subtraction(cls, first_val, second_val):
        """return the difference of two values"""
        return first_val-second_val

    @classmethod
    def calc_division(cls, first_val, second_val):
        """return the division result"""
        return first_val/second_val

    @classmethod
    def calc_multiplication(cls, first_val, second_val):
        """return the multiplication result"""
        return first_val*second_val
