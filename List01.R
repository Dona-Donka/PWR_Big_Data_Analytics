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
        print("after if")        
    }
    
    A[col,] <- A[col,] / A[col,col]  
    
    for (row in 1:nrow(M)){
        if (row != col){ A[row,] <- A[row,] - A[row,col]*A[col,] }
        }
    }
print("Result: ")
A
