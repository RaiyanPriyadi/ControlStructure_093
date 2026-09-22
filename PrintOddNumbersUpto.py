n = int(input("Enter the maximum value (n): "))

print(f"Odd numbers up to {n}:")
# range(start, stop, step)
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()