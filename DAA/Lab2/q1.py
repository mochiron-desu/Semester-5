arr=[]
n=int(input("Enter the number of values to be added: "))
for i in range(n):
    a=input("Enter the value to be added: ")
    arr.append(a)
print("Current array is ",arr)
x=input("Enter the value to be serched: ")
for i in range(n):
    if arr[i]==x:
        print("Value found at index ",i+1)

# space complexity:O(N)
# Time complexity: O(N) 