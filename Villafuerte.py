'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def full_triangle(n):
   for i in range(1, n + 1):
       print(' ' * (n - i) + '* ' * i)
def reverse_triangle(n):
   for i in range(n, 0, -1):
       print(' ' * (n - i) + '* ' * i)
def diamond(n):
   for i in range(1, n + 1):
       print(' ' * (n - i) + '* ' * i)
   for i in range(n - 1, 0, -1):
       print(' ' * (n - i) + '* ' * i)
n = 5
print("Triangle:")
full_triangle(n)
print("\nReverse Triangle:")
reverse_triangle(n)
print("\nDiamond:")
diamond(n)