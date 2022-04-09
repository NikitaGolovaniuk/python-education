"""simple calculator module with 4 methods"""
class Calculator:
    """core class"""
    @classmethod
    def addition_two_val(cls, first_val, second_val):
        """return x+y"""
        return first_val + second_val

    @classmethod
    def substraction_two_val(cls, first_val, second_val):
        """return x-y"""
        return first_val - second_val

    @classmethod
    def multiplication_two_val(cls, first_val, second_val):
        """return x*y"""
        return first_val * second_val

    @classmethod
    def division_two_val(cls, first_val, second_val):
        """return x/y"""
        return first_val / second_val
