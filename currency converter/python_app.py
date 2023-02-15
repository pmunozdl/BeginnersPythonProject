#pip install forex-python

from forex_python.converter import CurrencyRates

cr = CurrencyRates()

def exchange():
    amount = int(input("Enter the amount you want to convert: "))
    list = ["EUR - Euro Member Countries \n","IDR - Indonesia Rupiah\n","BGN - Bulgaria Lev\n" ,"ILS - Israel Shekel\n", "GBP - United Kingdom Pound\n" ,"DKK - Denmark Krone\n" ,"CAD - Canada Dollar\n" , "JPY - Japan Yen\n" ,"HUF - Hungary Forint\n", "RON - Romania New Leu\n" ,"MYR - Malaysia Ringgit\n" ,"SEK - Sweden Krona\n", "SGD - Singapore Dollar\n", "HKD - Hong Kong Dollar\n","AUD - Australia Dollar\n" ,"CHF - Switzerland Franc\n", "KRW - Korea (South) Won\n", "CNY - China Yuan Renminbi\n","TRY - Turkey Lira\n","HRK - Croatia Kuna\n","NZD - New Zealand Dollar\n","THB - Thailand Baht\n","USD - United States Dollar\n" ,"NOK - Norway Krone\n","RUB - Russia Ruble\n","INR - India Rupee\n" ,"MXN - Mexico Peso\n" ,"CZK - Czech Republic Koruna\n" ,"BRL - Brazil Real\n","PLN - Poland Zloty\n","PHP - Philippines Peso\n","ZAR - South Africa Rand\n"]
    print("Choose the currency that has to be converted: \n")
    for i in list:
        print(i)
    from_currency = input("Enter the code:").upper()
    print("Choose the currency that has to convert: \n")
    for i in list:
        print(i)
    to_currency = input("Enter the code:").upper()
    print("You are converting", amount, from_currency, "to", to_currency)
    output = cr.convert(from_currency, to_currency, amount)
    print("The converted rate is:", output)

exchange()


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
