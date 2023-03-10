import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity\t1\nGroup\t8\tBYTE\nBresenham\tMidpoint")

def BresenhamLine(x1, y1, x2, y2, color):
    
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)
    x3 = (x2 + x1) / 2
    y3 = (y2 + y1) / 2
   

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    xcoordinates = [x]
    ycoordinates = [y]

    
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    fig = plt.figure()
    for i in range(0, int(steps + 1)):
        
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2  * dy

        x = x + 1 if x < x2 else x - 1

        print('x = %s, y = %s' % (x, y))
        xcoordinates.append(x)
        ycoordinates.append(y)            
    plt.plot(xcoordinates, ycoordinates)
    plt.show()
    st.pyplot(fig)
    st.write("Midpoint: ", int(x3), ", ", int(y3), ".")
    
def Midpoint(x1, y1, x2, y2, color):
    fig = plt.figure()

    dx = x2 - x1
    dy = y2 - y1

    d  = dy - (dx/2)
    x = x1
    y = y1

    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        # print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates, color, marker='s', markersize=5)

    return fig

def main():
    st.title("Bresenham Line")
    x1 = 10
    x2 = 10

    x = st.slider(
        'X1',
        0, 100)
    st.write('x1: ', x)

    y = st.slider(
        'Y1',
        0, 100)
    st.write('y1: ', y)

    x2 = st.slider(
        'X2',
        0, 100)
    st.write('x2: ', x2)

    y2 = st.slider(
        'Y2',
        0, 100)
    st.write('y2: ', y2)
    color = "g." 
    BresenhamLine(x, y, x2, y2, color)
    Midpoint(x, y, x2, y2, color)


if __name__ == '__main__':
    main()
