from collections import defaultdict
import math
k=1
file = open("F:\KLA\m5\Testcase"+str(k)+".txt")
out=open("F:\KLA\m5\Test"+str(k)+"out.txt","a")
data=file.read()
data=data.split("\n")
print(data)
diameter=float(data[0].split(":")[1])
r=diameter/2
dielength=float(data[1].split(":")[1].split(",")[0][1:])
dieheight=float(data[1].split(":")[1].split(",")[1][:-1])
dieShiftx=data[2].split(":")[1].split(',')[0][1:]
dieShifty=data[2].split(":")[1].split(',')[1][:-1]
dieShift=[float(dieShiftx),float(dieShifty)]
print(dielength,dieheight)
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

exclusion = float(data[7].split(":")[-1])
print(exclusion)
coordinates = []

waferCordinates = data[11:]

for t in waferCordinates:
    tempx = float(t.split(",")[0][1:].strip())
    tempy = float(t.split(",")[1][:-1].strip())
    coordinates.append((tempx,tempy))

gripperWidth = float((data[8].split(":")[-1]).split(",")[0][1:])
gripperHeight = float((data[8].split(":")[-1]).split(",")[-1][:-1])
gripperAngles=list(map(float,(data[9].split(":")[-1]).split(",")))


print(gripperAngles)
print(gripperHeight)
print(gripperWidth)
print(coordinates)

rectangle_coordinates = []
# for angle in gripperAngles1:
#     midpoint1=(r*math.cos(math.radians(angle)),r*math.sin(math.radians(angle)))
#     m=math.tan(math.radians(90+angle))
#     dx=gripperHeight/(2*(1+m**2)**0.5)
#     dy=m*gripperHeight/(2*(1+m**2)**0.5)
#     lc1=(midpoint1[0]-dx,midpoint1[1]-dy)
#     lc2=(midpoint1[0]+dx,midpoint1[1]+dy)
#     uc1 = (lc1[0]-gripperWidth*math.cos(math.radians(angle)),lc1[1]-gripperWidth*math.sin(math.radians(angle)))
#     uc2 = (lc2[0]-gripperWidth*math.cos(math.radians(angle)),lc2[1]-gripperWidth*math.sin(math.radians(angle)))
#     rectangle_coordinates.append([lc1,lc2,uc1,uc2])

for angle in gripperAngles:
    midpoint1=(r*math.cos(math.radians(angle)),r*math.sin(math.radians(angle)))
    
    angle_rad=math.radians(angle)
   
    uc1 = (midpoint1[0]+gripperWidth/2*math.cos(angle_rad+math.pi/2),midpoint1[1]+gripperWidth/2*math.cos(angle_rad+math.pi/2))
    uc2 = (midpoint1[0]+gripperWidth/2*math.cos(angle_rad-math.pi/2),midpoint1[1]+gripperWidth/2*math.cos(angle_rad-math.pi/2))
    lc1=(uc1[0]+gripperHeight*math.cos(angle_rad+math.pi),uc1[1]+gripperHeight*math.cos(angle_rad+math.pi))
    lc2=(uc2[0]+gripperHeight*math.cos(angle_rad+math.pi),uc2[1]+gripperHeight*math.cos(angle_rad+math.pi))
    rectangle_coordinates.append([lc1,lc2,uc1,uc2])

print(rectangle_coordinates)



print(rectangle_coordinates)
refDie=[0,0]
res=[""]
ans=defaultdict(list)
stack=[]
visit=set()


def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
def inBoundary(x,y,xr,yr,dr,dc):
    
    
    

    stack.append((x,y,xr,yr,dr,dc))
    while stack:
        distances=[]
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
        distances.append(distance(origin,bottomLeft))
        distances.append(distance(origin,bottomRight))
        distances.append(distance(origin,topLeft))
        distances.append(distance(origin,topRight))
        distances.append(distance(origin,midTop))
        distances.append(distance(origin,midBottom))
        distances.append(distance(origin,midLeft))
        distances.append(distance(origin,midRight))

        if(min(distances)>=r):
            continue      
        if (x,y) == referenceDie:
            refDie[0]=xr
            refDie[1]=yr
            print(xr,yr,"HI")
            print(bottomLeft)
        
        for point in coordinates:
            gripFlag=False
            if distance(origin,point)<r-exclusion:
                if point[0] >bottomLeft[0] and point[0] <bottomRight[0] and point[1] <topLeft[1] and point[1] >bottomLeft[1]:
                    for grip in rectangle_coordinates:

                        lcc1=grip[0]
                        lcc2=grip[1]
                        ucc1=grip[2]
                        ucc2=grip[3]

                        if point[0] < max(lcc1[0],lcc2[0]) and point[0] > min(lcc1[0],lcc2[0]) and point[0] >min(ucc1[0],ucc2[0]) and point[0] <max(ucc1[0],ucc2[0]) and point[1] >min(lcc1[1],lcc2[1]) and point[1] <max(lcc1[1],lcc2[1]) and point[1] >min(ucc1[1],ucc2[1]) and point[1] <max(ucc1[1],ucc2[1]):
                            gripFlag=True
                            break
                    if not gripFlag:  
                        points = (point[0]-bottomLeft[0],point[1]-bottomLeft[1])
                        ans[(xr,yr)].append(points)
                        gripFlag=False


        visit.add((x,y))
        stack.append((round(x+dielength+dieStreet[0],4),round(y,4),xr+1,yr,dr+1,dc))
        stack.append((round(x-dielength-dieStreet[0],4),round(y,4),xr-1,yr,dr-1,dc))
        stack.append((round(x,4),round(y+dieheight+dieStreet[1],4),xr,yr+1,dr,dc+1))
        stack.append((round(x,4),round(y-dieheight-dieStreet[1],4),xr,yr-1,dr,dc-1)) 


        
print(dieShift[0]+dielength/2,dieShift[1]+dieheight/2)
inBoundary(dieShift[0]+dielength/2,dieShift[1]+dieheight/2,0,0,0,0)
print(ans)
for key in ans:
    key2=list(key)
    key2[0]-=refDie[0]
    key2[1]-=refDie[1]
    for point in ans[key]:
        res[0]=res[0]+str(tuple(key2))+":"+str(point)+"\n"
out.write(res[0])

