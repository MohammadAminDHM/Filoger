from Solution import fizz_buzz

def test_fizz_buzz():
    test_cases = [3, 5, 15, 30, 100, 1000, 10000]
    for test in test_cases:
        result = fizz_buzz(test)
        print(f"For n={test}, output is {result}\n")

def fizz_buzz(n):
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

# call the test function
test_fizz_buzz()