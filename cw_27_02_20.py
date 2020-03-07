#1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
try:
    custom_number = int(input("Please enter integer number: "))
    if custom_number % 2 == 0 :
        print("The number is even")
    else:
        print("The number is odd")
except ValueError:
    print("Sorry, the number is not valid")
except TypeError:
    print("The type you entered is wrong!")

#2. Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом.
#  Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
#  Головний код має викликати функцію, яка обробляє введену інформацію.

class NegativeAge(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)


try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise NegativeAge("Age can't be negative!")
    if age % 2 == 0:
        print("The age number is even")
    elif age % 2 !=0:
        print("The age number is odd")
except TypeError:
    print("The type you entered is wrong!")
except ValueError:
    print("Wrong value!")

#3. Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
#передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.

try:
    x, y = eval(input("Please enter 2 numbers separated by come: "))
    
    z =  x / y
    print(z)

except ZeroDivisionError:
    print("You can't divide by zero!!")
except SyntaxError:
    print("Coma is missing. Please enter 2 numbers separated by coma!")
#65866hgjh75785
except:
    print("Wrong input")
else:
    print("No exceptions. You entered valid numbers")
finally:
    print("Good bye!")

#4. Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу 
#  (1 це Понеділок, 2 це Вівторок і т.д.). Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.

week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

class OutOfIndexRange(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)
try:
    day = int(input("Please enter the number: "))
    if day <= 0 or day > 7:
        raise OutOfIndexRange("No week day corresponding to the number!")
    else:
        print(week[day])

except OutOfIndexRange as o:
    print(f"Custom exception:{o.data}")
except SyntaxError:
    print("Please enter valid number!")
except ValueError:
    print("Please enter correct number!")
finally:
    print("End of the program!")