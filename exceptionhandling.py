
print("enter number 1")
num1 = input()
print("enter number 2 ")
num2 = input()

"""print("the sum of this two number is ",int(num1)+int(num2))
print("this line is important")  #this line is not printed  hence we use exception handling


output :-
enter number 1
10
enter number 2
e
Traceback (most recent call last):
  File "C:/my python projects/exceptionhandling.py", line 5, in <module>
    print("the sum of this two number is ",int(num1),int(num2))
ValueError: invalid literal for int() with base 10: 'e'
"""

try :
    print("the sum of this two number is ",
          int(num1) + int(num2))
except Exception as a :
    print(a)

print("this line is important")

"""
output 1:-
enter number 1
q
enter number 2
1
invalid literal for int() with base 10: 'q'
this line is important

output 2:-
enter number 1
10
enter number 2
20
the sum of this two number is  30
this line is important

Process finished 

"""