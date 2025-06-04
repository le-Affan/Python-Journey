# Write a function that takes two numbers and returns their sum.
# Write a function that takes a string and prints whether it’s a palindrome.



def add(a,b):
    c=a+b
    return c

#print(add(90,2376))


def check_palindrome(a):
        i = 0
        j = len(a) - 1

        def helper(a):
            nonlocal i
            nonlocal j

            if i<j:
                if a[i] == a[j]:
                    i += 1
                    j -= 1
                    helper(a)
                else:
                    print("Not palindrome")

            elif i>=j:
                print("Palindrome")

        helper(a)


#check_palindrome("affan")
#check_palindrome("racecar")





