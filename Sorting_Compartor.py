d=[["amy", 100],["david", 100],["heraldo", 50],["aakansha", 75],["aleksa", 150]]
for z in range(0,len(d)):
    for i in range(z,len(d)):


        if d[z][0]>d[i][0]:
            d[z], d[i] = d[i], d[z]

        if d[i][1]>d[z][1]:
            d[z],d[i]=d[i],d[z]


print(d)
