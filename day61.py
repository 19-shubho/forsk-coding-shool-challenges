
currConv='https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=f0b762aa503b35b31af4'

import requests

resp=requests.get(currConv)
jsonD=resp.json()


cityNm=input('Enter city name: ')
gc="http://api.openweathermap.org/geo/1.0/direct?q="+cityNm+"&limit=1&appid=f6a83834813667ac6507638cb6ae37d2"

