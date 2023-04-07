# # 1
# def kopaytir(*n):
#     a=1 
#     for i in n:
#         a*=i
#     return a
# print(kopaytir(1,2,2,1,2,1,2,1,2,1,2))

# 2
def talaba_haqida(ism,fam,**info):
    info['ismi'] = ism
    info['familiyasi'] = fam
    return info
talaba1 = talaba_haqida('muxtor','asadov',tel = 4334343,t_joyi = 'uzb')
print(talaba1)

