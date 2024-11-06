'''
import datetime
import random
import math
import re
'''

'''
print(datetime.datetime.now())
'''

'''
from datetime import datetime
print(datetime.now())
'''

'''
from datetime import datetime as dt
print(dt.now())
'''

'''
answer = ["Так","Ні","Мабуть"]

while True:
    question = input("Введіть запитання:")
    print(random.choice(answer))
'''

'''
print(round(random.uniform(1,10),2))
'''

'''
my_text = """
User1 123-127-12-11 123@gmail.com
User2 123-113-12-21 321@ukr.net
User3 123-123-13-21 1234hello@gamil.com
User4 123-124-12-21 321hello@ukr.net
User5 123-123-15-21 1234hello2@gamil.com
User6 121-123-12-21 2323hello4@ukr.net
"""

#pattern =  "\d{3}-\d{3}-\d{2}-\d{2}"
#pattern = "[A-Z][a-z1-9]+"
pattern = "[1-9a-z]+@[a-z]+.[a-z]{3}"
print(re.findall(pattern,my_text))
'''

#PIP


import matplotlib.pyplot as plt

'''
plt.plot([1,2,3,4,5,6,7,8,9,10],
         [1,2,3,4,5,6,7,8,9,10],
         [1,2,3,4,5,6,7,8,9,10],
         [3,1,2,4,3,5,6,4,5,10])


plt.savefig("graph.png")
'''

'''
plt.bar([1,2,3,4,5],[1,2,3,4,5])
plt.show()
'''

import requests

data = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5").json
print(data)
