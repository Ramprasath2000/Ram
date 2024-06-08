def get_last_digit(number):
    # Take the last digit by modulo 10
    last_digit = number % 10
    return last_digit

# Test the function
number = int(input("Enter a number: "))
last_digit = get_last_digit(number)
print("The last digit of", number, "is", last_digit)