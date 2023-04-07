def tub(a,b):
    tub_sonlar = []
    for n in range(a,b+1):
        son =True
        if n == 1:
            son = False
        elif n == 2:
            son =True
        else :
            for x in range(2,n):
                if n % x == 0:
                    son = False
        if son:tub_sonlar.append(n)
    return tub_sonlar
a = int(input("1-oraliqni kiriting:"))
b = int(input("2-oraliqni kiriting:"))
print(tub(a,b))
