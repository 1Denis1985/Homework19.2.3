from app.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calc = Calculator()

    def test_adding_positive(self):
        assert self.calc.adding(2, 3) == 5

    def test_adding_negative(self):
        assert self.calc.adding(2, 3) == 1

    def test_subtraction_positive(self):
        assert self.calc.subtraction(2, 3) == -1

    def test_subtraction_negative(self):
        assert self.calc.subtraction(2, 3) == 1

    def test_division_positive(self):
        assert self.calc.division(2, 0) == 'на ноль делить нельзя!'
        assert self.calc.division(10, 2) == 5

    def test_division_negative(self):
        assert self.calc.division(10, 2) == 4

    def test_multiply_positive(self):
        assert self.calc.multiply(2, 2) == 4

    def test_multiply_negative(self):
        assert self.calc.multiply(2, 2) == 5
