def function1(a, b):
    """this is a function which will calcualte average of two numbers"""
    print("you are in function 1")
    average = (a+b)/2
    average = int(average)
    return average
z = function1(3, 5)
print(z)
print(function1.__doc__)