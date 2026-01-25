matrix_a=[[1,2],[3,4]]
matrix_b=[[5,6],[7,8]]
addition_result=[[0,0],[0,0]]
subtraction_result=[[0,0],[0,0]]
multiplication_result=[[0,0][0,0]]
for i in range(0,2):
    for j in range(0,2):
        addition_result[i][j]=matrix_a[i][j]+matrix_b[i][j]
        subtraction_result[i][j]=matrix_a[i][j]-matrix_b[i][j]
        multiplication_result[i][j]=matrix_a[i][j]*matrix_b[i][j]
print (addition_result)
print (subtraction_result)
print (multiplication_result)