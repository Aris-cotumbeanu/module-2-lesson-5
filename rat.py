print("Half pyramid pattern of stars(*):")
n = int(input("enter how many rows you want :"))
for i in range(n):
    for J in range (i + 1):
        print("*", end=" ")
    print()