# 1 royxat ustida amallar
# davlatalar = ['Uzb','Rus','Angl','Fra','Ger','Arg']
# # print(davlatalar)
# print(len(davlatalar))
# print(sorted(davlatalar))
# print(sorted(davlatalar,reverse=True))
# print(davlatalar)
# davlatalar.reverse()
# print(davlatalar)
# davlatalar.sort()
# davlatalar.sort(reverse=True)
# print(davlatalar)

# 2 sonlar bilan riyxat tuzish
# sonlar = list(range(120,1201,2))
# # print(sum(sonlar))
# # print(max(sonlar)-min(sonlar))
# print(len(sonlar))
# sonlar1 = sonlar[:21]
# print(sonlar1)
# sonlar2 = sonlar[270:291]
# print(sonlar2)
# print(sonlar[-20:])

#3 
taomlar = ['osh','somsa','gumma','manti','shashlik']
nonushta = taomlar[:]
print(taomlar)
print(nonushta)
nonushta = ['osh','shashlik','manti']
print(nonushta)
nonushta.append('tuxum')
nonushta.append('blinchik')
print(nonushta)
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)