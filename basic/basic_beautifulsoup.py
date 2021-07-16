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
    print(f"You choose{country[num]['name']}\n currency is {country[num]['currency']}")
    break
  except ValueError : 
    print("Please input number")
  except IndexError:
    print("This number is not in range")