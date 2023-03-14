# # 1 python lugati
# py_lugat = {
#     'pop':'sugurib olish',
#     'float':'haqiqiy son',
#     'str':'matn',
#     'append':'royxatga element qoshish metodi',
#     'insert':'royxatga indeks boyicha element qoshish metodi',
#     'del':'royxatdan indeks boyicha element ochirish funk',
#     'remove':'royxatdan elementni ochirish metodi',
#     'reverse':'royxatni teskari qilish',
#     'pop':'royxatdan elementlarni sugurib olish',
#     'get':'lugatni qiymatini chiqarish metodi'
# }
# for soz in sorted(py_lugat):
#     print(f"{soz} - {py_lugat[soz]}")

# 2 davlatalar poytaxtlari
# dav_poy = {
#     'aqsh':'vashington',
#     'uzb':'toshkent',
#     'baa':'makka',
#     'rossiya':'moskva',
#     'italiya':'rim',
#     'fransiya':'parij',
#     'angliya':'london'
# }
# print('Davlatlar:')
# for dav in sorted(dav_poy):
#     print(dav.upper())
# print('Davlatlarning poytaxtlari:')
# for sort_p in sorted(dav_poy.values()) :
#     print(sort_p)

# # 3 
# davlat = input('Istalgan davlatni kiritng:')
# if davlat in dav_poy:
#     print(dav_poy[davlat])
# else: print('Bizda bunday malumot yoq')

# 4 restaron
menu = {
    'somsa':9000,
    'shashlik':7000,
    'xotdog':10000,
    'osh':20000,
    'gumma':5000,
    'chiz':15000,
    'shaverma':14000,
    'kabob':30000,
    'mastava':12000,
    'gril':40000
}
taomlar = []
print('3 ta taom kiriting:')
for n in range(3):
    taom = input(f"{n+1}-taomni kiritng:")
    taomlar.append(taom)
for buyurtma in taomlar:
    if buyurtma in menu:
        print(f"{buyurtma} {menu[buyurtma]} sum")
    else: print(buyurtma,'Bizda bunday taom yoq')