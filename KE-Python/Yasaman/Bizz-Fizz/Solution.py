def fizz_buzz(n):
    # Create an empty list to store the results
    results = []

    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If the number is divisible by both 3 and 5, append "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        # If the number is divisible by 3, append "Fizz"
        elif i % 3 == 0:
            results.append("Fizz")
        # If the number is divisible by 5, append "Buzz"
        elif i % 5 == 0:
            results.append("Buzz")
        # If the number is not divisible by either 3 or 5, append the number as a string
        else:
            results.append(str(i))
    
    # Return the results list
    return results
