#1.
names = ['Sam', 'Don', 'Daniel'] 
names = map(hash,names)
print(list(names))

#2.
colors = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']

def isRed(str):
    return str == 'red'

new_colors = filter(isRed,colors)
print(list(new_colors))

#3.
str_list = ['1','2','3','4','5','7']
num = []
for i in str_list:
    num.append(int(i))
    
num_list = map(int,str_list)
print(num)

#4. 
f = lambda x: round(x * 1.6, 2)
miles = [1,2,3]
km = map(f,miles)
print(list(km))