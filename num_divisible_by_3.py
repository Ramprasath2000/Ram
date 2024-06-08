def is_last_digit_divisible_by_3(number):
    last_digit = number % 10
    if last_digit % 3 == 0:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
if is_last_digit_divisible_by_3(number):
    print("The last digit of", number, "is divisible by 3.")
else:
    print("The last digit of", number, "is not divisible by 3.")