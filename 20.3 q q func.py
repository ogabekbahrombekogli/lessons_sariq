def fibonachi(n):
    sonlar =[]
    for x in (range(n)):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-2] + sonlar[x-1])
    return sonlar
print(fibonachi(12))