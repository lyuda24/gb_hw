class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = f'Полное имя сотрудника: {self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        print(f'Доход сотрудника с учетом премии: {total_income} $')


pos = Position("Иванов", "Алексей", "Manager", 20000, 7000)
pos.get_full_name()
pos.get_total_income()
