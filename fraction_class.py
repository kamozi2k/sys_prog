import math


class Fraction:
    """
    Класс для работы с дробями.

    Атрибуты:
        numerator (int): Числитель дроби.
        denominator (int): Знаменатель дроби.
    """

    def __init__(self, numerator, denominator=1):
        """
        Инициализация дроби.

        :param numerator: Числитель (целое число).
        :param denominator: Знаменатель (целое число, по умолчанию 1).
        :raises TypeError: Если числитель или знаменатель не являются целыми числами.
        :raises ValueError: Если знаменатель равен нулю.
        """
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("Числитель и знаменатель должны быть целыми числами.")
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")

        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Упрощаем дробь при создании

    def _simplify(self):
        """
        Упрощает дробь, деля числитель и знаменатель на их НОД.
        """
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:  # Убедимся, что знаменатель положительный
            self.numerator *= -1
            self.denominator *= -1

    @classmethod
    def from_float(cls, value):
        """
        Создает Fraction из числа с плавающей точкой.

        :param value: Число с плавающей точкой.
        :return: Объект Fraction.
        :raises TypeError: Если value не является float.
        """
        if not isinstance(value, float):
            raise TypeError("Ожидается число с плавающей точкой.")
        decimal_places = len(str(value).split('.')[1])
        denominator = 10 ** decimal_places
        numerator = int(value * denominator)
        return cls(numerator, denominator)

    def __add__(self, other):
        """
        Сложение двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: Новая дробь.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()  # Упрощаем результат
        return result

    def __sub__(self, other):
        """
        Вычитание двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: Новая дробь.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()  # Упрощаем результат
        return result

    def __mul__(self, other):
        """
        Умножение двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: Новая дробь.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()  # Упрощаем результат
        return result

    def __truediv__(self, other):
        """
        Деление двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: Новая дробь.
        :raises TypeError: Если other не является Fraction, int или float.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result._simplify()  # Упрощаем результат
        return result

    def __iadd__(self, other):
        """
        Оператор +=.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self._simplify()  # Упрощаем результат
        return self

    def __isub__(self, other):
        """
        Оператор -=.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
        self.denominator = self.denominator * other.denominator
        self._simplify()  # Упрощаем результат
        return self

    def __imul__(self, other):
        """
        Оператор *=.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        self.numerator = self.numerator * other.numerator
        self.denominator = self.denominator * other.denominator
        self._simplify()  # Упрощаем результат
        return self

    def __itruediv__(self, other):
        """
        Оператор /=.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: self.
        :raises TypeError: Если other не является Fraction, int или float.
        :raises ZeroDivisionError: Если other равен нулю.
        """
        if isinstance(other, int):
            other = Fraction(other)
        elif isinstance(other, float):
            other = Fraction.from_float(other)
        elif not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        self.numerator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        self._simplify()  # Упрощаем результат
        return self

    def __eq__(self, other):
        """
        Проверка на равенство двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: True, если дроби равны, иначе False.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        if isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        elif isinstance(other, float):
            return float(self) == other
        elif not isinstance(other, Fraction):
            return NotImplemented
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        """
        Проверка на неравенство двух дробей.

        :param other: Другая дробь, целое число или число с плавающей точкой.
        :return: True, если дроби не равны, иначе False.
        :raises TypeError: Если other не является Fraction, int или float.
        """
        return not self.__eq__(other)

    def __neg__(self):
        """
        Унарный минус.

        :return: Новая дробь с противоположным знаком.
        """
        result = Fraction(-self.numerator, self.denominator)
        result._simplify()  # Упрощаем результат
        return result

    def __pow__(self, power):
        """
        Возведение дроби в степень.

        :param power: Степень (целое число).
        :return: Новая дробь.
        :raises TypeError: Если power не является целым числом.
        """
        if not isinstance(power, int):
            raise TypeError("Степень должна быть целым числом.")
        result = Fraction(self.numerator ** power, self.denominator ** power)
        result._simplify()  # Упрощаем результат
        return result

    def __float__(self):
        """
        Преобразование дроби в число с плавающей точкой.

        :return: Число с плавающей точкой.
        """
        return self.numerator / self.denominator

    def __int__(self):
        """
        Преобразование дроби в целое число.

        :return: Целое число.
        """
        return self.numerator // self.denominator

    def __abs__(self):
        """
        Абсолютное значение дроби.

        :return: Новая дробь с положительными числителем и знаменателем.
        """
        result = Fraction(abs(self.numerator), abs(self.denominator))
        result._simplify()  # Упрощаем результат
        return result

    def __round__(self, ndigits=None):
        """
        Округление дроби.

        :param ndigits: Количество знаков после запятой.
        :return: Округленное число с плавающей точкой.
        """
        return round(float(self), ndigits)

    def __str__(self):
        """
        Строковое представление дроби.

        :return: Строка в формате "numerator/denominator" или "numerator", если знаменатель равен 1.
        """
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """
        Представление для отладки.

        :return: Строка в формате "Fraction(numerator, denominator)".
        """
        if self.denominator == 1:
            return f"Fraction({self.numerator})"
        return f"Fraction({self.numerator}, {self.denominator})"
