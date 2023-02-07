import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self): # через метод setup подключаем тестируемый объект
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # тест, который проверяет корректность умножения (multiply)
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 6, 3) == 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 3, 5) == 8