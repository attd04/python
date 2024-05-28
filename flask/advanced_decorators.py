inputs = eval(input())

# TODO: create logging_decorator() function

def logging_decorator(function):
    def wrapper(*args):
        function_name = function.__name__
        print(f"You called {function_name}{args}")
        calc = function(args[0], args[1], args[2])
        print(f"The result is {calc}")
    return wrapper


# TODO: use decorator

@logging_decorator
def a_function(a, b, c):
    return a*b*c


a_function(inputs[0], inputs[1], inputs[2])
