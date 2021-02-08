'''
Homework #3 "If" Statements
Function that accepts 3 parameters and checks for equality between any two of them
'''


def ComprABC(a, b, c):
    # Compare values for parameters a, b and c
    if (a == b) or (a == c) or (b == c):
        # print 'Match Found' if the If statement returns True
        print("Match Found")
    else:
        # print 'No Match Found' if the If statement returns False
        print("No Match Found")


a = "100"  # variable for parameter a set as string
b = 25 * 4  # variable for parameter b set as integer
c = 25  # variable for parameter b set as integer

ComprABC(int(a), b, c)
