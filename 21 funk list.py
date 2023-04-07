# 1 , 2
#  def katta_harf(ismlar):
#     ism = []
#     for n in ismlar:
#         i = n.title()
#         ism.append(i)
#     return ism
# ism = ['ali','akmal','otabek','rustam']
# print(katta_harf(ism))
# print(ism) 
 
# 3 
def bahola(ismlar):
    baholar ={}
    for i in ismlar:
        baho = int(input(f"{i}ni bahosini kiriting:"))
        baholar[i] = baho
    return baholar
Ismlar = ['ali','rustam','odil']
print(bahola(Ismlar))
print(Ismlar)