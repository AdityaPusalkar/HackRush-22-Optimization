def notworthit(numjam, radius):
    return (200*numjam - 100 > 0.7*3.14*radius**2)
N,R = map(int, input().split())
bombs = []
for _ in range(N):
    a,b,c = map(int, input().split())
    bombs.append([c,a,b,_])
bombs.sort(reverse=True)
bombedges = {}
for i in range(len(bombs)):
    bombedges[i] = 0
for i in range(len(bombs)):
    for j in range(i+1,len(bombs)):
        if((abs(bombs[i][1]-bombs[j][1])**2+abs(bombs[i][2]-bombs[j][2])**2)<=bombs[i][0]**2):
            bombedges[i]+=1
        if((abs(bombs[i][1]-bombs[j][1])**2+abs(bombs[i][2]-bombs[j][2])**2)<=bombs[j][0]**2):
            bombedges[j]+=1
numjam = 0
jammers = []
while(len(bombs)):
    num = 0
    jammers.append([bombs[num][1], bombs[num][2], bombs[num][0], bombs[num][3]])
    numjam+=1
    bombs.remove(bombs[num])
    for bomb in bombs:
        if((abs(jammers[-1][0]-bomb[1])**2 + abs(jammers[-1][1]-bomb[2])**2)<=R*R):
            bombs.remove(bomb)
truejam = [True for _ in range(numjam)]
for i in range(len(jammers)):
    if(notworthit(numjam, jammers[i][2]) and bombedges[jammers[i][3]]==0):
        truejam[i] = False
        numjam-=1
print(numjam)
for i in range(len(jammers)):
    if(truejam[i]):
        print(jammers[i][0], jammers[i][1])