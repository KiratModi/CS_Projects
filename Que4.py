# Part a
def p_5_by_3_grid():
    print("This is for part A")
    for i in range(5):
        for j in range(3):
            print('*', end='')
        print()

# Part b
def print_grid_with_diagonals():
    print("This is for part B")
    n = int(input("Enter the number of rows (n): "))
    m = int(input("Enter the number of columns (m): "))
    
    for i in range(n):  #nested loops
        for j in range(m):
            if i == j:
                print('D', end='')
            else:
                print('*', end='')
        print()

# Part c
def print_grid_with_borders():
    print("This is for part c")
    n = int(input("Enter the number of rows (n): "))
    m = int(input("Enter the number of columns (m): "))
    
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1:
                print('=', end='')
            elif j == 0 or j == m-1:
                print('|', end='')
            else:
                print('*', end='')
        print()

p_5_by_3_grid()
print("-" * 50)
print_grid_with_diagonals()
print("-" * 50)
print_grid_with_borders()
print("Thanks that was all for this question")
