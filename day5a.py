n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, ":")
for i in range(1, n + 1):
    print(i)

sum1 = 0
current_num = 1

while current_num <= n:
    sum1 += current_num
    current_num += 1

print("The sum of numbers from 1 to", n, "is:", sum1)

##2question

def cal_square(n):
    return n ** 2

num = int(input("Enter a positive integer: "))
square = cal_square(num)
print(f"The square of {num} is {square}.")

