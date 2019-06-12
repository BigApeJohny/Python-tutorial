#a = True
#if a:
#    print("Hello")

# know_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in know_people:
#     print("You know {}!".format(person))
# else:
#     print("You don't know this person")

## Exercise

def who_do_you_know():
    people = input("Enter the names of people you know, separated by comas: ")
    people_list = people.split(",")
    people_without_spaces = [person.strip() for person in people_list]
    return people_without_spaces

    # people_without_spaces = []
    # for person in people_list:
    #     people_without_spaces.append(person.strip())
    # return people_without_spaces

def ask_user():
    person = input("Enter a name of somone you know: ")
    if person in who_do_you_know():
        print("You know: {} !".format(person))

ask_user()
