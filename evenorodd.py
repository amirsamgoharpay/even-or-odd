'''x = input("adad ra vared konid : ")
def evenorodd(y):
    y = list(str(y))
    y  = y[-1]
    y = int(y)
    if y%2 == 0 :
        print("even")
    elif y%2 == 1 :
        print("odd")

try :
    x = int(x)
    evenorodd(x)
except ValueError as error :
    print("Invalid")
'''
def eod(x):
    try :
        x = int(x)
        x = list(str(x))
        x = x[-1]
        x = int(x) 
        if x%2 == 0 :
            return "even"
        elif x%2 == 1 :
            return "odd"
    except ValueError as error :
       return "invalid"

