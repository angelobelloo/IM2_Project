matrix = []

for r in range(2):
    print("Row", r + 1)
    row = []
    for c in range(2):
        num = float(input(f"Enter numeric{c + 1}: "))
        row.append(num)
    matrix.append(row)
    search = float(input("\nSearch: "))

    print("\nThe numbers are:")
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()
print(f"\nNumber {search} found at:")
for r in range(2):
    for c in range(2):
        if matrix[r][c] == search:
            print(f"Row {r}, Col {c}")
