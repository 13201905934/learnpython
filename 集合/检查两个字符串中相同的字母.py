s1 = input("enter first string: ")
s2 = input("enter second string: ")

ss1 = set(s1)
ss2 = set(s2)
f = ss1.intersection(ss2)
# f1 = list(f)
print("the common letters are: ")
for c in f:
    print(c)
