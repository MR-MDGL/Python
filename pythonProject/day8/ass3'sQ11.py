# Write a Python program to compress a string by replacing consecutive repeating characters
# with the character followed by its count.
# aabbcccc      input
# a2b2c4        output


s = "aabbcccc"
c = ""
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        c += s[i - 1] + str(count)
        count = 1
c += s[-1] + str(count)
print("Compressed string:",c)
