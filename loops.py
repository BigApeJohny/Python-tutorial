var = "Hello world !"

#for char in var: #iterable are string, list, tuplets and more
#    print(char)
#
#arr = [1,3,4,5,6,7]
#
#for num in arr:
#    print(num ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = input("Should we print again? (y/n) ")
    if user_input == 'n':
        user_wants_number = False
