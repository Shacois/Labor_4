class Gun:
    def __init__(self, name, maximum_ammo: int, ammo_left: int):
        """
        :param name: Название
        :param maximum_ammo: Максимальное количество боеприпасов
        :param ammo_left: Оставшиеся боеприпасы
        """
        if not isinstance(maximum_ammo, int):
            raise TypeError
        if maximum_ammo <= 0:
            raise ValueError
        self.maximum_ammo = maximum_ammo

        if not isinstance(ammo_left, int):
            raise TypeError
        if ammo_left < 0:
            raise ValueError
        self.ammo_left = ammo_left

        self.name = name

    def __str__(self):
        return f"Максимальное количество боеприпасов {self.maximum_ammo}. Оставшиеся боеприпасы {self.ammo_left}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, maximum ammo={self.maximum_ammo!r}, " \
               f"left ammo={self.ammo_left})"

    def shoot(self, number_of_shots: int) -> None:
        """
        Выстрел
        :param number_of_shots: Количество выстрелов
        :raise ValueError: Если количество выстрелов превысит оставшееся количество боеприпасов, то возвращается ошибка
        :return: Количество оставшихся боеприпасов
        """
        if not isinstance(number_of_shots, int):
            raise TypeError
        if number_of_shots < 0:
            raise ValueError
        ...

    def reload(self, new_ammo: int) -> None:
        """
        Перезарядка
        :param new_ammo: Количество добавляемых боерипасов
        :raise ValueError: Если количество добавляемых боеприпасов превышает максимальное количество боеприпасов,
         то вызываем ошибку
        """
        if not isinstance(new_ammo, int):
            raise TypeError
        if new_ammo < 0:
            raise ValueError

class Flamethrower(Gun):

    def shoot(self, duration: float) -> None:
        """
        Огнемет стреляет не мгновенно, а в течение некоторого времени
        :param duration: Длительность выстрела
        :return: Количество оставшихся боеприпасов
        """