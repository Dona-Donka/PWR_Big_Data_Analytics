from random import randint
import matplotlib.pyplot as plt

stepsList = []
xnList = []
listOfR = []

def atomsMove(xn, L):
    for atom in range(0,L):
        x = 0
        y = 0
        for item in range(1, xn):
            R =randint(0, 4)

            if R == 0:
                x = x + 1
            elif R == 1:
                x = x - 1
            elif R == 3:
                y = y + 1
            elif R == 4:
                y = y - 1

            stepsList.append(x)
            xnList.append(y)

        R = x^2 + y^2
        listOfR.append(R)

    return listOfR
C01 = atomsMove(1000, 100) # C = 0.1
C05 = atomsMove(5000, 100) # C = 0.5

plt.plot(xnList, stepsList)
plt.show()

# C = n/L^2
# C = 0.1 gdy 10/100  100/1000   n =1000, L =100
# C = 0.5 gy  50 i 100  np  n = 5000, L = 10000
