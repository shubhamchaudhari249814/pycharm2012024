# Function to add two numbers
def add_two_numbers():
    try:
        # Get input from the user for the two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = num1 + num2

        # Display the result
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input! Please enter numerical values.")


# Call the function
add_two_numbers()
