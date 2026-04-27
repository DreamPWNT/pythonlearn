from my_lib import *


class Kid(Person):
    pass

class Adult(Person):  # Взрослый
    def __init__(
            self, first_name, last_name, age, salary=None
        ):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def introduce(self):
        return super().introduce() + \
            f", salary {self.salary}$"


class Customer(Person):  # Клиент
    name = "Customer"

class Employee(Salary_Mixin, Adult):  # Сотрудник
    name = "Employee"

class Employer(Salary_Mixin, Adult):  # Работодатель
    pass
