import random
import sys
import os

print("Hello World")
#comment
"""
Muliline
"""

name = "Macane"
print(name)

name = 15
print(name)

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2)
print("5 // 2 =", 5//2)

quote = "its only rainy if you say it is"
multi_line_quote = ''' this
is a multiline quote'''

doublequote = quote + " " + quote

print(doublequote)

car_list = ['bugatti', 'ferrari', 'audi']
print(car_list[0])
print(car_list[1:])

double_car_list = [car_list, car_list]
print(double_car_list)

car_list.append('bmw')
car_list.insert(4, 'tesla')

print(car_list)

car_list.remove('bugatti') #too expensive
print(car_list)

car_list.reverse()
print(car_list)

car_list.sort()
print(car_list)

print("Length of Car_List:" + str(len(car_list)))
print("Length of Car_List:",len(car_list))
print("Length of Car_List:" + len(car_list).__str__())

test_tuple = (1, 3, 6)
print("Test Tuple:",test_tuple)

new_list = list(test_tuple)
new_list.append(2)
print("new list:",new_list)

test_tuple = tuple(new_list)
print("Test Tuple:",test_tuple)
test_tuple2 = test_tuple.__add__(tuple(test_tuple))
print("Test Tuple2: ",test_tuple2)


name_dictionary = {'John' : 'Doe', 'Macane' : 'Dunbar'}

print(name_dictionary['Macane'])
del name_dictionary['Macane']
try: print(name_dictionary['Macane'])
except KeyError: print('Good work, Macane is off grid')


if name_dictionary['John'] == 'Doe':
    print("TRUEEEE")

for x in range (0,10):
    print (x)

for x in range (0,10):
    print (x, " ", end="")

for x in range (0,10):
    if x < 9:
        print(x, end="-")
    else: print(x)


num_list = [[1,2,3],[4,5,6],[7,8,9]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y], "~")














