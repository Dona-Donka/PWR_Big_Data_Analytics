# list 01 task 2/4
# Explain Gaussian method of computing an inverse of a matrix. 
# Implement this method

print("matrix: ")
#M <- matrix(c(0, 2, 3, 7), 2, 2)
M <- matrix(c(2,6,5,5,3,-2,7,4,-3), 3,3)
M

A <- cbind(M, diag(nrow(M)))

for (col in 1:ncol(M))
{
    if (A[col,col] == 0) {
        for (r in 2:nrow(A)){
            A[c(col,r),] <- A[c(r,col),]
        }       
    }
    
    A[col,] <- A[col,] / A[col,col]  
    
    for (row in 1:nrow(M)){
        if (row != col){ A[row,] <- A[row,] - A[row,col]*A[col,] }
        }
    }
print("Result: ")
A

# list 01 task 3/4
# Explain Gaussian method of computing the rank of a matrix.
# Implement this method.

#M <- matrix(c(0, 2, 3, 7), 2, 2)
M <- matrix(c(2,6,5,5,3,-2,7,4,-3), 3,3)
M
for (col in 1:ncol(M))
{
    if (M[col,col] == 0) {
        for (r in 2:nrow(M)){
            M[c(col,r),] <- M[c(r,col),]
        }
    }
    
    M[col,] <- M[col,] / M[col,col]  
    
    for (row in 1:nrow(M)){
      if (row > col){ M[row,] <- M[row,] - M[row,col]*M[col,]}
        }
    }
M
