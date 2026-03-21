#wap to to check whether the string is plaindrome or symmetrical or not
s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")
mid = len(s) // 2

if len(s) % 2 == 0:
    if s[:mid] == s[mid:]:
        print("The string is Symmetrical")
    else:
        print("The string is not Symmetrical")
else:
    if s[:mid] == s[mid+1:]:
        print("The string is Symmetrical")
    else:
        print("The string is not Symmetrical")