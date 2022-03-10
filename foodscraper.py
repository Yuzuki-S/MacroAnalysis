#!/usr/bin/env python 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

example_page = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=815451&name=arnotts-tim-tam-slams-chocolate-biscuits-dark-chocolate-raspberry'
page = urlopen(example_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('div', attrs={'class': 'product-title span12 mspan12'})
price = soup.find('div', attrs={'class': 'cup-price mspan6'})
nutrition = soup.find('div', attrs={'class': 'nutritionInfo-table'})
servings = soup.find('div', attrs={'class': 'product-details-description'})

print(name_box.h1.text.strip())
print(price.text.strip())
print(re.findall('Energy.+?kJ',nutrition.text.strip()))
print(re.findall('Protein.+?g',nutrition.text.strip()))
print('m1')

print('rebase-third')
print('rebase-four')
print('rebase-six')
print('f1')
print('m2')
print('dev1')
print('m3')
print('rebase1')
print('1')
print('2')
print('3')
print('4')
print('5')
print('6')
print('merge2')
print('pull')
