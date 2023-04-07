# 1
# def user(ism,yosh):
#     '''Foydalanuvchi tugilgan yili'''
#     print(f'{ism.title()}, {2023-yosh} - yilda tugilgan')
# user('anvar',23)

# 2
# def kv_kub(son):
#     print(f"{son}ning kvadrati {son**2}ga teng\n {son}ning kubi {son**3} ga teng")
# kv_kub(4)

# 3 
# def j_t(son):
#     if son % 2 == 1:
#         print(son, 'bu son toq')
#     else: print(son, 'bu son juft')
# j_t(9758)

# 4 
# def taqqosla(son1,son2):
#     if son1 > son2:
#         print(son1,'>',son2)
#     elif son1 == son2:
#         print(son1,'=',son2)
#     else: print(son1,'<',son2)
# taqqosla(43,43)

# 5,6
# def daraja(x,y=2):
#     '''y o'rniga y=2 qoyish ham mumkin'''
#     print(f"{x}ning {y}nchi darajasi {x**y}ga teng")
# daraja(-2,3)

# 7
def qoldsz_bol(son):
    for n in range(2,11):
        if son % n == 0:
            print(f"{son} {n}ga qoldiqsiz bo\'linadi")
qoldsz_bol(70)
