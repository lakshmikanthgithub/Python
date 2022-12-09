
print ("\n*****************Lists can be indexed and updated********************\n")

my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']



print ("\n*****************Lists can be nested********************\n")

my_list = [1, 'a', ["list", 64, [0, 1], False]]
print (my_list)


print ("\n*****************List elements and lists can be deleted********************\n")


my_list = [1, 2, 3, 4]
print (my_list)
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]
del my_list  # deletes the whole list


print ("\n*****************Lists can be iterated through using the for loop********************\n")
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

print ("\n*****************Exercise 1********************\n")
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)


print ("\n*****************Exercise 2********************\n")
lst = [1, 3, 5, 1, 9]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
print ("\n*****************Exercise 3********************\n")

lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
