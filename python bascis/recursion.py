# # P1: print n to 1
# def count(n):
#     if n==0:
#         return
#     print(n)
#     count(n-1)
# count(9)
     # Change the code so it prints 1 2 3 (not 3 2 1)
def rev(n):
    if n==4:
        return
    print(n)
    rev(n+1)
rev(1)


