num1 = int(input())
num2 = int(input())
int_sum = int(num1,2) + int(num2,2)
binary_sum = bin(int_sum)[2:]
print(binary_sum)