#!/bin/python3

from Phones import Phones

low = Phones('Motorola G7', 30000)
mid = Phones('Samsung A53', 45000)
medium = Phones('Samsung S22 Ultra', 90000)
high = Phones('Iphone 14 Pro Max',  140000)

try:
          phone_budget = float(input('What is your phone budget?'))
except ValueError:
          exit('Please enter a number')
          
for phones in [high, medium, mid, low]:
          phones.buy(phone_budget)
