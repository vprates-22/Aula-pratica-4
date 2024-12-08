import unittest
from calculator import soma, subtrai, multiplica, divide

class TestCalculator(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(5, 10.0), 15.0)
        self.assertEqual(soma(1, -1), 0)
        self.assertEqual(soma(0, 0), 0)
        self.assertEqual(soma(2.5, 4.0, 0.0, 10, -8.5), 8.0)

    def test_subtract(self):
        self.assertEqual(subtrai(10, 8), 2)
        self.assertEqual(subtrai(0, 2), -2)
        self.assertEqual(subtrai(2, -2), 4)
        self.assertEqual(subtrai(2.5, 1.5), 1.0)

    def test_multiplica(self):
        self.assertEqual(multiplica(10, 8), 80)
        self.assertEqual(multiplica(0.5, 2), 1.0)
        self.assertEqual(multiplica(2, -2), -4)
        self.assertEqual(multiplica(0, 1.5), 0)
        self.assertEqual(multiplica(0, 1.5, 1, 3, 5), 0.0)
        self.assertEqual(multiplica(1, 1.5, 1, 3, 5), 22.5)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(2, -2), -1)
        self.assertEqual(divide(4.5, 1.5), 3.0)
        self.assertEqual(divide(5, 2), 2.5)

    def test_erro_de_tipo(self):
        with self.assertRaises(TypeError):
            soma("a", 3)
        with self.assertRaises(TypeError):
            subtrai(3, None)
        with self.assertRaises(TypeError):
            divide(divide, 3)
        with self.assertRaises(TypeError):
            multiplica(2, 3, 1, 2, 3, "5")

    def test_erro_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(2.4, 0)


if __name__ == '__main__':
    unittest.main()