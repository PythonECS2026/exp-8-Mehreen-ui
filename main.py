# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder: mehreen ansari
# Date: 20/02/2026

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


