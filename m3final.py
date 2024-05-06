k=4
file = open("F:\KLA\m3\Testcase"+str(k)+".txt")
out=open("F:\KLA\m3\Test"+str(k)+"out.txt","a")
data=file.read()
data=data.split("\n")
print(data)
diameter=float(data[0].split(":")[1])
r=diameter/2
dielength=float(data[1].split(":")[1].split("x")[0])
dieheight=float(data[1].split(":")[1].split("x")[1])
dieShiftx=data[2].split(":")[1].split(',')[0][1:]
dieShifty=data[2].split(":")[1].split(',')[1][:-1]
dieShift=[float(dieShiftx),float(dieShifty)]

print(dieShift)

referenceDie=data[3].split(":")[1]
referenceDie=tuple(map(float,referenceDie[1:-1].split(",")))
dieStreet=data[4].split(":")[1]
dieStreet=tuple(map(float,dieStreet[1:-1].split(",")))
reticleStreet=data[5].split(":")[1]
reticleStreet=tuple(map(float,reticleStreet[1:-1].split(",")))
diesPerRow= int(data[6].split(":")[1].split("x")[0])
diesPerCol = int(data[6].split(":")[1].split("x")[1])
print(referenceDie)

diesCount=[diesPerRow,diesPerCol]

refDie=[0,0]
res=[""]
ans={}
stack=[]
visit=set()
def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
def inBoundary(x,y,xr,yr,dr,dc):
    
    
    

    stack.append((x,y,xr,yr,dr,dc))
    while stack:
        x,y,xr,yr,dr,dc = stack.pop()
        if dr==diesCount[1]:
            dr=0
            x+=reticleStreet[0]
        if dc==diesCount[0]:
            dc=0
            y+=reticleStreet[1]
        if dr==-1:
            x-=reticleStreet[0]
            dr=diesCount[1]-1
        if dc==-1:
            y-=reticleStreet[1]
            dc=diesCount[0]-1
        

        bottomLeft = (x-dielength/2,y-dieheight/2)
        bottomRight=(x+dielength/2,y-dieheight/2)
        topRight=(x+dielength/2,y+dieheight/2)
        topLeft=(x-dielength/2,y+dieheight/2)
        midTop=((topLeft[0]+topRight[0])/2,(topLeft[1]+topRight[1])/2)
        midRight=((bottomRight[0]+topRight[0])/2,(bottomRight[1]+topRight[1])/2)
        midLeft=((topLeft[0]+bottomLeft[0])/2,(topLeft[1]+bottomLeft[1])/2)
        midBottom=((bottomLeft[0]+bottomRight[0])/2,(bottomLeft[1]+bottomRight[1])/2)
        origin=(0,0)
       
        
        if (x,y) in visit:
            continue
        if(distance(origin,bottomLeft)>=r and distance(origin,bottomRight)>=r and distance(origin,topLeft)>=r and distance(origin,topRight)>=r and distance(origin,midTop)>=r and distance(origin,midBottom)>=r and distance(origin,midLeft)>=r and distance(origin,midRight)>=r): 
            continue       
        if (x,y) == referenceDie:
            refDie[0]=xr
            refDie[1]=yr
            print(xr,yr,"HI")
            print(bottomLeft)
        print(xr,yr,x,y)
        
        ans[(xr,yr)]=bottomLeft
        visit.add((x,y))
        stack.append((round(x+dielength+dieStreet[0],4),round(y,4),xr+1,yr,dr+1,dc))
        stack.append((round(x-dielength-dieStreet[0],4),round(y,4),xr-1,yr,dr-1,dc))
        stack.append((round(x,4),round(y+dieheight+dieStreet[1],4),xr,yr+1,dr,dc+1))
        stack.append((round(x,4),round(y-dieheight-dieStreet[1],4),xr,yr-1,dr,dc-1))


        
print(dieShift[0]+dielength/2,dieShift[1]+dieheight/2)
inBoundary(dieShift[0]+dielength/2,dieShift[1]+dieheight/2,0,0,0,0)
for key in ans:
    key2=list(key)
    key2[0]-=refDie[0]
    key2[1]-=refDie[1]
    
    res[0]=res[0]+str(tuple(key2))+":"+str(ans[key])+"\n"
out.write(res[0])
print(dieShift[0]+dielength/2,dieShift[1]+dieheight/2)

print(refDie)
