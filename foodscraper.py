#!/usr/bin/env python 
from urllib.request import urlopen
from bs4 import BeautifulSoup

example_page = 'https://shop.countdown.co.nz/shop/productdetails?stockcode=815451&name=arnotts-tim-tam-slams-chocolate-biscuits-dark-chocolate-raspberry'
page = urlopen(example_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('div', attrs={'class': 'product-title span12 mspan12'})
price = soup.find('span', attrs={'class': 'price din-medium'})


print(name_box.h1.text.strip())
print(price.text.strip())

