''''
contains key value pair
keys cant be changed
keys are unique
changes allowed at value level not key level

'''
# create an empty dictionary
# newdata={}
# print(newdata)
#
# # dictionary with data
# newdata={"name": "sunil", "age": 23}
# print(type(newdata))

#-----------------------------creating dictionary with  list for tuples
# list 000 not possible because list is mutable
# tupledict=dict([(),()])


#u------------------------------sing dict() constructor
# newdict=dict(name="sunil",age=22)
# print(type(newdict),newdict)


#----------------------------using square brackets
# mydict={"name": "sunil", "age": 23}
# print(mydict["name"])
# print(mydict["sub"])        #KeyError: 'sub'



# ---------------------using .get()
# print(mydict.get("name"))


# ---------------------modifying dictionary-------------------------
# mydict={"name": "sunil", "age": 23}
# print(mydict,"before age update")
# mydict["age"]=24
# print(mydict,"after age update")

#-----adding new pair
# mydict["city"]="bhiwani"
# print(mydict)



#---del value pair
# del mydict["city"]
# print(mydict)
# del mydict              #delete whole dictionary
# print(mydict)



# #----using pop
# print(mydict,'before')
# mydict.pop("city")
# print(mydict,'after')
#
#
#
# #----using popitem
# print(mydict,'before')
# mydict.popitem()                #removes last added value
# print(mydict,'after')



#-------------------------------dictionary methods
#keys
# print(mydict.keys(),"---using keys")                #print keys return only set of keys
#
#
# #values
# print(mydict.values())              #returns only the set of values
#
# #item()
# print(mydict.items(),"----using item")               #return   tuples with key and value
#
#
# #update            update single or multiple values at the same time
# dict1={"name":"sunil","age":23}
# dict2={"dept":101,"city":"los angles"}
# dict2.update(dict1)
# print(dict1)
#
#
# #copy
# newdict=dict1.copy()
# print(newdict,"-------new dictionary")


# fromkeys():  create copy of the dictionary with specfied keys with the same value
# keys=[1,2,3,4]
# defaultvalue='welcome'
# finaldict=dict.formkeys([1,2,3,4],"welcomehey")
# print(finaldict)







#setdefault()               set default if not given by user
# mydict={"name": "sunil", "age": 23}
# mydict.setdefault("pin",127021)
# # print(mydict)

# -----------iterate dictionary
#using for loop
# for i in mydict:
#     print(i)

# to print values
# for key,value in mydict.items():
#     print(f"key and value are {key} and {value}")



#-------------dictionary compression
# square={x: x**2 for x in range(0,11)}           #createing dictionary with formula
# print(square)               #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}




#--------------------nested dictionary
#dictionary isnide dictionary

mydict={
    "p1":{"name": "sunil", "age": 23},
    "p2":{"name": "marle", "age": 33}

}
print(mydict["p1"]["name"])
print(mydict["p2"]["name"])


# union
dict1={"name": "sunil", "age": 23}
dict2={"name": "sunil", "age": 23}
