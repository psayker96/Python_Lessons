'''
import turtle
from tkinter import Button

pero = turtle.Turtle()
pero.speed(1000)
pero.color("green")

def image():
    for number in range(200):
        pero.forward(number)
        pero.left(number)

btn = Button(text="Вперед",command=lambda:pero.forward(10)).pack()
btn2 = Button(text="Вліво",command=lambda:pero.left(10)).pack(side="left")
btn3 = Button(text="Вправо",command=lambda:pero.right(10)).pack(side="right")
btn4 = Button(text="Image",command=image).pack()
'''
#-------------------------------------------------------
'''
class Car:
    speed = 0

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        if speed > 0:
            self.speed -= 5

my_car = Car()

while True:
    choice = input("""1 - Speed Up
2 - Speed Down
q - Quit
Choose option""")
    if choice == "1":
        my_car.speed_up
    if choice == "2":
        my_car.speed_down
    if choice == "q":
        break
    print(f"Speed is {my_car.speed}")
'''
