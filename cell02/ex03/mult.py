first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
result_num = first_num * second_num

print(str(first_num) + " x " + str(second_num) + " = " + str(result_num))

if result_num > 0:
    print("This result is positive.")
elif result_num < 0 :
    print("This result is negative.")
else :
    print("This result is zero.")