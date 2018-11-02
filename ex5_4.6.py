from random import *
N =100000
sequence = ['车','羊1','羊2']
first,change=0,0
for i in range(times):
    x=random.choice(a)
    y=random.choice(a)
    if x==y:
        first +=1
    else:
        change +=1
print("坚持初心获得胜利的概率;{:.2f}%".format(first/times*100))
print("坚持改变初心获得胜利的概率;{:.2f}%".format(change/times*100))
