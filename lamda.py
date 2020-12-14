#lamda funnction or ananomus function
def  add(a,b):
    return a+b

minus = lambda a,b:a-b

print(minus(10,5))               #   output = 5

a = [[1,4],[2,5],[2,3]]
# a.sort()
# print("assending  =  ",a)
# a.sort(reverse=True)
# print("desending  =  ",a)

print("a[1] = ",a[1])
a.sort(key=lambda x:x[1])
print("lamda b = ",a)