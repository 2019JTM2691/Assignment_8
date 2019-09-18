def value(x, y, arr):
    x = int(x)
    c = x // 3
    z = x % 3
    print(c)
    print(z)
    arr[c][z - 1] = y
    print(arr[c][z])
    # For printing the matrix
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end=" ")
        print()


print("welcome to the game ")
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        print(board[i][j], end=" ")
    print()
fpers = ["1", "3", "5", "7"]
sepers = ["2", "4", "6", "8"]
for i in range(0, 9):
    if i % 2 == 0:
        a = input("Enter the input for  from the first person : ")
        if int(a) <= 9:
            d = 1
        else:
            print("Enter correct number.")
            exit()
        b = input("Enter the input for value at {} position: ".format(a))
        for char in fpers:
            if char == b:
                v = 1

            else:
                v = 0
        fpers.remove(b)
        #if v == 0:
           # print("Enter correct number.")
            #exit()

        value(a, b, board)
    else:
        a = input("Enter the input for  from the second person : ")
        if int(a) <= 9:
            d = 1
        else:
            print("Enter correct number.")
            exit()
        b = input("Enter the input for value at {} position: ".format(a))
        for char in sepers:
            print(char)
            if char != b:
                v = 1
            else:
                v = 0
        sepers.remove(b)
        #if v == 1:
         #   print("Enter correct number.")
          #  exit()
        value(a, b, board)
