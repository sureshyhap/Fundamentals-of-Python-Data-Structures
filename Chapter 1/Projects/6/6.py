"""Calculates wages per pay period."""

def main():
    """Calculates wages per week."""
    input_file = input("Enter the name of the data file: ")
    with open(input_file, "r") as f:
    print("%20s%20s%20s" % ("Name", "Hours", "Wages"))
    for line in f:
        datum = line.split()
        # dataum[0] holds the last name
        # datum[1] holds hourly wage
        # datum[2] holds hours worked
        print("%20s%20s%20s" % (datum[0], datum[2], datum[1] * datum[2])


if __name__ == "__main__":
    main()
