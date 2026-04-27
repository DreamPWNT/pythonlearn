import random
import string


# а давайте хранить где-то существующие wallet_id?
LIKE_ID_DATA_BASE = []

class Wallet:
    """
    Класс представляет кошелек пользователя.

    Атрибуты:
        owner (str): имя владельца
        wallet_id (str): уникальный идентификатор кошелька
        currency (str): валюта кошелька
        balance (float): текущий баланс
    """

    def __init__(self, owner: str, currency: str = "USD"):
        self.owner = owner
        self.wallet_id = self.generate_id()
        self.currency = currency
        self.balance = 0.0

    def generate_id(self) -> str:
        """
        Генерирует уникальный ID длиной 10 символов, состоящий из цифр и букв.
        """
        while True:
            # Если не понятно что такое k, то попробуйте сомостоятельно это узнать
            # по подсказке функции random.choices и теста. Мне не лень было это описать,
            # я просто хочу чтоб вы становились более самостоятельными.
            wallet_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if wallet_id not in LIKE_ID_DATA_BASE:
                break
        LIKE_ID_DATA_BASE.append(wallet_id)
        return wallet_id

    def deposit(self, amount: int | float):
        """
        Пополняет баланс на заданную сумму.

        Args:
            amount (int | float): сумма пополнения
        """
        if amount <= 0:
            print("Сумма пополнения должна быть положительной")
            return False
        self.balance += amount
        return self

    def withdraw(self, amount: int | float):
        """
        Списывает средства с баланса.

        Args:
            amount (int | float): сумма списания
        """
        if amount <= 0:
            print("Сумма списания должна быть положительной")
            return False
        if amount > self.balance:
            print("Недостаточно средств на балансе")
            return False
        self.balance -= amount
        return self

    # Аннотацию типа, если ссылка не доступна можно укказать в кавычках "Wallet"
    def transfer_to(self, target_wallet: "Wallet", amount: int | float):
        """
        Переводит средства на другой кошелек.

        Args:
            target_wallet (Wallet): объект другого кошелька
            amount (int | float): сумма перевода
        """
        if self.currency != target_wallet.currency:
            print("Нельзя перевести между кошельками с разной валютой")
            return False
        
        result = self.withdraw(amount)
        if result:
            target_wallet.deposit(amount)
        return result

    def __add__(self, amount: int | float):
        """
        Позволяет пополнить кошелек через оператор +.

        Пример:
            wallet = wallet + 100
        """
        if isinstance(amount, (int, float)):  # или int или float
            return self.deposit(amount)
        return NotImplemented

    def __sub__(self, amount: int | float):
        """
        Позволяет списать с кошелька через оператор -.

        Пример:
            wallet = wallet - 50
        """
        if isinstance(amount, (int, float)):  # или int или float
            return self.withdraw(amount)
        return NotImplemented

    def __str__(self) -> str:
        return f"{self.owner}'s Wallet | ID: {self.wallet_id} | {self.balance:.2f} {self.currency}"

