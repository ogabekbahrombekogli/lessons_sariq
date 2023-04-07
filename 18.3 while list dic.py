mahsulotlar1 ={}
m=1 
print('Mahsulotlar royxatini shakllantiramiz.')
while True:
    mahsulot1 = input(f'{m}-mahsulotni kiriting:')
    narx = input('Mahsulotning narxini kiriting:')
    mahsulotlar1[mahsulot1] = narx
    m+=1
    savol = input('Yana mahsulot kirtasizmi? ha/yoq ')
    if savol == 'ha':
        continue
    else : break
###
mahsulotlar = []
n=1
while True:
    mahsulot = input(f'{n}-mahsulotni kiriting:')
    mahsulotlar.append(mahsulot)
    n+=1
    key = input('Yana mahsulot qoshasizmi? ha/yoq ')
    if key == 'yoq':
        break
    elif key == 'ha':
        continue
# 3
while mahsulotlar:
    mah = mahsulotlar.pop()
    if mah in mahsulotlar1:
        print(mahsulotlar1[mah])
    else: print('Bizda bunday mahsulot yoq')
