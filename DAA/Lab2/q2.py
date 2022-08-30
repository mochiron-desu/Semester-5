arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=int(input("Search element: "))
l,m,r=0,0,len(arr)
while l<=r and arr[m]!=x:
    m=(r+l)//2
    if(arr[m]<x):
        l=m+1
    elif arr[m]>x:
        r=m-1
    else:
        print(m)

# Space complexity: O(1)
# Time complexity:  O(logN)