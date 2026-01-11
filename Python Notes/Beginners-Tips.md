Num-0:In a programming language, instructions(what you want the code to do) are called statements.
Num -1:In Python indentation(Space before a line) is must.
The number of spaces is up to you as a programmer, the most common use is $, but it has to be at least 1,have to use the same number of spaces in the same block of code otherwise error.
Num-2:Python has no command for declaring a variable.variables are created when you assign a value to it.
No, you don't need to mention data type before variable.
Variables gets Overwrite.
Num-3:For multiline statements,write them inside any Brackets (),{},[]
Num-4:  Print Without a New Line- 
             Just use **end=" "**
             After                                            Before
     Code :                                                Code :   
     print("Hello World!", end=" ")                          print("Hello World!")
     print("I will print on the same line.")                 print("I will print on the same line.")
     Output:                                               Output:
     Hello World! I will print on the same line.              Hello World!
                                                              I will print on the same line.
Num-5: Concatenation

Num-6:
 Global Variable fact-
 "If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value."
Num-7:
  Use of global Keyword- 
  Make a local variable into a global variable.
  **There is a big game happening in code 9,10,11**
  Subtle changes but solid effects
  You can see the effect of global and print placement.
    **Code-9**
        *There was no x before the function.
        *Inside the function, global x creates a new global variable and sets it to "fantastic".
        *The first print (inside the function) shows "Python is fantastic".
        *The second print (outside the function) also shows "Python is fantastic" because x now exists globally.

**Code-10**

    * x already existed globally as "awesome".
    *The first print (before the function runs) shows "Python is awesome".
    *The function uses global x and changes x to "fantastic".
    *The second print (after the function) shows "Python is fantastic".

**Code-11**
    *x already existed globally as "awesome".
    *The function changes x to "fantastic" and prints it immediately.
    *So the first output is "Python is fantastic" (inside function).
    *The second print (outside function) also shows "Python is fantastic" because the global x was already changed.*



**Complex Numbers:** 
You cannot compare complex numbers
You cannot convert complex to int or float

**Random Numbers:** 
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers.
