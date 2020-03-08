# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сatch the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# ############################################################
# def new_ball():
#     global x,y,r,ball_number
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     canv.create_text(90,20,text=f"SCORE:{points} out of {ball_number}", font = 'Arial 20')
    
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
#     ball_number += 1
###################################################################

 # функція, яка провіряє, чи не лежить 
 # точка event.x,event.y дальше, ніж r 
 # від точки x,y. Для цього, з допомогою
 # теореми Піфагора ми знаходимо
 # відстань між двома точками і порівнюємо 
 # з радіусом круга.
 #  
 # якщо відстань(гіпотенуза) більша за радіус 
 # круга, то клік відбувся зовні круга
 #  
 # якщо відстань(гіпотенуза) менша за радіус 
 # круга, то клік відбувся всередині круга    
     
# def click(event):
#     global points
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1 #змінна підрахунку кількості співпадінь (вгадувань)
 
# points = 0
# ball_number = 0
# new_ball()
# canv.bind('<Button-1>', click)
 
# mainloop()

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сatch the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     #виводити рахунок в консоль незручно
#     #зручніше його вивести на canvas
#     #використавши функцію canv.create_text()
#     canv.create_text(60,20,text="Score: "+str(points), font = 'Arial 20')
    
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
     
     
# def click(event):
#     global points
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
 
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)
 
# mainloop()

from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Сatch the BALL")
 
canv = Canvas(root,bg='grey')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r,ball,text,ball_number, points
    canv.delete(ball)
    canv.delete(text)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    text = canv.create_text(90,20,text=f"SCORE:{points} out of {ball_number}", font = 'Arial 20')
    root.after(1000,new_ball)
    ball_number += 1

def click(event):
    global x, points
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = -1000
#видалення круга при кліку
        canv.delete(ball)


#щоб не можна було «накручувати» очки, 
# клікаючи багато разів по кругу, 
# поки він не зникне

#Після кліку круг не зникає і це не ok.
#Можна видалити все 
# canv.delete(ALL), 
# але тоді буде видалятись і рахунок

#краще дати імена всім графічним примітивам
# (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
#щоб можна було видалити ball, треба перед викликом 
#функції ball() намалювати цей ball
points = 0
ball_number = 0
ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(90,20,text="",font = 'Arial 20')
new_ball()
canv.bind('<Button-1>', click)


mainloop()