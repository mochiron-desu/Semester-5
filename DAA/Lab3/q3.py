a = []
b = []
i = 0
n1 = int(input("Enter the number of elements for A: "))
for i in range(0, n1):
    temp = int(input("Enter sorted element %s: " % (i + 1)))
    a.append(temp)

if (a != sorted(a)):
    print("A is not sorted")
    exit()
print()

n2 = int(input("Enter the number of elements for B: "))
for i in range(0, n2):
    temp = int(input("Enter sorted element %s: " % (i + 1)))
    b.append(temp)

if (b != sorted(b)):
    print("B is not sorted")
    exit()
print()
print("List A: ", a)
print("List B: ", b)

c = a+b
c.sort()
print(c)
if ((n1 + n2) % 2 != 0):
    print(c[len(c) // 2])
else:
    print((c[(len(c) // 2)-1] + c[(len(c) // 2)])/2)
