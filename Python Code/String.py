#code-1
string="i am   a   Student   "
string2='i am a comsci student' #using double quotes inside single quotes

print(string.title())  # 'I Am   A   Student   '
print(string.upper()) # 'I AM   A   STUDENT   '
print(string.lower())  # 'i am   a   student   '
print(string.capitalize())  # 'I
print(string.strip())  # 'i am   a   Student' (removes leading/trailing whitespace)
print(string.replace("Student", "Human"))  # 'i am   a   Human   '
print(string.split())  # ['i', 'am', 'a', 'Student'] (splits by whitespace)
print(string2.split("a"))  # ['i ', 'm ', ' comsci student'] (splits by 'a')
print(string2.find("comsci"))  # 7 (index of first occurrence)
print(string2.count("m"))  # 2 (number of occurrences)
print(string.startswith("I am"))  # False (case-sensitive)
print(string.endswith("  "))  # True (checks for trailing spaces)
print(string2.index("comsci"))  # 7 (index of first occurrence)
print(string.isalpha())  # False (contains spaces)
print(string.isdigit())  # False (contains letters and spaces)
print(string.isalnum())  # False (contains spaces)
print(string.format(name="Ria", age=20))  # 'i am   a   Student   ' (no placeholders to replace)
print(string2.format(name="Ria", age=20))  # 'i am a comsci student' (no placeholders to replace)
print(string)
print(string2)

#code-2      # Check substring presence
txt = "The best things in life are free!" 
print("free" in txt)  # True
print("expensive" not in txt)  # True
if "free" in txt:
  print("Yes, 'free' is present.") # Yes, 'free' is present.
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  # No, 'expensive' is NOT present.


#code-3      
a = "Hello"
b = "World"
c = a + b
print(c) # HelloWorld
d = a + " " + b
print(d) # Hello World
e = a * 3
print(e) # HelloHelloHello
f = (a + " ") * 3
print(f) # Hello Hello Hello
