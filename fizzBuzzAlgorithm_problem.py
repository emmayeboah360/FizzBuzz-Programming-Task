def fizzBuzz():
    count = 0
    while count < 5:
        count += 1
        try:
            number = int(input("Enter the number: "))
        except ValueError:
            print("Enter a number")
            count -= 1          # don't count invalid inputs
            continue

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


# Run the function directly (no print around it)
fizzBuzz()
