#inbuilt functions for strings
# cheack weather string contain alpha/numeric
s='abc123'
t="ddddd"
print(t.isalpha())          #string only contain alphabet only    isalpha give true if it contains spaces concider space as numeric value
print("sunil m".isalpha(),"sunil m ")
print("SUNIL".isalpha(),"is for SUNIL")
print(s.isalnum())

print("2020".isalpha(),"for 2020")


print("2020".isnumeric(),"for 2020")


#identifier
print("if".isidentifier(),"is answer for identifier")

print("  ".isspace(),"for space")               #cheack for  spaces in string

#starts with str / ends with str inbuilt methods
print("abcdefghijkl".startswith("abc"),"starts with ")
print("abcdef".endswith("def"),"ends with ")

name="sunilsharma"
print(name.find("l"))
print(name.index("nil"))
print(name.count("s"),'times')



