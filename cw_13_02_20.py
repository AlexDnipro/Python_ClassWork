#from math import sqrt
# 1. Find mean

# def meanfind (*args):
#     return sum(args)/len(args)


# #a=(10,20,30)
# print(meanfind(10, 20, 30))

# # 2. Abs

# def absolut (n):
#     return sqrt(n**2)

# print(absolut(-5))

# # 3. Max

# def maxim (a, b):
#     """ Returns max from 2 numbers"""
# #   if a > b:
#         print (a, "is max")
#     elif a == b:
#         print("Numbers are equal")
#     else:
#         print (b, "is max")

# print(maxim.__doc__)

#4. 
# choice = 0

# def rectsquare():
#     height = int(input("Please enter height:"))
#     width = int(input("Please enter width:"))
#     return height * width

# def triangle():
#     h = int(input("Please enter height:"))
#     base = int(input("Please enter base:"))
#     return  0.5 * h * base

# def rectcircle():
#     PI = 3.14
#     radius = int(input("Please enter radius:"))
#     return PI * radius ** 2

# def squarefind():
#     choice = int(input("choose 1 - Rectangle 2 - Triangle 3 - Circle:" ))
#     if choice == 1:
#         return rectsquare()
       
#     elif choice == 2:
#         return triangle()
        
#     elif choice == 3:
#         return rectcircle()
#     else:
#         print("Error")

# print(squarefind())

#5.  Написати функцію, яка обчислює суму цифр введеного числа.

# def sum_of_numbers():
#     number = input("Enter number:")
#     result = sum([int(x) for x in number])
    
#     print(f"Sum of number digits is: {result}")

# sum_of_numbers()

#6. Написати програму калькулятор, яка складається з наступних функцій: 
#головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, калькулятор працює доти,
#поки ми не виберемо дію вийти з калькулятора, після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

# def main_menu():
#     operation = int(input("Choose operation: 1 - Add, 2 - Substruct, 3 - Multiply, 4 - Divide:"))
    
#     if operation == 1:
#         adding()
#     elif operation == 2:
#         substract()
#     elif operation == 3:
#         multiply()
#     elif operation == 4:
#         divide()
#     else:
#         print ("There's no such operation!")
#     print("Thank you for choosing our Calculator!")

# def adding():
#     a = int(input("Enter namber a:"))
#     b = int(input("Enter namber b:"))
#     print (f"Sum of a and b is {a+b}")
# def substract():
#     a = int(input("Enter namber a:"))
#     b = int(input("Enter namber b:"))
#     print (f"Difference between a and b is {a-b}")
# def multiply():
#     a = int(input("Enter namber a:"))
#     b = int(input("Enter namber b:"))
#     print (f"Product of a and b is {a*b}")
# def divide():
#     a = int(input("Enter namber a:"))
#     b = int(input("Enter namber b:"))
#     print (f"Result of division a and b is {a/b}")

# main_menu()

#7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем
# def fib(n):
#     if n<3:
#         return 1
#     return fib(n-1) + fib(n-2)
    
# n=int(input("Input your number for Fibonachi sequence: "))
# for i in range(1,n+1):
#     print(fib(i))

#8.  Написати програму, яка обчислює дискримінант квадратного рівняння
# def discriminant():
#     x = float(input("Enter x:"))
#     y = float(input("Enter y:"))
#     z = float(input("Enter z:"))
#     result = (y ** 2 ) - (4 * x * z)
 #    print(result)
    
# discriminant()