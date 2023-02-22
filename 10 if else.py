# 1 tenglik bn
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else: print(car.title())

# 2 tengsizlik bn
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else : print(car.upper())

# 3 ADMIN
# user = input('Isminggizni kiritning:')
# if user == 'admin' :
#     print(f'Xush kelibsiz {user}.Foydalanuvchilar royxatini korasizmi?')
# else : print(f'Xush kelibsiz {user}!')

# 4 sonlar 
# son1  = int (input('1-sonni kiriting:'))
# son2  = int (input('2-sonni kiriting:'))
# if son1 == son2:
#     print('Sonlar teng ekan',son1,'=', son2)
 
 # 5 + - sonlar
# son = int(input('Istalgan sonni kiriting:'))
# if son > 0:
#     print(f'{son},bu son musbat')
# else: print(f"{son}, bu son manfiy")

# 6 ildiz
son = float(input('Sonni kiriting:'))
if son > 0 :
    print("Bu sonning ildizi",son**(1/2), 'ga teng')
else: print('Musbat son kiriting')