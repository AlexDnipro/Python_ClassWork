# a = int(input("Enter a:"))
# b = int(input("Enter b:"))


# if a < b:
#  #   print("%d is bigger than %d" %(b, a))
#      print("{} is bigger than {}".format(b, a))
# else:
#     print("%d is bigger than %d" %(a, b))

# c = int(input("Enter C:"))
# if c%2 == 0:
#     print("%d is even" %c)
# else:
#     print("%d is odd" %c)

# i = 1
# fact = 1
# while i <= c:
#     fact = fact * i
#     i += 1

# print(fact)

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number {0} is even".format(num))
# else:
#     print("The number {0} is odd".format(num))

# for i in range(100):
#     if i % 2 != 0:
#         print(i)
#     else:
#         continue

# i = 1
# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#         i += 1
#     else:
#         i += 1
#         continue

# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#         i += 1
#     else:
#         i += 1

# spisok = [5, 9, 10, 20]
# for i in spisok:
#     if i % 2 == 0:
#         print("Found even number {0}".format(i))
#         break
#     else:
#         continue

# print(list(range(0,100,2)))

#spisok = list(range(0,20,2))

# i = 0
# N = len(spisok)
# while i < N:
#      spisok[i] = float(spisok[i])
#      i += 1
# print(spisok)
# print(type(spisok[3]))



#Fibonacci
n = int(input("Please enter number n:"))

elements = [1,1]

for i in range(2,n):
    elements.append(elements[i-1] + elements[i-2])
    if elements[i] >= n:
        del elements[i]
        break
    else:
        continue

print(elements)