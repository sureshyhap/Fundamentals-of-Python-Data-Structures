"""Allows user to navigate through the lines in a file."""

def main():
    """Parses a file's lines."""
    filename = input("Enter a filename for reading: ")
    with open(filename, "r") as f:
        list_lines = f.readlines()
    print("Number of lines: " + str(len(list_lines)))
    while True:
        line = int(input("Enter a line number to get that line (or 0 to quit)"))
        if not line:
            break
        # line - 1 because start counting at 1 
        print(list_lines[line - 1])

if __name__ == "__main__":
    main()
