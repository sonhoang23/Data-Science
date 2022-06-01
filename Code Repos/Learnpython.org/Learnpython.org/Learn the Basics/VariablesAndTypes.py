# Variable
from operator import indexOf
from draw import draw_game
# game.py
# import the draw module
import draw as draw_module
from draw import * #import het
myInt = 5
print(myInt)

myfloat = 0.888
print(myfloat)

a, b = 3, 9
print(a + b)

# List
myList = []
myList.append(1)
myList.append(9)
print(myList)

# Basic_Operators

myNumber = 1 + 6 + 9 / 6
print(myNumber)

myNumber1 = 12 / 3**2
# kiểu như 3^2rint(myNumber1)
squared = 7**2
cubed = 2**3
print(squared)
print(cubed)

myNumber2 = 6**2
print(myNumber2)
lotsoofhellos = "hello" * 10
print(lotsoofhellos)

evenArr = [2, 6, 8]
oddArr = [3, 5, 9]
print(oddArr + evenArr)
print(oddArr * 3)

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)
name = "sonhoangdatascience"
age = 24
school = "bk"
print("heloo, %s, age: %d, school: %s" % (name, age, school))
data = (name, age, school)
print("helo %s %d %s" % data)

print(len(name))
print(name.index("n"))
# print(name.index("en"));
print(name.count("p"))
print(name[0:5])
print(name[1:5:9])
# condition
x = 10
y = 11
print(x == 10)
print(x == 8)

if x == 10 and y == 11 or y == 2:
    print("ok")

if x in [10, 81, 21]:
    print("ok")

statement = True
if statement is True:
    print("ok")
    pass
else:
    print("false")
    pass

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

print(not False)
print((not False) == False)

# region LOOP
loops = [2, 5, 6, 9, 8]
for loop in loops:
    # print(loop)
    pass

for x in range(10):
    # print(x)
    pass
for x in range(3, 8, 3):
    print(x)
    pass

count = 0
while count < 10:
    print(count)
    count += 1
    if count >= 5:
        break


count1 = 0
while count1 < 5:
    print(count1)
    count1 += 1
else:
    print("thoát loop")

# Prints out 1,2,3,4
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print(
        "this is not printed because for loop is terminated because of break but not due to fail in condition"
    )
# endregion

# region Functions
def fun1():
    print("fun1")


fun1()
# endregion

# region Class

# endregion

# region Dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook1 = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook1)
# loop
for name, num in phonebook1.items():
    print(name)
    print(num)
# removing
del phonebook1["Jack"]
phonebook.pop("John")
print(phonebook1)

# endregion

# region Modules and Packages
def play_game():
    return "khoong";


def main():
    result = play_game()
    draw_module.draw_game(result)


# this means that if this script is executed, then
# main() will be executed
main()
draw_game("goi mot minh")
# endregion
