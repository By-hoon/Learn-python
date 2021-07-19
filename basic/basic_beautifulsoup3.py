import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

result = requests.get(alba_url)
soup = BeautifulSoup(result.text, 'html.parser')

file = open("albas.csv", mode="w")
writer = csv.writer(file)
writer.writerow(["local", "name", "time", "pay", "regis_day"])
one = soup.find("div", {"id" : "MainSuperBrand"})
two = one.find("ul", {"class" : "goodsBox"})
three = two.find_all("li")
for threes in three:
  if threes['class'][0] != 'noInfo':
    four = threes.find("a", {"class" : "goodsBox-info"})
    alba_url2 = four['href']
    result2 = requests.get(alba_url2)
    soup2 = BeautifulSoup(result2.text, 'html.parser')
    one2 = soup2.find("div", {"id" : "NormalInfo"})
    two2 = one2.find("table")
    three2 =two2.find("tbody")
    four2 = three2.find_all("tr")
    for ff in four2:
      print(ff.text)
      if ff.text != "채용공고가 없습니다.":
        if ff['class'] != "summaryView":
          five2 = ff.find_all("td")
          try:
            six = five2[1].find("a")
            seven = six.find("span")
            local_name = (five2[0].text).replace('\xa0', " ")
            writer.writerow([local_name, seven.text, five2[2].text, five2[3].text, five2[4].text])
          except:
            continue
file.close()