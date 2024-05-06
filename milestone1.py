import numpy as np
import math

for k in range(1,5):
    file = open("F:\KLA\m1\Testcase"+str(k)+".txt")
    out=open("F:\KLA\m1\Test"+str(k)+"out.txt","a")
    data=file.read()
    data=data.split("\n")
    print(data)
    diameter=data[0].split(":")
    noOfPoints=int(data[1].split(":")[1])
    angle=int(data[2].split(":")[1])

    d=int(diameter[1])
    radius=d/2
    endpoint2=(radius*math.cos(math.radians(angle)),radius*math.sin(math.radians(angle)))
    endpoint1=(radius*np.cos(math.radians(180+angle)),radius*np.sin(math.radians(180+angle)))
    equidistant_points = []

    equidistant_points.append(endpoint1)

    for d in range(1,noOfPoints-1):
            # Calculate the ratio for linear interpolation
        
            
            # Use linear interpolation formula to find the intermediate point
            a=endpoint1[0]+d/(noOfPoints-1)*(endpoint2[0]-endpoint1[0])
            b=endpoint1[1]+d/(noOfPoints-1)*(endpoint2[1]-endpoint1[1])
            equidistant_points.append((a,b))
    equidistant_points.append(endpoint2)
    string=""
    for i in equidistant_points:
            string+=str(i)+"\n"
    print(string)
    out.write(string)

    