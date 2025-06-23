# num=input("enter a number =>")

# if num==num[::-1]:
#     print("It is palindrome")
# else:
#     print("it is not palindrome")


num = int(input("Enter a number: "))

original_num = num

reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original_num == reverse:
    print(original_num, "is a Palindrome Number")
else:
    print(original_num, "is not a Palindrome Number")


