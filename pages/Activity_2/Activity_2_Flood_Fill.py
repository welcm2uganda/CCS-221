import numpy as py
import matplotlib.pyplot as plt
import random as rndm
import streamlit as st


def isValid(screen, m, n, x, y, prevC, newC):
    if x<0 or x>= m\
       or y<0 or y>= n or\
       screen[x][y] != prevC\
       or screen[x][y] == newC:
        return False
    return True
 
def floodFill(screen, 
            m, n, x, 
            y, prevC, newC):
    queue = []
     
    queue.append([x, y])
 
    screen[x][y] = newC
 
    while queue:
         
        currPixel = queue.pop()
         
        posX = currPixel[0]
        posY = currPixel[1]
         
        if isValid(screen, m, n, 
                posX + 1, posY, 
                        prevC, newC):
             
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])
         
        if isValid(screen, m, n, 
                    posX-1, posY, 
                        prevC, newC):
            screen[posX-1][posY]= newC
            queue.append([posX-1, posY])
         
        if isValid(screen, m, n, 
                posX, posY + 1, 
                        prevC, newC):
            screen[posX][posY + 1]= newC
            queue.append([posX, posY + 1])
         
        if isValid(screen, m, n, 
                    posX, posY-1, 
                        prevC, newC):
            screen[posX][posY-1]= newC
            queue.append([posX, posY-1])

screen =[
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
[1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
[1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 2, 2, 0, 1, 0, 0, 0, 0],
[1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 0],
[1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1],
[1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1]]
fig = plt.figure()
plt.rcParams["figure.figsize"] = [8, 7]
plt.rcParams["figure.autolayout"] = False

plt.axis([-0.5, 10.5, -0.5, 10.5])

print("Before floodfill: ")
plt.imshow(screen, interpolation = 'none', cmap = 'inferno')
plt.colorbar()
plt.show()
     
m = len(screen)

n = len(screen[0])

st.title("Floodfill")

x = st.slider(
    'X1',
    0, 10)
st.write('x1: ', x)

y = st.slider(
    'Y1',
    0, 10)
st.write('y1: ', y)

newC = st.slider(
        'Color',
        0, 3)
st.write('color: ', newC)
 
prevC = screen[x][y]
floodFill(screen, m, n, x, y, prevC, newC)
 
plt.rcParams["figure.figsize"] = [8, 7]
plt.rcParams["figure.autolayout"] = False

plt.axis([-0.5, 10.5, -0.5, 10.5])
for i in range(m):
    for j in range(n):
        print(screen[i][j], end =' ')
    print()


print("After floodfill: ")
plt.imshow(screen, interpolation = 'none', cmap = 'inferno')
plt.colorbar()
plt.show()
st.pyplot(fig)
plt.show()
