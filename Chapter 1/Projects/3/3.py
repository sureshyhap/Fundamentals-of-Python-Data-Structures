"""Calculates total distance traveled of a bouncing ball."""
def main():
    """Finds total distance traveled by a bouncing ball
    for a chosen number of bounces."""
    initial_height = float(input("What is the initial height? "))
    bounces = int(input("How many bounces should we consider? "))
    total_dist = 0
    height = initial_height
    for i in range(bounces):
        total_dist += (1.6 * height)
        height *= .6
    print("Total distance traveled: ", total_dist)


if __name__ == "__main__":
    main()
