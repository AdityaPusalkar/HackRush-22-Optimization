import math
from random import randint

def notworthit(numjam, area, currjam):
    return (200*numjam*currjam - 100*currjam**2 > 0.7*area)
N,R = map(int, input().split())
bombs = []
for _ in range(N):
    a,b,c = map(int, input().split())
    bombs.append([c,a,b])
bombs.sort(reverse=True)
bombedges = [[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if((abs(bombs[i][1]-bombs[j][1])**2+abs(bombs[i][2]-bombs[j][2])**2)<=max(bombs[i][0]**2,bombs[j][0]**2)):
            bombedges[i].append(j)
            bombedges[j].append(i)
visbomb = [False for _ in range(N)]
ind = 0
numjam = 0
jammerslist = []
clusterjams = []
while(ind<N):
    if(visbomb[ind]):
        ind+=1
        continue
    visbomb[ind]=True
    bombscluster = [ind]
    queue = [ind]
    left = bombs[ind][1]
    right = bombs[ind][1]
    top = bombs[ind][2]
    bottom = bombs[ind][2]
    while(queue):
        curr = queue.pop(0)
        for node in bombedges[curr]:
            if(not visbomb[node]):
                bombscluster.append(node)
                queue.append(node)
                visbomb[node] = True
    area = 0
    for bomb in bombscluster:
        left = min(left, bombs[bomb][1])
        right = max(right, bombs[bomb][1])
        top = max(top, bombs[bomb][2])
        bottom = min(bottom, bombs[bomb][2])
        area += 3.14*bombs[bomb][0]**2
    startX = left+R/2
    startY = bottom+R/2
    currbombs = 0
    addconst = 1.73
    jammers = []
    if(max(1,(math.ceil((right-left-R)/(addconst*R)))+1)*max(1,(math.ceil((top-bottom-R)/(addconst*R)))+1)>len(bombscluster)):
        while(bombscluster):
            bomb = bombscluster[randint(0,len(bombscluster)-1)]
            jammers.append([bombs[bomb][1], bombs[bomb][2]])
            numjam+=1
            bombscluster.remove(bomb)
            for newbomb in bombscluster:
                if((abs(jammers[-1][0]-bombs[newbomb][1])**2 + abs(jammers[-1][1]-bombs[newbomb][2])**2)<=R*R):
                    bombscluster.remove(newbomb)
    else:
        jammers.append([startX, startY])
        numjam += 1
        while(startX<=right-R/2+addconst*R):
            startY = bottom+R/2
            while(startY<=top-R/2+addconst*R):
                if(currbombs==0):
                    currbombs+=1
                else:
                    jammers.append([startX,startY])
                    currbombs+=1
                    numjam += 1
                startY += R*addconst
                if(currbombs==1):
                    break
            startX += R*addconst
            if(currbombs==1):
                break
    jammerslist.append([jammers,True])
    clusterjams.append(area)
    ind+=1
for i in range(len(jammerslist)):
    currjam = len(jammerslist[i][0])
    if(notworthit(numjam, clusterjams[i], currjam)):
        jammerslist[i][1] = False
        numjam -= currjam
print(numjam)
for jammers in jammerslist:
    if(jammers[1]):
        for jammer in jammers[0]:
            print(jammer[0], jammer[1])
    