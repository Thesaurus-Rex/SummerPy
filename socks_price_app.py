# Nov2018 Tutorial
# price of chair
from typing import Optional, Any

_author_ = 'devi'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.sockdreams.com/dreamer-proud-stripes-otk.html") #gets site
#price: <span class="price">$18.00</span>

content = request.content  # stores it
soup = BeautifulSoup(content, "html.parser")   # runs it through BS as html
element = soup.find("span", {"class":"price"})  #  searches by dictionary pair

print(element.text.strip())  # prints string of search results

string_price = element.text.strip() #stores string value
price_no_symbol = string_price[1:] # implied default [0:end] #copies into new var

num  = (float(price_no_symbol)) #convert to float

print(num)

if num < 15:
    print("it's on sale!")
else:
    print("Regular price: {}".format(num))

