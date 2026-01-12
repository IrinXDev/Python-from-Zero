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


#code-12                                 Data Types in Python
z = complex(2, 5)
print(z)                                  #(2+5j)


#code-13               Access real and imaginary parts
z = 3 + 4j

print(z.real)   # 3.0
print(z.imag)   # 4.0
print(z.conjugate())  # (3-4j)
print(type(z))  # <class 'complex'>

#code-14               Convert to complex number
x = 2     # int   
y = 3.5   # float

a = complex(x)      # convert int to complex
b = complex(y)      # convert float to complex
print(a)    # (2+0j)
print(b)    # (3.5+0j)
print(type(a))  # <class 'complex'>
print(type(b))  # <class 'complex'>

#code-15               Arithmetic Operations with Complex Numbers
a = 2 + 3j
b = 1 + 4j
print(a + b)  # (3+7j)
print(a - b)  # (1-1j)
print(a * b)  # (-10+11j)
print(a / b)  # (0.8235294117647058-0.29411764705882354j)

#code-16               
# Conjugate of a complex number
a = 2 + 3j
conjugate_a = a.conjugate()
print(conjugate_a)  # (2-3j)

#code-17
import random

print(random.randrange(1, 10))  # prints a random integer from 1 to 9
print(random.choice(['apple', 'banana', 'cherry']))  # prints a random fruit from the list
print(random.random())   # prints a random float between 0.0 and 1.0
print(random.uniform(1.5, 10.5))  # prints a random float between 1.5 and 10.5
print(random.sample(range(1, 100), 5)) # prints a list of 5 unique random numbers from 1 to 99
print(random.shuffle([1, 2, 3, 4, 5]))  # shuffles the list in place
print(random.choices(['red', 'blue', 'green'], weights=[10, 5, 1], k=3)) # prints 3 random colors with specified weights
print(random.sample(['red', 'blue', 'green', 'yellow'], 2)) # prints 2 random colors from the list
print(random.choice('abcdefghij')) # prints a random character from the string

#code-18                   string join() Method
print("Items: " + ", ".join(["apple", "banana"]))  # Items: apple, banana

#code-19                   
first="I am ria"
sec="I am a comsci std"

print(first+"\n"+sec)

#code-20                  
