#1 lugat
# otam = {'ismi':'Bahrombek','t_yili':1973,'t_joyi':'Xorazm','manzili':'Yangiariq'}
# print(f"Otamning ismi {otam['ismi']},{otam['t_joyi']} viloyatida\
#  {otam['manzili']} tumanida, {otam['t_yili']}-yilda tug'ilgan.")

# 2
# taomlar = {'onam':'osh','otam':'shashlik','opam':'somsa','bobom':'mastava','buvim':'shorva'}
# print(f"onamning sevimli taomi {taomlar['onam']}")
# print(f"otamning sevimli taomi {taomlar['otam']}")
# print(f"opamning sevimli taomi {taomlar['opam']}")

# 3 python
py_lugat = {
    'pop':'sugurib olish',
    'float':'haqiqiy son',
    'str':'matn',
    'append':'royxatga element qoshish metodi',
    'insert':'royxatga indeks boyicha element qoshish metodi',
    'del':'royxatdan indeks boyicha element ochirish funk',
    'remove':'royxatdan elementni ochirish metodi',
    'reverse':'royxatni teskari qilish',
    'pop':'royxatdan elementlarni sugurib olish',
    'get':'lugatni qiymatini chiqarish metodi'
}
soz = input('Biror soz kiriting:')
# print(py_lugat.get(soz,'Bunday soz mavjud emas!'))

# 4 if else bilan 
if soz in py_lugat:
    print(py_lugat[soz])
else: print('Bunday soz mavjud emas!')
