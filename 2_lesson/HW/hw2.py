#Task 1
print("Task 1")
print("-"*25)
data = [[1,2,3],[4,5,6],[6,7,8,[155]]]
print(f"Прямий порядок data[2][3][0]: {data[2][3][0]}")
print(f"Зворотній порядок data[-1][3][0]: {data[-1][3][0]}")
print("-"*25)

data2 = {'1':'1',
         '2':'2',
         '3':'3',
         '4':[{'5':'5',
               '6':[155]}]}
print(data2['4'][0]['6'][0])
print("-"*25)

data3 = [{1:2,
          2:3,
          3:[4,5,6,7,{8:9,
                      10:[3,2,1,[155]]}]}]
print(data3[0][3][4][10][3][0])
print("-"*25)

data4 = {"1":"1",
         "2":[1,2,3,4,5,6,7,8,9,10,
              [3,2,4,1,2,3,4],
              [3,2,4,3,5,4,{"1":1,
                            "2":2,
                            "3":{"result":[1,2,3,4,155]}},6,5,7,6,9],
              [1,3,2,4,3,5,4,6,5]]}
print("Вивід двома способами, подробиці в коді!")
print(data4["2"][-2][6]['3']['result'][-1])
print(data4["2"][11][6]['3']['result'][4])
print("-"*25)
print("="*25)
print("Task 2")
print("-"*25)

product = {"name":"Name of product",
           "description":"Product description",
           "Price":123.85}

article = {"title":"Article title",
           "text":"Text of article",
           "description":"Article sescription"}

staff = {"name":"Name of staff member",
         "positoin":"Position of staff member",
         "office":{"city":"Name of city where is office located",
                   "number":"Code number of the office branch",
                   "type":"Type of office, remote or official"}}

print(f"Вивід словника про товар: {product}")
print("-"*25)
print(f"Вивід словника про статтю: {article}")
print("-"*25)
print(f"Вивід словника про працівника: {staff}")
print("-"*25)



