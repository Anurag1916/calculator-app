def do_addition(a:int, b:int):
    return a+b

def do_subtraction(a,b):
    return a-b

def do_division(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return "cant devide by zero"