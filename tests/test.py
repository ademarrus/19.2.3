import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

 # тест на произведение 
    def test_multiply_calculate_cottectly(self):
        assert self.calc.multiply(self, 3, 3) == 9

 # тест на деление
    def test_division_calculate_cottectly(self):
        assert self.calc.division(self, 12, 3) == 4

 # тест на вычитание
    def test_subtraction_calculate_cottectly(self):
        assert self.calc.subtraction(self, 10, 5) == 5

 # тест на сложение
    def test_adding_calculate_cottectly(self):
        assert self.calc.adding(self, 3, 3) == 6
