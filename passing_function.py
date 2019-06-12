def foo(foo2):
    return foo2()

def addNums():
    return 2 + 2

# print(foo(addNums))
# print(foo(lambda: 4 + 7))

myList = [1,2,3,4]
print(list(filter(lambda x: x != 1, myList)))

print((lambda x: x * 3)(5))
