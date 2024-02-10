from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
import time

url = 'https://ru.investing.com/currencies/usd-rub-historical-data'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")
date = soup.findAll("td", {"class": "datatable_cell__LJp3C text-left align-middle overflow-hidden text-v2-black text-ellipsis whitespace-nowrap text-sm font-semibold leading-4 min-w-[106px] left-0 sticky bg-white sm:bg-inherit"})
money = soup.findAll("td", {"class": "datatable_cell__LJp3C datatable_cell--align-end__qgxDQ datatable_cell--up__hIuZF text-right text-sm font-normal leading-5 align-middle min-w-[77px] rtl:text-right")
print (money)
m1 = []
m2 = []
for i in range(len(money)):
    i = date[i].text
    i = i[:5]
    print(i)
    m1.append(i)
for g in range(len(money)):
    m2.append(money[g].text)
m1.reverse()
m2.reverse()
print(m2)
print(m1)

plt.figure(figsize=(60, 60))
plt.plot(m1, m2, ':o')
plt.xlabel("Дата")
plt.ylabel("Доллар в рублях")
plt.show()
