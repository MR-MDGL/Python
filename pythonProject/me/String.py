s1 = input("enter string")
dictionary = {}

for i in s1:
    if i==" ":
        continue
    elif i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i] = 1

for i in s1:
    if dictionary[i] == 1:
        print("first non-repeating character is:", i)
        break
# print(dictionary)
