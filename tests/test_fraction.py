import unittest
from fraction_class import Fraction


class TestFraction(unittest.TestCase):
    def test_initialization(self):
        # Проверка корректной инициализации
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        # Проверка упрощения дроби
        f = Fraction(6, 8)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        # Проверка отрицательного знаменателя
        f = Fraction(3, -4)
        self.assertEqual(f.numerator, -3)
        self.assertEqual(f.denominator, 4)

        # Проверка исключения при нулевом знаменателе
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_from_float(self):
        # Проверка создания дроби из float
        f = Fraction.from_float(0.75)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        # Проверка исключения при неверном типе
        with self.assertRaises(TypeError):
            Fraction.from_float("0.75")

    def test_addition(self):
        # Проверка сложения дробей
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

        # Проверка сложения с целым числом
        result = f1 + 1
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 2)

        # Проверка сложения с float
        result = f1 + 0.5
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

    def test_subtraction(self):
        # Проверка вычитания дробей
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

        # Проверка вычитания целого числа
        result = f1 - 1
        self.assertEqual(result.numerator, -1)
        self.assertEqual(result.denominator, 2)

        # Проверка вычитания float
        result = f1 - 0.25
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_multiplication(self):
        # Проверка умножения дробей
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 3)

        # Проверка умножения на целое число
        result = f1 * 2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Проверка умножения на float
        result = f1 * 0.5
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

    def test_division(self):
        # Проверка деления дробей
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 / f2
        self.assertEqual(result.numerator, 3)
        self.assertEqual(result.denominator, 4)

        # Проверка деления на целое число
        result = f1 / 2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 4)

        # Проверка деления на float
        result = f1 / 0.5
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 1)

        # Проверка исключения при делении на ноль
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_comparison(self):
        # Проверка равенства дробей
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        self.assertEqual(f1, f2)

        # Проверка неравенства дробей
        f3 = Fraction(1, 3)
        self.assertNotEqual(f1, f3)

        # Проверка сравнения с целым числом
        self.assertEqual(Fraction(2, 1), 2)
        self.assertNotEqual(Fraction(3, 2), 1)

        # Проверка сравнения с float
        self.assertEqual(Fraction(1, 2), 0.5)
        self.assertNotEqual(Fraction(1, 2), 0.75)

    def test_negation(self):
        # Проверка унарного минуса
        f = Fraction(1, 2)
        neg_f = -f
        self.assertEqual(neg_f.numerator, -1)
        self.assertEqual(neg_f.denominator, 2)

    def test_absolute_value(self):
        # Проверка абсолютного значения
        f = Fraction(-1, 2)
        abs_f = abs(f)
        self.assertEqual(abs_f.numerator, 1)
        self.assertEqual(abs_f.denominator, 2)

    def test_power(self):
        # Проверка возведения в степень
        f = Fraction(2, 3)
        result = f ** 2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 9)

        # Проверка исключения при неверной степени
        with self.assertRaises(TypeError):
            f ** 1.5

    def test_conversion(self):
        # Проверка преобразования в float
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

        # Проверка преобразования в int
        f = Fraction(3, 2)
        self.assertEqual(int(f), 1)

        # Проверка округления
        f = Fraction(3, 4)
        self.assertEqual(round(f), 1)

    def test_string_representation(self):
        # Проверка строкового представления
        f = Fraction(3, 4)
        self.assertEqual(str(f), "3/4")
        self.assertEqual(repr(f), "Fraction(3, 4)")

        # Проверка для целого числа
        f = Fraction(4, 2)
        self.assertEqual(str(f), "2")
        self.assertEqual(repr(f), "Fraction(2)")

    def test_inplace_operations(self):
        # Проверка оператора +=
        f = Fraction(1, 2)
        f += Fraction(1, 3)
        self.assertEqual(f.numerator, 5)
        self.assertEqual(f.denominator, 6)

        # Проверка оператора -=
        f = Fraction(1, 2)
        f -= Fraction(1, 3)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 6)

        # Проверка оператора *=
        f = Fraction(1, 2)
        f *= Fraction(2, 3)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 3)

        # Проверка оператора /=
        f = Fraction(1, 2)
        f /= Fraction(2, 3)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)

        # Проверка исключения при делении на ноль
        f = Fraction(1, 2)
        with self.assertRaises(ZeroDivisionError):
            f /= Fraction(0, 1)

    def test_round(self):
        # Проверка округления
        f = Fraction(3, 4)
        self.assertEqual(round(f), 1)

        # Проверка округления с указанием количества знаков
        f = Fraction(5, 6)
        self.assertEqual(round(f, 2), 0.83)

    def test_int_conversion(self):
        # Проверка преобразования в целое число
        f = Fraction(3, 2)
        self.assertEqual(int(f), 1)

        f = Fraction(4, 2)
        self.assertEqual(int(f), 2)

    def test_float_conversion(self):
        # Проверка преобразования в float
        f = Fraction(1, 2)
        self.assertEqual(float(f), 0.5)

        f = Fraction(3, 4)
        self.assertEqual(float(f), 0.75)


if __name__ == "__main__":
    unittest.main()
