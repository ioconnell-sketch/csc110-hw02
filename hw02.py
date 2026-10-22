# Name: Issy O'Connell
# CSC110 - Homework 2
# Reads two integers, computes (a * b) / (a + b), and prints the final results.

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two integers from the user and return them."""
    # input() gives me text, so wrap it in int() to get a number
    x = int(input("give me x: "))
    y = int(input("give me y: "))
    # no parentheses on the return, just a comma
    return x, y

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Print the product and sum of a and b, then return product divided by sum."""
    # top of the fraction
    product = a * b
    print("mult result: " + str(product))

    # bottom of the fraction
    total = a + b
    print("add result: " + str(total))

    # "/" always makes a float, so 150 / 25 shows up as 6.0
    return product / total

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the two inputs and the multadd result inside a decorated box."""
    print()  # blank line so the box doesn't crowd the lines above
    print("*" * 16)  # 16 stars, just multiplying a string
    print("RESULTS:")
    print("first number: " + str(a))
    print("second number: " + str(b))
    print("multadd result: " + str(ab_multadd))
    print("=" * 16)  # 16 equals signs
    print()  # blank line before "The End"

def main ():
    """Run the program: read two ints, compute multadd, and print the results."""
    # this is a note for the user about what this program does
    print("This program multiplies two whole numbers, adds them, and divides the product by the sum. Have fun by experimenting with different x and y values!")

    # Task 1.2: grab both numbers at once
    x, y = read_two_ints()

    # Task 2.2: needs x and y, gives back one value
    xy_multadd = compute_multadd(x, y)

    # Task 3.2: this one just prints, nothing to catch
    print_fancy(x, y, xy_multadd)

    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
