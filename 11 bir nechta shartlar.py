# 1 juft toq
# son = int(input('Juft son kiriting:'))
# if son>0 and son%2 == 0 :
#     print('rahmat')
# else: print('Bu son juft emas')

# 2 muzeyga kirish summasi
# yosh = int(input('Yoshinggiz nechada:'))
# if yosh < 4 or yosh > 60:
#     print('sizga kirish bepul')
# elif yosh < 18:
#     print('Sizga kirish 10000 sum')
# elif yosh >18:
#     print('Sizga kirish 20000 sum')

# 3 sonlarni taqqoslash
# son1 = float(input('1-sonni kiriting:'))
# son2 = float(input('2-sonni kiriting:'))
# if son1 == son2 :
#     print(f'{son1} = {son2}')
# elif son1 >son2 :
#     print(f'{son1} > {son2}')
# else: print(f'{son1} < {son2}')

# 4
# mahsulotlar = ['piyoz','sabzi','tuxum','guruch','kartoshka','gosht','un','suv','olma','tuz']
# savat = []
# print("Kamida 5 ta mahsulot kiriting!")
# for n in range(5):
#     savat.append(input(f'{n+1}-mahsulotni kiriting:'))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f'{mahsulot} dokonimizda bor')
#         else: print(f'{mahsulot} dokonimizda yoq')

# 5 yuqoridagi dasturni ozgartiramiz
# mahsulotlar = ['piyoz','sabzi','tuxum','guruch','kartoshka','gosht','un','suv','olma','tuz']
# print("Kamida 5 ta mahsulot kiriting!")
# bor_mahsulotlar =[]
# mavjud_emas = []
# for n in range(5):
#     mahsulot = input(f"{n+1}-mahsulotni kiriting:")
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else: mavjud_emas.append(mahsulot)
# if mavjud_emas:
#      print('Quyidagi mahsulotlar dokonimizda yoq')
#      for n in mavjud_emas:
#         print(n)
# else: print("Barcha mahsulotlar dokonimizda bor")
    
# 6 foydalanuvchi loginini tekshirish
# foydalanuvchilar = ['admin','dr','aziz','long','uzb']
# login = input('Loginni kiriting:')
# if login in foydalanuvchilar:
#     print('Login band yangi login tanlang')
# else : print(f"Xush kelibsiz {login}")

# 7 qoldiqsiz bolish
son = int(input("Biror butun son kiriting:"))
for n in range(2,11):
    if son%n == 0:
        print(f"{son}, {n} ga qoldiqsiz bo'linadi")
    

