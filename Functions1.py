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
 -------------------------
#define function
def getGreeting(name):

    #if name is empty or null
    if not name:
        #Returns a value.
        #And function ends here.
        return "Hello every body!"


    #if name is not empty and not null (not None),
    #this code will be executed.
    else:
        return "Hello " + name

#Call function, pass parameters to function.
greeting = getGreeting("")

print(greeting)

greeting = getGreeting('Python')

print(greeting)

-------------------------

def showInfo(name, gender):

    print("Name: ", name);
    print("Gender: ", gender);


#valid
showInfo("Train", "Male")

#Invalid==>Error!!

showInfo("Train")
'''''''''''''''''

def showInfo(name, gender = 'Male', country = 'US'):

    print("Name: "+name)
    print("Gender: "+gender)
    print("Country: "+country)


showInfo("Aladdin","Male","India")
print("--------")

showInfo("Tom","Male")

print("-----------")

showInfo("Jerry")

print("-----------")

showInfo(name = "Tintin", country = 'France')


















































