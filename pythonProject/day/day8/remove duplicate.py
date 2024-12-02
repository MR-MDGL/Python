# remove duplicate from a list
newlist=[1, 2, 2, 3, 4, 5, 4, 6]
# print(newlist)
num =[]
for i in range(0,len(newlist)):
    for j in range(i+1,len(newlist)):

        if(newlist[i]==newlist[j]):
            continue
        else:
            num.append(newlist[i])

print("after duplicate remove", num)
