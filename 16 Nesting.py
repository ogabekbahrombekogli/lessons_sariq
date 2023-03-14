# # 1 shaxslar haqida malumot
# shaxs1 = {'al-xorazmiy':'783-yilda Xiva shahrida tugilgan'}
# shaxs2 = { 'beruniy':'973-yilda Xorazmda tugilgan'}
# shaxs3 = {'ibn sino':'980-yilda Buxoro viloyatida tugilgan'}
# shaxs4 = {'Komiljon':'1917-yilda Shovot tumanida tugilgan'}
# shaxslar = [shaxs1,shaxs2,shaxs3,shaxs4]
# for Shaxs in shaxslar:
#     for shaxs_i,shaxs_m in Shaxs.items():
#         print(f"{shaxs_i.title()},{shaxs_m}.",end='')

# # 2 shaxslarning asarlari
# shaxs1 = {'al-xorazmiy':['al-jabr','arifmetika']}
# shaxs2 = { 'beruniy':['saydana','gedeziya']}
# shaxs3 = {'ibn sino':['risola','ash shifo']}
# shaxs4 = {'Komiljon':['vatan','xorazm']}
# shaxslar = [shaxs1,shaxs2,shaxs3,shaxs4]
# for Shaxs in shaxslar:
#     for shaxs_i,shaxs_k in Shaxs.items():
#         print(f"{shaxs_i.title()}ning mashhur asarlari: ")
#         for asar in shaxs_k:
#             print(asar)

# # 3 dostlar kinolari
# dostlar = {
#     'Aziz':['odob','terminator','odamlar'],
#     'Rustam':['forsaj1','forsaj2','forsaj3'],
#     'Odil':['hayot','axloq','snayper']
# }
# for k,q in dostlar.items():
#     print(f"{k}ning sevimli kinolari:")
#     for kino in q :
#         print(kino)

# #4 davlatlar haqida malumot
# davlatlar = {
#     'uzb':{
#         'poytaxti':'toshkent',
#         'hududi':448978,
#         'aholisi':33000000,
#         'puli':'sum'
#     },
#     'rus':{
#         'poytaxti':'moskva',
#         'hududi':17098246,
#         'aholisi':144000000,
#         'puli':'rubl'
#     },
#     'aqsh':{
#         'poytaxti':'vashington',
#         'hududi':9631468,
#         'aholisi':327000000,
#         'puli':'dollar'
#     }
# }
# for k1,q1 in davlatlar.items():
#     print(k1)
#     for k2,q2 in q1.items():
#         print(k2,q2)

# 5
davlatlar = {
    'uzb':{
        'poytaxti':'toshkent',
        'hududi':448978,
        'aholisi':33000000,
        'puli':'sum'
    },
    'rus':{
        'poytaxti':'moskva',
        'hududi':17098246,
        'aholisi':144000000,
        'puli':'rubl'
    },
    'aqsh':{
        'poytaxti':'vashington',
        'hududi':9631468,
        'aholisi':327000000,
        'puli':'dollar'
    }
}

davlat = input("Davlatni kiriting:")
if davlat in davlatlar:
    for k,q in davlatlar[davlat].items():
        print(k,q)
else: print('Bizda bunday davlat mavjud emas!')