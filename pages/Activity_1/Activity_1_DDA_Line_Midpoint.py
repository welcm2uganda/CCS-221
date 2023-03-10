import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Activity\t1\nGroup\t8\tBYTE\nDDA\tMidpoint")

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xcoordinate = float(dx / steps)
    Ycoordinate = float(dy / steps)

    fig = plt.figure()
    for i in range(0, int(steps + 1)):

        print('x = %s, y = %s' % (x, y))
        plt.plot(int(x1), int (y1), color)
        x1 += Xcoordinate
        y1 += Ycoordinate
    plt.plot(x3, y3, marker = "o", markersize = 5, markerfacecolor = "red")
    plt.show()
    st.pyplot(fig)
    st.write("Midpoint: ", int(x3), ", ", int(y3), ".")

def main():
    st.title("DDA Line")
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
    DDALine(x, y, x2, y2, color)

if __name__ == '__main__':
    main()
