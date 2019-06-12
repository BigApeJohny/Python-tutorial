import functools

def myDecorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!=!")
        func()
        print("After the decorator")
    return function_that_runs_func

@myDecorator
def my_fuction():
    print("I am the function!")

# my_fuction()

def decorator_with_arguments(number):
    def myDecorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator !")
            if number == 56:
                print("Not running the fucntion")
            else:
                func(*args, **kwargs)
            print("After the decorator !")
        return function_that_runs_func
    return myDecorator

@decorator_with_arguments(57)
def foo(x, y):
    print(x + y)

foo(2, 6)
