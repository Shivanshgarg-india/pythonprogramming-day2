# Question1

try:
    x = 3
except:
    print('x value is 3')
else:
    print('something went worng')

# output--- something went worng

# Question2

try:
    a = float(input("enter a number"))
    b = float(input("enter number"))


    def div(a, b):
        return a / b


    print(div())
except:
    print("can't be divided by zero")
# output--- can't devided by zero you enter the like this 2/0
# you enter 4/2 now answer is 2

# Question3

a = 20
try:
    print(a)
except:
    print("somthing went worng")
finally:
    print("welcome to data loves cloud servies")




# Question4
try:
    def name(a=int(input("enter a age"))):
        if (a >= 18):
            print("you are elder")
        else:
            print("you are minior")


    name()
except:
    print("value error")
else:
    print("something went worng")

# output ---your input according

# Question5
a = 2000
if (200 < 2000):
    raise Exception("sorry the number is 300")

# raise Exception is make a error