def inc():
    global op
    op+=1

op = 0
# Actual program
n = int(input("Enter number of student details to be entered: "))
inc()
for i in range(n):
    inc()
    name= input("Enter Student name: ")
    inc()
    id = input("Enter ID: ")
    inc()
    gender = input("Enter Gender: ")
    inc()
    interest = str(input("Enter Interest: "))
    inc()
    i=i+1
    inc()
    print("=================================\nStudent Name:",name,"\nStudent ID:",id,"\nSex:",gender,"\nStudent Interest:",interest,"\n================================")
    inc()

inc()
print("Total number of operations",op)
