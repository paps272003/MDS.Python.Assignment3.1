def myfilter(fnc, l):
    result=[]
    for i in l:
        if fnc(i):
            result.append(i)
    return result