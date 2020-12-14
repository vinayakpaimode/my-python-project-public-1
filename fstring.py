
import math
me = "harry"
a = "this is %s ",me
print(a)                                 ##('this is %s ', 'harry')


c = "this is {1}    {0} "
b = c.format(me,a)
print(b)


d = f"this is{me}   {math.cos(60)}"
print(d)