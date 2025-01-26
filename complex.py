import math
from fraction_class import Fraction


class Complex:
    """
    Класс для работы с комплексными числами.

    Атрибуты:
        real (Fraction): Действительная часть комплексного числа.
        imag (Fraction): Мнимая часть комплексного числа.
    """

    def __init__(self, real: Fraction | int | float = 0, imag: Fraction | int | float = 0):
        """
        Инициализация комплексного числа.

        :param real: Действительная часть (Fraction, int или float).
        :param imag: Мнимая часть (Fraction, int или float).
        """
        if isinstance(real, float):
            self._real = Fraction.from_float(real)
        else:
            self._real = real if isinstance(real, Fraction) else Fraction(real)

        if isinstance(imag, float):
            self._imag = Fraction.from_float(imag)
        else:
            self._imag = imag if isinstance(imag, Fraction) else Fraction(imag)

    @property
    def real(self):
        """
        Геттер для действительной части.

        :return: Действительная часть комплексного числа (Fraction).
        """
        return self._real

    @real.setter
    def real(self, value: Fraction | int | float):
        """
        Сеттер для действительной части.

        :param value: Новое значение действительной части (Fraction, int или float).
        """
        if isinstance(value, float):
            self._real = Fraction.from_float(value)
        else:
            self._real = value if isinstance(value, Fraction) else Fraction(value)

    @property
    def imag(self):
        """
        Геттер для мнимой части.

        :return: Мнимая часть комплексного числа (Fraction).
        """
        return self._imag

    @imag.setter
    def imag(self, value: Fraction | int | float):
        """
        Сеттер для мнимой части.

        :param value: Новое значение мнимой части (Fraction, int или float).
        """
        if isinstance(value, float):
            self._imag = Fraction.from_float(value)
        else:
            self._imag = value if isinstance(value, Fraction) else Fraction(value)

    def __str__(self):
        """
        Форматированный вывод комплексного числа.

        :return: Строка в формате "a + bi" или "a - bi".
        """
        if float(self.imag) >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(float(self.imag))}i"

    def __repr__(self):
        """
        Форматированный вывод для отладки.

        :return: Строка в формате "Complex(real, imag)".
        """
        return f"Complex({self.real}, {self.imag})"

    def __add__(self, other):
        """
        Перегрузка оператора сложения.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: Новое комплексное число.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: Новое комплексное число.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """
        Перегрузка оператора умножения.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: Новое комплексное число.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )

    def __truediv__(self, other):
        """
        Перегрузка оператора деления.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: Новое комплексное число.
        :raises TypeError: Если other не является Complex, int или float.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denominator,
            (self.imag * other.real - self.real * other.imag) / denominator
        )

    def __iadd__(self, other):
        """
        Перегрузка оператора +=.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        self.real += other.real
        self.imag += other.imag
        return self

    def __isub__(self, other):
        """
        Перегрузка оператора -=.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        self.real -= other.real
        self.imag -= other.imag
        return self

    def __imul__(self, other):
        """
        Перегрузка оператора *=.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + self.imag * other.real
        self.real = new_real
        self.imag = new_imag
        return self

    def __itruediv__(self, other):
        """
        Перегрузка оператора /=.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Complex, int или float.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        new_real = (self.real * other.real + self.imag * other.imag) / denominator
        new_imag = (self.imag * other.real - self.real * other.imag) / denominator
        self.real = new_real
        self.imag = new_imag
        return self

    def __eq__(self, other):
        """
        Перегрузка оператора равенства.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: True, если числа равны, иначе False.
        :raises TypeError: Если other не является Complex, int или float.
        """
        if isinstance(other, (int, float)):
            other = Complex(other)
        elif not isinstance(other, Complex):
            return NotImplemented
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        """
        Перегрузка оператора неравенства.

        :param other: Другое комплексное число, целое число или число с плавающей точкой.
        :return: True, если числа не равны, иначе False.
        :raises TypeError: Если other не является Complex, int или float.
        """
        return not self.__eq__(other)

    def __neg__(self):
        """
        Перегрузка унарного минуса.

        :return: Новое комплексное число с противоположными знаками.
        """
        return Complex(-self.real, -self.imag)

    def __abs__(self):
        """
        Перегрузка функции abs().

        :return: Модуль комплексного числа (float).
        """
        return math.sqrt(float(self.real ** 2 + self.imag ** 2))

    def __pow__(self, n):
        """
        Перегрузка оператора **.

        :param n: Степень (целое число).
        :return: Новое комплексное число.
        :raises TypeError: Если n не является целым числом.
        """
        if not isinstance(n, int):
            raise TypeError("Степень должна быть целым числом.")

        if n == 0:
            return Complex(1)  # Любое число в степени 0 равно 1

        result = Complex(1)
        for _ in range(abs(n)):
            result *= self

        if n < 0:
            return Complex(1) / result
        return result

    def arg(self):
        """
        Вычисление аргумента комплексного числа в радианах.

        :return: Аргумент комплексного числа (float).
        """
        return math.atan2(float(self.imag), float(self.real))

    def conjugate(self):
        """
        Вычисление сопряженного комплексного числа.

        :return: Новое комплексное число.
        """
        return Complex(self.real, -self.imag)

    def exp(self):
        """
        Вычисление экспоненты комплексного числа.

        :return: Новое комплексное число.
        """
        real_part = Fraction.from_float(math.exp(float(self.real)) * math.cos(float(self.imag)))
        imag_part = Fraction.from_float(math.exp(float(self.real)) * math.sin(float(self.imag)))
        return Complex(real_part, imag_part)

    def polar(self):
        """
        Представление комплексного числа в полярных координатах.

        :return: Кортеж (модуль, аргумент), где оба значения — float.
        """
        return abs(self), self.arg()

    def is_real(self):
        """
        Проверка, является ли комплексное число действительным.

        :return: True, если число действительное, иначе False.
        """
        return self.imag == 0

    def is_imaginary(self):
        """
        Проверка, является ли комплексное число чисто мнимым.

        :return: True, если число чисто мнимое, иначе False.
        """
        return self.real == 0
