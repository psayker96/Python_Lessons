
file = open("db.txt","r")
print(file.read())
file.seek(0)
print(file.read())
file.close()


'''
file = open("db.txt","r")

data = file.readlines()
for line in data:
    print(line.strip())
    
file.close()
'''

'''
file = open("db1.txt","w")
file.write("Вітаємо у програмі")
file.close()

file = open("db2.txt","a")
file.write("Вітаємо у програмі з доповненням")
file.close()
'''
