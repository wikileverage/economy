class Economy:
    def __init__(self):
        self.markets = []


class Market:
    def __init__(self, product_name):
        self.product_name = product_name
        self.transactions = []


class EconomicActor:
    def __init__(self, assets, liabilities):
        self.assets = assets
        self.liabilities = liabilities

    @property
    def equity(self):
        return self.assets - self.liabilities


class CashTransaction:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """    
    def __init__(self, buyer, seller, product, amount, currency):
        self.buyer = buyer  # the economic actor providing payment
        self.seller = seller  # the economic actor providing the product (good/service/financial asset)
        self.amount = amount  # the amount of actual cash changing hands at the exchange of the product
        self.currency = currency  # the currency in which the cash_amount is denominated


class CreditTransaction:
    def __init__(self, buyer, seller, currency, amount, repayment_date, interest_rate):
        self.buyer = buyer  # the economic actor providing payment
        self.seller = seller  # the economic actor providing the product (good/service/financial asset)
        self.currency = currency  # the currency in which the cash_amount is denominated
        self.amount = amount  # the amount of money to be paid for the product
        self.repayment_date = repayment_date  # the date at which the loan provided for the purchase of the product
        # must be repaid
        self.interest_rate = interest_rate  # the amount of interest to be paid for the loan provided for the purchase
        # of the product
