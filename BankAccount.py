from enum import Enum


class Account(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'


class BankAccount:
    name: str
    surname: str
    cash_amount: float = 0
    wallet_type: Account

    def __init__(self, name: str, surname: str, wallet_type: Account):
        self.name = name
        self.surname = surname
        self.wallet_type = wallet_type

    def add_to_bank_account(self, amount: int) -> None:
        self.cash_amount += amount

    def subtract_from_bank_account(self, amount: int) -> None:
        self.cash_amount -= amount

    def money_conversion(self, next_wallet_type: Account) -> None:
        if next_wallet_type == Account.KZT:
            if self.wallet_type == Account.USD:
                self.cash_amount *= 470
            if self.wallet_type == Account.RUB:
                self.cash_amount *= 7
            if self.wallet_type == Account.EUR:
                self.cash_amount *= 495
            self.wallet_type = Account.KZT

        elif next_wallet_type == Account.USD:
            if self.wallet_type == Account.KZT:
                self.cash_amount /= 470
            if self.wallet_type == Account.RUB:
                self.cash_amount /= 62
            if self.wallet_type == Account.EUR:
                self.cash_amount *= 1.05
            self.wallet_type = Account.USD

        elif next_wallet_type == Account.RUB:
            if self.wallet_type == Account.KZT:
                self.cash_amount /= 7
            if self.wallet_type == Account.USD:
                self.cash_amount *= 62
            if self.wallet_type == Account.EUR:
                self.cash_amount *= 65
            self.wallet_type = Account.RUB

        elif next_wallet_type == Account.EUR:
            if self.wallet_type == Account.KZT:
                self.cash_amount /= 495
            if self.wallet_type == Account.RUB:
                self.cash_amount /= 65
            if self.wallet_type == Account.USD:
                self.cash_amount /= 1.05
            self.wallet_type = Account.EUR

    def get_cash_amount(self) -> str:
        return f'Balance: {self.cash_amount} {self.wallet_type.value}'

    def set_cash_amount(self, cash_amount: float) -> None:
        self.cash_amount = cash_amount

    def __repr__(self):
        return f'{self.name} {self.surname}'

    def __del__(self):
        print(f"{self.name} {self.surname} account has been deleted")


bank_accounts = []
while True:
    command = int(input("Выберите действие:\n1. Создать пользователя\n2. Выбрать пользователя\n0. Выйти\n"))

    if command == 1:
        name = input("Введите имя:")
        surname = input("Введите фамилию:")
        w_type = input("Введите валюту:")

        wallet_type = Account.KZT
        if w_type == "USD":
            wallet_type = Account.USD
        elif w_type == "RUB":
            wallet_type = Account.RUB
        elif w_type == "EUR":
            wallet_type = Account.EUR

        bank_account = BankAccount(name=name, surname=surname, wallet_type=wallet_type)
        bank_accounts.append(bank_account)
        print("Пользователь создан")

    if command == 2:
        if len(bank_accounts) == 0:
            print("Пользователь не найден")
        else:
            for i in range(len(bank_accounts)):
                print(f"{i + 1}. {bank_accounts[i]}")
            account_num = int(input("Введите номер пользователя:"))

            account = bank_accounts[account_num - 1]

            while True:
                action = int(input(
                    "Выберите ваше действие:\n1. Пополнить баланс\n2. Снять деньги с баланса\n"
                    "3. Конвертировать в другую валюту\n4. Вывести баланс\n5. Установить баланс\n6. Закончить сессию\n"
                ))

                if action == 1:
                    amount = int(input("Введите сумму:"))
                    account.add_to_bank_account(amount=amount)

                if action == 2:
                    amount = int(input("Введите сумму:"))
                    account.subtract_from_bank_account(amount=amount)

                if action == 3:
                    new_w_type = input("Введите новую валюту:")
                    new_wallet_type = Account.KZT
                    if new_w_type == "USD":
                        new_wallet_type = Account.USD
                    elif new_w_type == "RUB":
                        new_wallet_type = Account.RUB
                    elif new_w_type == "EUR":
                        new_wallet_type = Account.EUR
                    account.money_conversion(next_wallet_type=new_wallet_type)

                if action == 4:
                    print(account.get_cash_amount())

                if action == 5:
                    amount = int(input("Введите сумму:"))
                    account.set_cash_amount(cash_amount=amount)

                if action == 6:
                    break

    if command == 0:
        exit()
