class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        self.usd = 'usd'
        self.eur = 'eur'
        self.jpy = 'jpy'
        self.btc = 'btc'

    @property
    def currency_type(self):
        if self.currency.lower() == self.usd:
            return self.amount
        elif self.currency.lower() == self.eur:
            return self.amount * 1.1
        elif self.currency.lower() == self.jpy:
            return self.amount * 0.011065
        elif self.currency.lower() == self.btc:
            return self.amount * 531.40
        else:
            return "Invalid Input"

    def __str__(self):
        return "{}".format(self.currency_type)

    def __eq__(self, other):
        return self.currency_type == other.currency_type

    def __ne__(self, other):
        return self.currency_type != other.currency_type

    def __add__(self, other):
        return Money(self.currency_type + other.currency_type, self.currency)

    def __sub__(self, other):
        return Money(self.currency_type - other.currency_type, self.currency)

    def __lt__(self, other):
        return self.currency_type < other.currency_type

    def __le__(self, other):
        return self.currency_type <= other.currency_type

    def __gt__(self, other):
        return self.currency_type > other.currency_type

    def __ge__(self, other):
        return self.currency_type >= other.currency_type
