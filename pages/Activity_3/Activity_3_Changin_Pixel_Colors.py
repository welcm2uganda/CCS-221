import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]])

def changePixelikea(row, column):
        colorchange = int(input("Which color would you want to change it with?(0/1): "))
        two_d_arr[row][column] = colorchange
        plt.imshow(two_d_arr, interpolation = 'none', cmap = 'plasma')
        plt.colorbar()
        plt.show()

def changePixelgrey(row, column):

        colorchange = int(input("Which color would you want to change it with?(0/1): "))
        two_d_arr[row][column] = colorchange
        plt.imshow(two_d_arr, interpolation = 'none', cmap = 'gray_r')
        plt.colorbar()
        plt.show()

def changePixelrandom(row, column):

        colorchange = int(input("Which color would you want to change it with?(0/1): "))
        two_d_arr[row][column] = colorchange
        plt.imshow(np.random.random((3,3)), interpolation = 'none', cmap = 'gray_r')
        plt.colorbar()
        plt.show()


def main():

    ikea = 'y'

    while (ikea == 'y'):
        print("Choices:")
        print("1 = Yellow Blue")
        print("2 = Grey")
        print("3 = Grey(Random Variant)")
        print("4 = Terminate Program\n")
        choice = int (input("Which kind of table do you want to edit: "))

        if (choice == 1):
            print ("You are now editting yellow blue table.\n")
            row = int(input("From which row would you like to modify your specific tile?: "))
            column = int(input("From which column would you like to modify your specific tile?: "))
            changePixelikea(row, column)
            ikea = input("Do you want to continue editting?(y/n): ")

        if (choice == 2):
            print ("You are now editting grey table.\n")
            row = int(input("From which row would you like to modify your specific tile?: "))
            column = int(input("From which column would you like to modify your specific tile?: "))
            changePixelgrey(row, column)    

        if (choice == 3):
            print ("You are now editting a randomized grey table.\n")
            row = int(input("From which row would you like to modify your specific tile?: "))
            column = int(input("From which column would you like to modify your specific tile?: "))
            changePixelrandom(row, column)

        if (choice == 4 or ikea == 'n'):
            print("Program Terminated.")
            exit()
        
        ikea = input("Do you want to continue editting?(y/n): ")

if __name__ == '__main__':
    main()
