import unittest
import math
from fraction_class import Fraction
from complex import Complex


class TestComplex(unittest.TestCase):
    def test_initialization(self):
        # Проверка инициализации с целыми числами
        c = Complex(1, 2)
        self.assertEqual(c.real, Fraction(1))
        self.assertEqual(c.imag, Fraction(2))

        # Проверка инициализации с дробями
        c = Complex(Fraction(1, 2), Fraction(3, 4))
        self.assertEqual(c.real, Fraction(1, 2))
        self.assertEqual(c.imag, Fraction(3, 4))

        # Проверка инициализации с числами с плавающей точкой
        c = Complex(0.5, 0.75)
        self.assertEqual(c.real, Fraction.from_float(0.5))
        self.assertEqual(c.imag, Fraction.from_float(0.75))

    def test_addition(self):
        # Сложение двух комплексных чисел
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 + c2
        self.assertEqual(result.real, Fraction(4))
        self.assertEqual(result.imag, Fraction(6))

        # Сложение с целым числом
        result = c1 + 5
        self.assertEqual(result.real, Fraction(6))
        self.assertEqual(result.imag, Fraction(2))

        # Сложение с числом с плавающей точкой
        result = c1 + 0.5
        self.assertEqual(result.real, Fraction(3, 2))
        self.assertEqual(result.imag, Fraction(2))

    def test_subtraction(self):
        # Вычитание двух комплексных чисел
        c1 = Complex(5, 6)
        c2 = Complex(1, 2)
        result = c1 - c2
        self.assertEqual(result.real, Fraction(4))
        self.assertEqual(result.imag, Fraction(4))

        # Вычитание целого числа
        result = c1 - 2
        self.assertEqual(result.real, Fraction(3))
        self.assertEqual(result.imag, Fraction(6))

        # Вычитание числа с плавающей точкой
        result = c1 - 0.5
        self.assertEqual(result.real, Fraction(9, 2))
        self.assertEqual(result.imag, Fraction(6))

    def test_multiplication(self):
        # Умножение двух комплексных чисел
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 * c2
        self.assertEqual(result.real, Fraction(-5))
        self.assertEqual(result.imag, Fraction(10))

        # Умножение на целое число
        result = c1 * 2
        self.assertEqual(result.real, Fraction(2))
        self.assertEqual(result.imag, Fraction(4))

        # Умножение на число с плавающей точкой
        result = c1 * 0.5
        self.assertEqual(result.real, Fraction(1, 2))
        self.assertEqual(result.imag, Fraction(1))

    def test_division(self):
        # Деление двух комплексных чисел
        c1 = Complex(1, 2)
        c2 = Complex(3, 4)
        result = c1 / c2
        self.assertEqual(result.real, Fraction(11, 25))
        self.assertEqual(result.imag, Fraction(2, 25))

        # Деление на целое число
        result = c1 / 2
        self.assertEqual(result.real, Fraction(1, 2))
        self.assertEqual(result.imag, Fraction(1))

        # Деление на число с плавающей точкой
        result = c1 / 0.5
        self.assertEqual(result.real, Fraction(2))
        self.assertEqual(result.imag, Fraction(4))

        # Проверка исключения при делении на ноль
        with self.assertRaises(ZeroDivisionError):
            c1 / Complex(0, 0)

    def test_comparison(self):
        # Проверка равенства
        c1 = Complex(1, 2)
        c2 = Complex(1, 2)
        self.assertEqual(c1, c2)

        # Проверка неравенства
        c3 = Complex(2, 3)
        self.assertNotEqual(c1, c3)

        # Проверка сравнения с целым числом
        self.assertEqual(Complex(2, 0), 2)
        self.assertNotEqual(Complex(2, 1), 2)

        # Проверка сравнения с числом с плавающей точкой
        self.assertEqual(Complex(0.5, 0), 0.5)
        self.assertNotEqual(Complex(0.5, 0.1), 0.5)

    def test_negation(self):
        # Унарный минус
        c = Complex(1, 2)
        neg_c = -c
        self.assertEqual(neg_c.real, Fraction(-1))
        self.assertEqual(neg_c.imag, Fraction(-2))

    def test_absolute_value(self):
        # Модуль комплексного числа
        c = Complex(3, 4)
        self.assertEqual(abs(c), 5)

    def test_power(self):
        # Тест 1: Возведение в положительную степень
        c1 = Complex(2, 3)
        result1 = c1 ** 2
        self.assertEqual(result1.real, Fraction(-5))  # (2 + 3i)^2 = -5 + 12i
        self.assertEqual(result1.imag, Fraction(12))

        # Тест 2: Возведение в нулевую степень
        c2 = Complex(1, 1)
        result2 = c2 ** 0
        self.assertEqual(result2.real, Fraction(1))  # Любое число в степени 0 равно 1
        self.assertEqual(result2.imag, Fraction(0))

        # Тест 3: Возведение в отрицательную степень
        c3 = Complex(1, 1)
        result3 = c3 ** -1
        self.assertEqual(result3.real, Fraction(1, 2))  # (1 + i)^-1 = 0.5 - 0.5i
        self.assertEqual(result3.imag, Fraction(-1, 2))

        # Тест 4: Проверка исключения при нецелой степени
        c4 = Complex(1, 1)
        with self.assertRaises(TypeError):
            c4 ** 1.5  # Нецелая степень должна вызывать TypeError

    def test_conjugate(self):
        # Сопряженное комплексное число
        c = Complex(1, 2)
        conj = c.conjugate()
        self.assertEqual(conj.real, Fraction(1))
        self.assertEqual(conj.imag, Fraction(-2))

    def test_exp(self):
        # Экспонента комплексного числа
        c = Complex(0, math.pi)
        result = c.exp()
        self.assertAlmostEqual(float(result.real), -1, places=5)
        self.assertAlmostEqual(float(result.imag), 0, places=5)

    def test_polar(self):
        # Полярные координаты
        c = Complex(1, 1)
        r, theta = c.polar()
        self.assertAlmostEqual(r, math.sqrt(2), places=5)
        self.assertAlmostEqual(theta, math.pi / 4, places=5)

    def test_is_real(self):
        # Проверка, является ли число действительным
        c1 = Complex(1, 0)
        self.assertTrue(c1.is_real())

        c2 = Complex(1, 1)
        self.assertFalse(c2.is_real())

    def test_is_imaginary(self):
        # Проверка, является ли число чисто мнимым
        c1 = Complex(0, 1)
        self.assertTrue(c1.is_imaginary())

        c2 = Complex(1, 1)
        self.assertFalse(c2.is_imaginary())


if __name__ == "__main__":
    unittest.main()
