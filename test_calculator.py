import calculator


class TestCalculator:

	def test_addition(self):
		assert 5 == calculator.addition(4,1)

	def test_subtraction(self):
		assert 2 == calculator.subtraction(5,3)

	def test_multiply(self):
        assert 2 == calculator.multiplication(1, 2)