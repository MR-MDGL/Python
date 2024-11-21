import math
from typing import TextIO

s1="acer"
s2="racb"
a=sorted(s2)
b=sorted(s1)
answer=False
for i in range (len(a)):
    if a[i]==b[i]:
        answer=True

print(answer)

