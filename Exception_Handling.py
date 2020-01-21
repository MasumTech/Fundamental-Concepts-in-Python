'''
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not divide by zero")
    except TypeError:
        print("Unsupported type. Did you use string?")
        


print(div(10,2))
print(div(3,0))
print(div(9,3))
print(div("12", 3))
'''

import io
filename = "file1.txt"
mode = "w"


try:
    with open(filename, mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(filename, "not found. Please check if the file's name is corrent.")
    
except io.UnsupportedOperation:
    print("Are you sure", filename, "is readable?")
