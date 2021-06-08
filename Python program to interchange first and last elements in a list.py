list = [1,2,3,4,5,6,7]
s = len(list)

temp = list[0]
list[0] = list[s-1]
list[s-1] = temp

print(list)