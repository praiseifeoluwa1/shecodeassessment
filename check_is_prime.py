def is_prime(number):
    if number > 1:
        if number in [2, 3]:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        else:
            return True
    return False


print(is_prime(int(input("Enter a number to check if it is prime: "))))

