from os import pread


cipher="heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V6E5926A}4 "
decoupeList=[]
prInd=0
for i in range(3,len(cipher),3):
    try:
        decoupeList.append(cipher[prInd:i])
        prInd=i
    except:
        print("error")
        pass

for i in range(len(decoupeList)):
    decoupeList[i]=decoupeList[i][2]+decoupeList[i][0]+decoupeList[i][1]
print(''.join(decoupeList))