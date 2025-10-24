A = input()

# Please write your code here.
def check_palindrome(A):
    return A == A[::-1]

print("Yes" if check_palindrome(A) else "No")
