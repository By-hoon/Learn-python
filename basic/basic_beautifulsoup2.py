# print(format_currency(5000, "KRW", locale="ko_KR"))
# from babel.numbers import format_currency

import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

result = requests.get("https://www.iban.com/currency-codes")

soup = BeautifulSoup(result.text, 'html.parser')

country = []

tbody = soup.find("tbody")
country_tr = tbody.find_all("tr")
for i in country_tr:
  country_td = i.find_all("td")
  if country_td[1].text == 'No universal currency':
    continue
  else:
    country_info = {
    'name' : (country_td[0].text).capitalize(), 
    'currency':country_td[2].text
    }
    country.append(country_info)
for i in range(len(country)):
  print(f"{i}: {country[i]['name']}")
while(True):
  try:
    num = int(input("Choice number!"))
    print(f"1. {country[num]['name']}")
    while(True):
      try:
        num2 = int(input("Choice one more!"))
        print(f"1. {country[num2]['name']}")
        c1 = country[num]['currency']
        c2 = country[num2]['currency']
        url = f"https://wise.com/gb/currency-converter/{c1}-to-{c2}-rate?amount=50"
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        exchange_rate = soup.find("span", {"class" : "text-success"})
        while(True):
          try:
            num3 = int(input(f"How many {c1} do you want to convert to {c2}?"))
            mul = round((num3 * float(exchange_rate.text)), 3)
            print(f"{num}{c1} is {mul}{c2}")
            break
          except ValueError : 
            print("Please input number")
          except IndexError:
            print("This number is not in range")
        break
      except ValueError : 
        print("Please input number")
      except IndexError:
        print("This number is not in range")
    break
  except ValueError : 
    print("Please input number")
  except IndexError:
    print("This number is not in range")