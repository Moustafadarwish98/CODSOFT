def addition(num_1, num_2):
    """Adding numbers, returning sum"""
    return num_1 + num_2


def subtraction(num_1, num_2):
    """Subtracting numbers, returning difference"""
    return num_1 - num_2


def multiplication(num_1, num_2):
    """multiplying numbers, returning product"""
    return num_1 * num_2


def division(num_1, num_2):
    """dividing numbers, returning quotient"""
    return num_1 / num_2


new_calculation = True

"""Checking if there is a previous stored result"""
try:
    with open(file="./result_storage.txt", mode="r") as file:
        result = float(file.read())
        print(f"Last stored result is {result}.")
except FileNotFoundError:
    result = 0
    new = "yes"
else:
    new = input(f"Do you want to start a new calculation (type yes) or continue "
                f"with stored result (result = {result}) (type no) ").lower()
while new_calculation:
    if new == "yes":
        first_number = float(input("Enter first number: "))
    else:
        first_number = result
    second_number = float(input("Enter second number: "))
    operation_choice = input("Choose an operation ('+', '-', '*', '/'): ")

    if operation_choice == "+":
        result = addition(first_number, second_number)
    elif operation_choice == "-":
        result = subtraction(first_number, second_number)
    elif operation_choice == "*":
        result = multiplication(first_number, second_number)
    else:
        result = round(division(first_number, second_number), 2)
    print(f"result = {result}")

    """Checking if user wants to continue calculations with result or
    they want to start a new calculation"""
    continue_calculation = input("Do you want to continue with previous result (type yes)  or "
                                 "start a new calculation (type no) or "
                                 "Exit (type E)? ").lower()

    if continue_calculation == "yes":
        new = "no"
    elif continue_calculation == "e":
        """Storing result before terminating program to be used in future calculation if needed."""
        with (open("result_storage.txt", mode="w")) as file:
            file.write(str(result))
        print("turned off")
        new_calculation = False





