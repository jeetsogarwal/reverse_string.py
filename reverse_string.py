def reverse(str1):
    new_str = ' '
    i = len(str1)-1
    while i>=0:
        new_str += str1[i]
        i -=1
        return new_str

str1 = input("\nEnter the string: ")
print("\nReverse of the string is: ",reverse(str1))