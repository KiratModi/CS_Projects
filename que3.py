def partA():
    print("NAme = Kirat Sanjaykamar modi")
    print("Student number: 640326")

def partB():
    while True:
        name = input("Enter your name: ")
        if any(char.isdigit() for char in name):
            print("Error: Name should not contain numbers. Please try again.")
            continue
        break

    while True:
        student_number = input("Enter your student number: ")
        if not student_number.isdigit():
            print("Error: Student number should only contain digits. Please try again.")
            continue
        break

    print(f"Name: {name}")
    print(f"Student Number: {student_number}")
    
    sum_digits = sum(int(digit) for digit in student_number if digit.isdigit())
    print(f"The sum of all numbers in the student number {student_number} is: {sum_digits}") #PART C

partA()
print("-" * 100)
partB()
