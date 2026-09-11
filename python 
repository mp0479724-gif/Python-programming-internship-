# ============================================================
# Python Programming Internship - Task 1
# Core Python Challenges
# ============================================================

# ------------------------------------------------------------
# 1. Sum of Two Numbers
# ------------------------------------------------------------
def sum_of_two_numbers():
    print("\n--- 1. Sum of Two Numbers ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 + num2

    print("Sum =", result)


# ------------------------------------------------------------
# 2. Odd or Even Checker
# ------------------------------------------------------------
def odd_even_checker():
    print("\n--- 2. Odd or Even Checker ---")

    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is an Even number")
    else:
        print(num, "is an Odd number")


# ------------------------------------------------------------
# 3. Factorial Calculation
# ------------------------------------------------------------
def factorial_calculation():
    print("\n--- 3. Factorial Calculation ---")

    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial of", num, "=", factorial)


# ------------------------------------------------------------
# 4. Fibonacci Sequence
# ------------------------------------------------------------
def fibonacci_sequence():
    print("\n--- 4. Fibonacci Sequence ---")

    n = int(input("Enter the number of terms: "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    a = 0
    b = 1

    print("Fibonacci sequence:")

    for i in range(n):
        print(a, end=" ")

        next_term = a + b
        a = b
        b = next_term

    print()


# ------------------------------------------------------------
# 5. String Reverse
# ------------------------------------------------------------
def string_reverse():
    print("\n--- 5. String Reverse ---")

    text = input("Enter a string: ")

    reversed_text = text[::-1]

    print("Reversed string:", reversed_text)


# ------------------------------------------------------------
# 6. Palindrome Check
# ------------------------------------------------------------
def palindrome_check():
    print("\n--- 6. Palindrome Check ---")

    text = input("Enter a word: ")

    text = text.lower()

    if text == text[::-1]:
        print(text, "is a Palindrome")
    else:
        print(text, "is not a Palindrome")


# ------------------------------------------------------------
# 7. Leap Year Check
# ------------------------------------------------------------
def leap_year_check():
    print("\n--- 7. Leap Year Check ---")

    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")


# ------------------------------------------------------------
# 8. Armstrong Number
# ------------------------------------------------------------
def armstrong_number():
    print("\n--- 8. Armstrong Number ---")

    num = int(input("Enter a number: "))

    original_num = num

    # Number of digits
    order = len(str(num))

    # Calculate sum of powers of digits
    sum_val = sum(int(digit) ** order for digit in str(num))

    if original_num == sum_val:
        print(original_num, "is an Armstrong number")
    else:
        print(original_num, "is not an Armstrong number")


# ============================================================
# RUN ALL PROGRAMS
# ============================================================
def run_all_programs():
    print("\n==========================================")
    print("     RUNNING ALL 8 PROGRAMS")
    print("==========================================")

    sum_of_two_numbers()
    odd_even_checker()
    factorial_calculation()
    fibonacci_sequence()
    string_reverse()
    palindrome_check()
    leap_year_check()
    armstrong_number()

    print("\n==========================================")
    print("       ALL PROGRAMS COMPLETED")
    print("==========================================")


# ============================================================
# MAIN MENU
# ============================================================
def main():
    while True:

        print("\n==========================================")
        print("   PYTHON PROGRAMMING INTERNSHIP")
        print("              TASK 1")
        print("==========================================")

        print("1. Sum of Two Numbers")
        print("2. Odd or Even Checker")
        print("3. Factorial Calculation")
        print("4. Fibonacci Sequence")
        print("5. String Reverse")
        print("6. Palindrome Check")
        print("7. Leap Year Check")
        print("8. Armstrong Number")
        print("9. Run All Programs")
        print("0. Exit")

        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            sum_of_two_numbers()

        elif choice == "2":
            odd_even_checker()

        elif choice == "3":
            factorial_calculation()

        elif choice == "4":
            fibonacci_sequence()

        elif choice == "5":
            string_reverse()

        elif choice == "6":
            palindrome_check()

        elif choice == "7":
            leap_year_check()

        elif choice == "8":
            armstrong_number()

        elif choice == "9":
            run_all_programs()

        elif choice == "0":
            print("\nThank you!")
            print("Python Internship Task 1 completed.")
            break

        else:
            print("\nInvalid choice! Please select a number from 0 to 9.")


# ============================================================
# START PROGRAM
# ============================================================
if __name__ == "__main__":
    main()