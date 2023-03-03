from string import ascii_letters


class Person():

    S_RUS = 'йцукенгшщзхъфывапролджэячсмитьбюё-'
    S_RUS_UPPER = S_RUS.upper()


    def __init__(self, fio, old, ps, weight):
        self.veryfy_fio(fio)

        self.__fio = fio
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def veryfy_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        strok = fio.split()

        if len(strok) != 3:
            raise TypeError('Не верный формат ФИО')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for i in strok:
            if len(i.strip(letters)) != 0:
                raise TypeError('Не верный формат ФИО')

    @classmethod
    def veryfy_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Не верный формат возраста')

    @classmethod
    def veryfy_weight(cls, weight):
        if type(weight) != float or weight < 0:
            raise TypeError('Не верный формат массы')

    @classmethod
    def veryfy_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('паспорт должен быть строкой')
        passp = ps.split()
        if len(passp) != 2 or len(passp[0]) != 4 or len(passp[1]) != 6:
            raise TypeError('Не верный формат паспорта')
        for i in passp:
            if not i.isdigit():
                raise TypeError('Не верный формат паспорта')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.veryfy_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.veryfy_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.veryfy_ps(passport)
        self.__passport = passport


p = Person('Иванов Иван Иванович', 110, '1234 567891', 80.2)
print(p.__dict__)
p.old = 120
p.weight = 300.0

print(p.__dict__)
