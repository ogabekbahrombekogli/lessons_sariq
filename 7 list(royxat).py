# 1royxat
# ismlar = ['Anvar','Odil','Shix']
# print('Salom',ismlar[0],',','Qalaysan',ismlar[1],',','Dostim',ismlar[2])

# 2 list arifmetika
# sonlar = [31,23,-4,0,21,1343,-3423,2.3,432.24,-42,4324,0,42342.43]
# qosh = sonlar[-1] + sonlar[3]
# bol = sonlar[3]/sonlar[0]
# print('qoshish:',qosh)
# print('bolish:',bol)
# sonlar[6] = -1
# print(sonlar)
# son1 = sonlar.pop(0)
# print(sonlar, son1)
# sonlar.append(0)
# print(sonlar)
# sonlar.insert(0,0)
# print(sonlar)

# # 3 soz
# t_shaxslar = ['Al-xorazmiy','Al-beruniy','Ibn sino','Pahlovon Mahmud',]
# z_shaxslar = ['Bobur','azam','rustam','abbos','ali','abu']
# t_shaxs1 = t_shaxslar.pop(0)
# z_shaxs1 = z_shaxslar.pop(4)
# print('Men tarixiy shaxslar ichidan', t_shaxs1, ',', 'dostlarimdan esa', z_shaxs1, 'bilan suhbat qurishni istardim!')

# 4 list ustida amallar
friends = []
friends.append('anvar')
friends.append('daston')
friends.append('odil')
friends.append('ali')
friends.remove('ali')
friends.append('aziz')
friends.insert(0,'sasha')
friends.insert(3,'sodiq')
print(friends)

# 5 mehmonga kelgan dostlar
mehmonlar = []
m1 = friends.pop(0)
m2 = friends.pop(3)
m3 = friends.pop(2)
mehmonlar.append(m1)
mehmonlar.append(m2)
mehmonlar.append(m3)
print(mehmonlar)