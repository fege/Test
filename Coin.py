'''
Created on 24/ago/2012

@author: fede
'''
CASH = [100,50,20,10,5,1]
class InvalidAmount(ValueError): pass
def MakeChange(amount):
    money = []
    if amount <= 0:
        raise InvalidAmount('amount must be positive!')
    for coin in CASH:
        num = amount/coin
        money += [coin] * num
        amount -= coin * num
    return money

        