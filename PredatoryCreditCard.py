class CreditCard:
    '''A Customer Credit card'''
    def __init__(self, customer, bank, account, limit):
        '''Create a new credit card instance

        The initial balance is Zero
        
        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        '''

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount



class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self, apr):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor

acc = PredatoryCreditCard('Uday', 'SBI', '123456789', 10000, 15)
print(acc.charge(5000))
print(acc.get_balance())
print(acc.process_month(15))

