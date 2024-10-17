def calculate_factorial(number):
    print(number)
    res = number
    if number ==0:
        return 1
    if number > 0:
        while number > 1:
            res = res * (number -1)
            number = number -1
        
    return res
print(calculate_factorial(5))
