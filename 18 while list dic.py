# mahsulotlar = []
# n=1
# while True:
#     mahsulot = input(f'{n}-mahsulotni kiriting:')
#     mahsulotlar.append(mahsulot)
#     n+=1
#     key = input('Yana mahsulot qoshasizmi? ha/yoq ')
#     if key == 'yoq':
#         break
#     elif key == 'ha':
#         continue
# print('Sizning mahsulotlaringgiz:')
# for n in mahsulotlar:
#     print(n)
mahsulotlar = ['olma','anor','orik']
mahsulotlar1 = {'nok': 3000,'olma':2000}
while mahsulotlar:
    mah = mahsulotlar.pop()
    if mah in mahsulotlar1:
        print(mahsulotlar1[mah])
    else: print('Bizda bunday mahsulot yoq')

