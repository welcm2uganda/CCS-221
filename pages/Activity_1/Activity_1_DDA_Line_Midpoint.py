import matplotlib.pyplot as plt

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xcoordinate = float(dx / steps)
    Ycoordinate = float(dy / steps)

    for i in range(0, int(steps + 1)):

        plt.plot(int(x1), int (y1), color)
        x1 += Xcoordinate
        y1 += Ycoordinate
    plt.plot(x3, y3, marker = "o", markersize = 5, markerfacecolor = "red")
    plt.show()

def main():
    x = int(input("Enter X1: "))
    y = int(input("Enter Y1: "))
    xEnd = int(input("Enter X2: "))
    yEnd = int(input("Enter Y2: "))
    color = "g."
    DDALine(x, y, xEnd, yEnd, color)

if __name__ == '__main__':
    main()