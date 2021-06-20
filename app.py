from module_class import GetInfo
from module import *

data = {}
data['exchangeRate'] = []
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'USD',
    'saleRateNB': 27.0275,
    'purchaseRateNB': 27.0275,
    'saleRate': 27.18,
    'purchaseRate': 26.75
})
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'PLZ',
    'saleRateNB': 7.2526,
    'purchaseRateNB': 7.2526,
    'saleRate': 7.35,
    'purchaseRate': 7.05
})
data['exchangeRate'].append({
    'baseCurrency': 'UAH',
    'currency': 'EUR',
    'saleRateNB': 32.7722,
    'purchaseRateNB': 32.7722,
    'saleRate': 32.95,
    'purchaseRate': 32.35
})


# us = GetInfo(
#     'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014')
# print(us.show_object())


# write_json('file/file_1.json', data)
