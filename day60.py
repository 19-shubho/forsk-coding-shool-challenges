CUR=input('Enter your currency name: ')

currencyapi = "https://free.currencyconverterapi.com/api/v6/convert?q=USD_INR&compact=ultra&apiKey=7a276e3336d5cd40d295"

import requests

resp=requests.get(currencyapi)

jsonD=resp.json()
