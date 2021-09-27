# Task 6.6
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores
# information about exchange rates to your default currency:
# exchange_rate = {
#     "EUR": 0.93,
#     "BYN": 2.1,
#     ...
# }
# Example:
# x = Money(10, "BYN")
# y = Money(11) # define your own default value, e.g. “USD”
# z = Money(12.34, "EUR")
# print(z + 3.11 * x + y * 0.8) # result in “EUR”
# >>543.21 EUR
#
# lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
# s = sum(lst)
# print(s) #result in “BYN”
# >>123.45 BYN
# Have a look at @functools.total_ordering


from functools import total_ordering

@total_ordering
class Money:

    exchange_rate = {"BYN": 1.00, "USD": 2.50, "EUR": 2.93, "JPY": 0.023, "RUR": 0.034}

    def __init__(self, sum, currency):
        self.sum = float(sum)
        self.currency = currency
        self.sum_byn = self.sum * self.exchange_rate[self.currency]

    def __eq__(self, other):
        return self.sum_byn == other.sum_byn

    def __lt__(self, other):
        return self.sum_byn < other.sum_byn

    def __str__(self):
        return f"{self.sum} {self.currency}"

    def __add__(self, other):
        sum = round((self.sum_byn + other.sum_byn) / self.exchange_rate[self.currency], 2)
        return Money(sum, self.currency)

    def __radd__(self, other):
        """other can be only 0"""
        if other == 0:
            return self

    def __mul__(self, other):
        """other can be int and float"""
        mul = round((self.sum_byn * other) / self.exchange_rate[self.currency], 2)
        return Money(mul, self.currency)


#  Test
# byn = Money(12, "BYN")
# usd = Money(10, "USD")
# eur = Money(72.24, "EUR")
# rur = Money(1587, "RUR")
#
#
# print(rur)
# print(byn * 3.7)
# print(usd + byn)
# print(eur + byn)
# print(eur + byn + byn + eur)
# lst = [Money(10,"RUR"), Money(10, "USD"), Money(10, "EUR"), Money(10587, "RUR")]
# aaa = lst[0] + lst[1] + lst[2] + lst[3]
# print(aaa)
# s = sum(lst)
# print(s)
# print(s * 3)
















