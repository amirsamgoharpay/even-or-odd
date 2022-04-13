
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

