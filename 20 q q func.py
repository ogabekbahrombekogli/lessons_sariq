# 1 
def user(ism,fam,t_yil,t_joy,email='',t_r=None):
    dic = {'ismi':ism,
           'familiyasi':fam,
           't_yili':t_yil,
           't_joyi':t_joy,
           'emaili':email,
           'tel':t_r,
           'yoshi':2023-t_yil
           }
    return dic
user1 = user('rustam','azamatov',1999,'turin')
mijozlar = []
while True:
    ism =input('Ismni kiriting:')
    fam = input('Familiyani kiritng:')
    t_y = int(input('Tugilgan yilni kiritng:'))
    t_j = input("Tug\'ilgan joyni kiriting:")
    em = input("email:")
    tel = input('tel raqam:')
    mijozlar.append(user(ism,fam,t_y,t_j,em,tel))
    a =input('Yana davom etasizmi? ha/yoq')
    if a == 'yoq':
        break
n=1
for mijoz in mijozlar:
    print(f"{n}-user")
    n+=1
    for q,k in user(ism,fam,t_y,t_j,em,tel).items():
        print(q,':',k)
        
