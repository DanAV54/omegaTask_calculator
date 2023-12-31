def print_menu():
    # The function prints the menu of the calculator and the calculator's options
    print("Hello!\nWelcome to Dan Ahuv's Calculator")
    print("The Calculator contains the following options")
    print("\t0- quit the calculator")
    print("\t1- addition operation between two numbers")
    print("\t2- subtraction operation between two numbers")
    print("\t3- multiplication operation between two numbers")
    print("\t4- the operation of dividing two numbers")
    print("\t5- power operation between two numbers")


def input_int_value(minimum_value, maximum_value, input_message):
    """ The function tries to get an input of type integer
        if the input from the user is out of the numbers range
        (smaller than minimum_value and bigger than maximum_value)
        OR if the input is not a number (contains letters ext)
        try to get the input again until the input is valid  """

    input_flag = True
    result_of_input = 0

    while input_flag:
        result_of_input = input(input_message)
        if not result_of_input.lstrip('-+').isdigit():
            print("Enter only numbers please.")
            continue
        result_of_input = int(result_of_input)
        if result_of_input > maximum_value:
            print("Enter smaller numbers than {0} please".format(maximum_value + 1))
            continue
        if result_of_input < minimum_value:
            print("Enter bigger numbers than {0} please".format(minimum_value - 1))
            continue
        input_flag = False
    return result_of_input


def addition_operation():
    # the function inputs two integer numbers and prints the result of adding these two integers
    first_operand = input_int_value(-1000000, 1000000, "please enter the first operand for the addition operation: ")
    second_operand = input_int_value(-1000000, 1000000, "please enter the second operand for the addition operation: ")

    print("the result of the addition operation between {0} and {1} is {2}\n\n".format(
        first_operand, second_operand, first_operand + second_operand))


def subtraction_operation():
    # the function inputs two integer numbers and prints the result of subtracting these two integers
    first_operand = input_int_value(-1000000, 1000000, "please enter the first operand for the subtraction operation: ")
    second_operand = input_int_value(-1000000, 1000000,
                                     "please enter the second operand for the subtraction operation: ")

    print("the result of the subtraction operation between {0} and {1} is {2}\n\n".format(
        first_operand, second_operand, first_operand - second_operand))


def multiplication_operation():
    # the function inputs two integer numbers and prints the result of multiplying these two integers
    first_operand = input_int_value(
        -1000000, 1000000, "please enter the first operand for the multiplication operation: ")
    second_operand = input_int_value(-1000000, 1000000,
                                     "please enter the second operand for the multiplication operation: ")

    print("the result of the multiplication operation between {0} and {1} is {2}\n\n".format(
        first_operand, second_operand, first_operand * second_operand))


def divide_operation():
    # the function inputs two integer numbers and prints the result of dividing these two integers
    first_operand = input_int_value(-1000000, 1000000, "please enter the first operand for the divide operation: ")

    second_operand = 0
    while second_operand == 0:
        second_operand = input_int_value(
            -1000000, 1000000, "please enter the second operand for the divide operation.\nremember, it can't be 0: ")

    print("the result of the divide operation between {0} and {1} is {2}\n\n".format(
        first_operand, second_operand, first_operand / second_operand))


def power_operation():
    # the function inputs two integer numbers and prints the result of powering these two integers
    first_operand = 0
    second_operand = 0

    while first_operand == 0 and second_operand == 0:
        first_operand = input_int_value(-10, 10, "please enter the first operand for the power operation: ")
        second_operand = input_int_value(
            -10, 10, "please enter the second operand for the power operation.\nremember, both operands cannot be 0: ")

    print("the result of the power operation between {0} and {1} is {2}\n\n".format(
        first_operand, second_operand, first_operand ** second_operand))


if __name__ == '__main__':
    flag = True

    while flag:
        print_menu()
        option = input_int_value(0, 5, "please enter an option from the written options: ")

        if option == 0:
            print("Thank you for using Dan Ahuv's Calculator!\nGoodbye :)")
            flag = False

        elif option == 1:
            addition_operation()

        elif option == 2:
            subtraction_operation()

        elif option == 3:
            multiplication_operation()

        elif option == 4:
            divide_operation()

        else:
            power_operation()
