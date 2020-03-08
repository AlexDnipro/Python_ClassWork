import pyowm
from random import randint
from math import pow, pi

owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key



# Search for current weather in your location

location = input("Please enter your city:")
observation = owm.weather_at_place(location)
w = observation.get_weather()
temperature = round(w.get_temperature('celsius')['temp'], 0)

# Weather details
w.get_wind()  # {'speed': 4.6, 'deg': 330}
w.get_humidity()  # 87
print(f"speed:{w.get_wind()['speed']}, deg:{w.get_wind()['deg']} ")
print("Himidility", w.get_humidity())
print("Temperature in " + location + " is :",temperature)

#Task 1: Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число.
#Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем.
#Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
(для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())

def play():
    
    secret_number = randint(1,100)
    user_guess = int(input("Please say a number from 1 to 100:"))
        
    while secret_number!= user_guess:
        if user_guess < secret_number:
            user_guess = int(input("Your number is smaller then should be, please try again:"))
        elif user_guess > secret_number:
            user_guess = int(input("Your number is bigger then should be, please try again:"))
    
    print("Your guess was right!")

play()


# Task 2: Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#(для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).

def rectsquare():
    height = float(input("Please enter height:"))
    width =  float(input("Please enter width:"))
    return height * width

def triangle():
    h = float(input("Please enter height:"))
    base = float(input("Please enter base:"))
    return  0.5 * h * base

def areacircle():
    #PI = 3.14
    radius = float(input("Please enter radius:"))
    return round(pi * pow(radius, 2), 2)

def squarefind():
    choice = float(input("choose 1 - Rectangle 2 - Triangle 3 - Circle:" ))
    if choice == 1:
        return rectsquare()
       
    elif choice == 2:
        return triangle()
        
    elif choice == 3:
        return areacircle()

print(squarefind())