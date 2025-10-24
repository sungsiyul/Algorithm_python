n = int(input())

# Please write your code here.
def helloworld(n):
    if n == 0:
        return
    helloworld(n-1)
    print("HelloWorld")

helloworld(n)