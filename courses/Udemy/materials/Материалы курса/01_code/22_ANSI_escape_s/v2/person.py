class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        return f"{self.first_name}" f" {self.last_name}, age {self.age}"


class Salary_Mixin:
    def change_salary(self, new):
        self.salary = new


class Kid(Person):
    pass


class Adult(Person):  # Взрослый
    def __init__(self, first_name, last_name, age, salary=None):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def introduce(self):
        return super().introduce() + f", salary {self.salary}$"


class Customer(Person):  # Клиент
    name = "Customer"


class Employee(Salary_Mixin, Adult):  # Сотрудник
    name = "Employee"


class Employer(Salary_Mixin, Adult):  # Работодатель
    pass
