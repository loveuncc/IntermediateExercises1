def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid integer. Please try again.")

total = 0
for i in range(5):
    total += get_integer_input(f"Enter integer {i + 1} of 5: ")

print(f"Total sum: {total}")

