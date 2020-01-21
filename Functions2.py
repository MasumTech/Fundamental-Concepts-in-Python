'''''''''''''''
#defien a funtion:

def sayHello(name):
    #if name is empty or null.
    if not name:
        print("Hello every body!!")

     #if name is not empty or not null 
    else:
            print("Hello " + name)

#Call funtion, pass parameters to funtion.
sayHello("")
sayHello("Python")
sayHello("Java")
 
'''''''''''''''''

#define funtion
def getGreeting(name):

    #if name is empty or null
    if not name:
        return "Hello every body!"

    else:
        return "Hello " + name

greeting = getGreeting("")

print(greeting)

greeting = getGreeting('Python')

print(greeting)








































