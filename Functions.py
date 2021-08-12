a = int(input("Enter value a "))
b = int(input("Enter value b "))
print(sum((a,b))) #built in functions

def func1(a,b):
    """This Function returns you Average of two numbers"""# docstring
   # print('Average of numbers: ',int((a+b)/2))
    return int((a+b)/2)

func1(12,12)
v= func1(13,13)
print(v) # will return None
print(func1.__doc__)