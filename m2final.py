for k in range(1,5):
    file = open("F:\KLA\m2\Testcase"+str(k)+".txt")
    out=open("F:\KLA\m2\Test"+str(k)+"out.txt","a")
    data=file.read()
    data=data.split("\n")
    print(data)
    diameter=int(data[0].split(":")[1])
    r=diameter/2
    dielength=int(data[1].split(":")[1].split("x")[0])
    dieheight=int(data[1].split(":")[1].split("x")[1])
    dieShift=(data[2].split(":")[1])
    dieShift=tuple(map(int,dieShift[1:-1].split(",")))
    print(dieShift)
    referenceDie=data[-1].split(":")[1]
    referenceDie=tuple(map(int,referenceDie[1:-1].split(",")))
    print(referenceDie)
    print(diameter)
    print(dielength,dieheight)
    # bottomLeft = (referenceDie[0]-dielength/2,referenceDie[1]-dieheight/2)
    # bottomRight=(bottomLeft[0]+dielength,bottomLeft[1])
    # topRight=(bottomRight[0],bottomRight[1]+dieheight)
    # bottomRight=(bottomLeft[0],bottomLeft[1]+dieheight)
    res={0:""}
    stack=[]
    visit=set()
    def distance(p1,p2):
        return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    def inBoundary(x,y,xr,yr):
        stack.append((x,y,xr,yr))

        while stack:
            x,y,xr,yr = stack.pop()
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
            
            print(x,y)
            res[0]=res[0]+"("+str(xr)+","+str(yr)+")"+":"+str(bottomLeft)+"\n"
            visit.add((x,y))
            stack.append((x+dielength,y,xr+1,yr))
            stack.append((x-dielength,y,xr-1,yr))
            stack.append((x,y+dieheight,xr,yr+1))
            stack.append((x,y-dieheight,xr,yr-1))
            
    inBoundary(referenceDie[0],referenceDie[1],0,0)
    out.write(res[0])




