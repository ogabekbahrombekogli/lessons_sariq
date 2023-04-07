mahsulotlar ={}
n=1 
print('Mahsulotlar royxatini shakllantiramiz.')
while True:
    mahsulot = input(f'{n}-mahsulotni kiriting:')
    narx = input('Mahsulotning narxini kiriting:')
    mahsulotlar[mahsulot] = narx
    n+=1
    savol = input('Yana mahsulot kirtasizmi? ha/yoq ')
    if savol == 'ha':
        continue
    else : break
# print('Mahsulotlar:')
# for value,keys in mahsulotlar.items():
#     print(value, keys)
print(mahsulotlar.values())