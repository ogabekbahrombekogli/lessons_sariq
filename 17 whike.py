# 1
# kitob = ''
# while kitob != 'stop':
#     kitob = input('Yaxshi korga kitoblaringgizni kiriting:')
#     if kitob != 'stop':
#         print('kitob')

#2.1
# while True:
#     yosh = input('Yoshingiz nechada ?')
#     if yosh == 'exit'or yosh == 'quit':
#         break
#     elif int(yosh) < 7:
#         print('Chipta 2000 som')
#     elif int(yosh) >=7 and int(yosh) <=18:
#         print('Chipta 3000 som')
#     elif int(yosh) >= 18 and int(yosh) <= 65:
#         print('Chipta 10000 som')
#     elif int(yosh) >65:
#         print('Chipta bepul')

# 3
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    if qiymat<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    

