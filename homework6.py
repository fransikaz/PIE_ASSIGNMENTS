'''
HOMEWORK # 6: Advance Loops
Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board with he same number of rows and columns as specified
'''


def drawPlayBoard(row, col):
    if row != col:  # Forcing the number of rows and columns to be equal
        print("Number of rows and columns must be equal!")
    elif row > 50:  # Maximum screen height (rows)
        print("Maximum height exceeded")
    elif col > 50:  # Maximum screen width (rows)
        print("Maximum width exceeded")
    else:
        for rows in range(row):
            if rows % 2 == 0:         # True for rows 0, 2, and 4
                for cols in range(col):
                    if cols % 2 != 0:  # True for columns 1 and 3
                        # prints "|" in cells (0,1),(0,3),(2,1),(2,3),(4,1), and (4,3)
                        print("|", end="")
                    else:  # For columns 0, 2, and 4 which returded False
                        # Prints '  ' in cells (0,0),(0,2),(0,4),(2,0),(2,2),(2,4),(4,0),(4,2) and (4,4)
                        print(" ", end="")
                print()  # Prints new line
            else:  # For rows 1 & 3 which returned False
                for cols in range(col):
                    if rows % 2 != 0:  # True for rows 1 & 3
                        # Prints "-" in rows 1 & 3 in columns 0 to 4
                        print("-", end="")
                print()  # Prints new line


r = int(input("Enter number of rows:  "))
c = int(input("Enter number of columns:  "))
drawPlayBoard(r, c)
