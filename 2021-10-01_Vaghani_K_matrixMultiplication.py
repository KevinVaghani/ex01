A=[]
print("Enter value for first matrix")
for i in range(3):
    a=[]
    for j in range(3):
        j=int(input("enter input for ["+str(i)+"]["+str(j)+"]"))
        a.append(j)
    A.append(a)
B=[]
print("Enter value for second matrix")
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("enter input for ["+str(i)+"]["+str(j)+"]"))
        b.append(j)
    B.append(b)

print("Value of first matrix")
for i in range(3):
    for j in range(3):
        print(A[i][j],end=" ")
    print()

print("Value of second matrix")
for i in range(3):
    for j in range(3):
        print(B[i][j],end=" ")
    print()

print("Multiplication of two 3*3 matrix")

result=[]
for i in range(3):
    result.append([])
    for j in range(3):
        sum=0
        for k in range(3):
            sum=sum+(A[i][k]*B[k][j])
        result[i].append(sum)
        
for i in range(3):
    for j in range(3):
        print(result[i][j],end=" ")
    print()

