# Before                                            
print("Hello World!")
print("I will print on the same line.") 

# After use of end=""                                            
print("Hello World!", end=" ")
print("I will print on the same line.") # will have both text in same line

# code -2
print("I am", 35, "years old.") # showing int+text together

#code-3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(z)
print(type(x))

#code-4

x, y, z = "Orange", "Banana", "Cherry"  #Many Values to Multiple Variables
print(x)
print(y)
print(z)

#code-5
x = y = z = "Orange" #One Value to Multiple Variables
print(x)
print(y)
print(z)

#code-6
fruits = ["apple", "banana", "cherry"] #Unpack a Collection,allows you to extract the values into variables
x, y, z = fruits
print(x)
print(y)
print(z)

                                               #global vs. local variables
#code-7         #global variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#code-8      #local variable with same name as global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#code-9      #global keyword to access global variable inside a function  or make a variable global
def myfunc():
  global x  #declare x as global
  x = "fantastic"
  print("Python is " + x)
myfunc()

print("Python is " + x)   #Python is fantastic
                          #Python is fantastic


#code-10      #global keyword to change a global variable inside a function
x = "awesome"       
def myfunc():
  global x
  x = "fantastic"
print("Python is " + x)
myfunc()
print("Python is " + x)   #Python is awesome
                          #Python is fantastic


#code-11
x = "awesome"       
def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)     #Python is fantastic
                            #Python is fantastic

