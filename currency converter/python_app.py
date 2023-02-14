#pip install forex-python
# from forex_python.converter import CurrencyRates

# cr = CurrencyRates()

# amount = int(input("Enter the amount you want to convert: "))

# from_currency = input("Enter the currency code that has to be converted: ").upper()

# to_currency = input("Enter the currency code to convert: ").upper()

# print("You are converting", amount, from_currency, "to", to_currency)

# output = cr.convert(from_currency, to_currency, amount)

# print("The converted rate is:", output)

def from_currency():
    list = ["EUR - Euro Member Countries","IDR - Indonesia Rupiah","BGN - Bulgaria Lev" ,"ILS - Israel Shekel", "GBP - United Kingdom Pound" ,"DKK - Denmark Krone" ,"CAD - Canada Dollar" , "JPY - Japan Yen" ,"HUF - Hungary Forint", "RON - Romania New Leu" ,"MYR - Malaysia Ringgit" ,"SEK - Sweden Krona", "SGD - Singapore Dollar", "HKD - Hong Kong Dollar","AUD - Australia Dollar" ,"CHF - Switzerland Franc", "KRW - Korea (South) Won", "CNY - China Yuan Renminbi","TRY - Turkey Lira","HRK - Croatia Kuna","NZD - New Zealand Dollar","THB - Thailand Baht","USD - United States Dollar" ,"NOK - Norway Krone","RUB - Russia Ruble","INR - India Rupee" ,"MXN - Mexico Peso" ,"CZK - Czech Republic Koruna" ,"BRL - Brazil Real","PLN - Poland Zloty","PHP - Philippines Peso","ZAR - South Africa Rand","BTC - Bitcoin"]
    print("Choose the currency that has to be converted:", list)
    currency = input("Enter the code: ").upper()
    
from_currency()
# EUR - Euro Member Countries 
# IDR - Indonesia Rupiah 
# BGN - Bulgaria Lev 
# ILS - Israel Shekel 
# GBP - United Kingdom Pound 
# DKK - Denmark Krone 
# CAD - Canada Dollar 
# JPY - Japan Yen 
# HUF - Hungary Forint 
# RON - Romania New Leu 
# MYR - Malaysia Ringgit 
# SEK - Sweden Krona 
# SGD - Singapore Dollar 
# HKD - Hong Kong Dollar 
# AUD - Australia Dollar 
# CHF - Switzerland Franc 
# KRW - Korea (South) Won 
# CNY - China Yuan Renminbi 
# TRY - Turkey Lira 
# HRK - Croatia Kuna 
# NZD - New Zealand Dollar 
# THB - Thailand Baht 
# USD - United States Dollar 
# NOK - Norway Krone 
# RUB - Russia Ruble 
# INR - India Rupee 
# MXN - Mexico Peso 
# CZK - Czech Republic Koruna 
# BRL - Brazil Real 
# PLN - Poland Zloty 
# PHP - Philippines Peso 
# ZAR - South Africa Rand
# BTC - Bitcoin