from cusModule import one_line_dir

# mylists = ['apple', 'banana', 'cherry','Math', 'History', 'ComputerSci']
# print(mylists)
# print(mylists[0:2])
# print(len(mylists))
#
# l1 = [True, False, True]
# print(l1)
#

# tuple
# tu1 = ('apple', 'banana', 'cherry','Math', 'History', 'ComputerSci')
# print(tu1)
#
# tu2 = tu1
# # tu2[0] = 'Art'
# print(tu1)
# print(tu2)

# t = ('1', 'a', True)
# t = {'apple': 1, 'banana': 'chilli', 'Zebra': True}


# print(type(t))
# one_line_dir(t)


li1 = ["apple", "banana", "Zebra", "Holo", "Mongo"]

ls = li1.sort(reverse=False)
r = sorted(li1)

print(li1)
print(ls)

print(r)

for j,i in enumerate(li1,start=1):
    print(j, i)

