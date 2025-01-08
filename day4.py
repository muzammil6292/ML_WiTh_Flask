def sum_even_numbers(n):
   
    if n < 1:
        return "Please enter a positive integer greater than or equal to 1."
    ev_sum = sum(i for i in range(2, n + 1, 2))
    return ev_sum

try:
    n = int(input("Enter a positive integer: "))
    result = sum_even_numbers(n)
    print(f"The sum of all even numbers between 1 and {n} is: {result}")
except ValueError:
    print("Invalid input! Please enter a positive integer.")
