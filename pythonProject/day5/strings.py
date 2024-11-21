#in py no concept of characters
# "" and '' are both same
# strings are immutable str="hello"
# if i wnt to change hellow to hellowworlde
from pyexpat.errors import messages

#
# s="welcome"
# str='welcome'
# s=str("welcome")
# s-str('welcome')

# name=''
# name=""
# name=str('')
# names=str("David")


name="david"
# name[0]="j"       #  change is not possinle because strings are immutable


messages="welcome is the message"
#id used to fetch memory locatins
print(id(messages),"address of welcome is reference")               #1951755233968 address of welcome is reference


messages+="to python"
print(id(messages),"address of welcome is reference")               #2578023431696 address of welcome is reference
#if we compare both address

#concatinaton
str1='sunil'
str2="mudgil"
print(str1+str2)

#    str*2 print's 2 times the string
print(str1*5)






#slicing in string
str3="123456789"
print(str3[:7],"normal indexing")                 #[first is strt :  second should be always len+1 becuse it ignores like for the olast value ]


#reverse indexing
print(str3[1:-1],"reverse indexing")
print(str3[-4:-1],)      #output is 678 here 9 is ignored




#ascii value
print(ord("Z"),"ascii value")
print(chr(64),"is the char form the ascii value 65")
# for i in range(40,100):
#     print(chr(i),end=" ")





#length functiln
print(len("12345"),"length is ")












# in | not     in strings
string="name"
print("nam"in string," it comes under the string")
print("nam"not in string,"nam comes in string byt not changes it back to false")




#string comparision
# it compares each char with its other ASCII vlaue and it doesnot compare length

print("abc"=="abc","in string ccomparison")
print("abc"!="abc","in string ccomparison")
print("abc"<"abc","in string ccomparison")
print("abc">"","in string ccomparison")
print("sunil">="sunil")

