print("Welcome to FizzBuzz game!")
while True:
    try:
        number = int(input("Select a number between 1 and 100 and make a fizzbuzz count: "))
        if number > 100:
            print("Number is too high.")
        elif number < 1:
            print("Number is too low.")
        else:
            for num in range(1, number + 1):
                if num % 3 == 0 and num % 5 == 0:
                    print('FizzBuzz')
                elif num % 5 == 0:
                    print('Buzz')
                elif num % 3 == 0:
                    print('Fizz')
                else:
                    print(num)
            break
    except ValueError:
        print("Input a whole number!")

