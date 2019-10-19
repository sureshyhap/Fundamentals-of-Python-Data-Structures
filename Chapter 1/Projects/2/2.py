"""
Calculates weekly pay based on wage and hours worked.
"""
def main():
    """Calculates pay"""
    wage = float(input("Enter the hourly wage: "))
    reg_hours = int(input("Enter the number of regular hours you worked: "))
    overtime_hours = int(input("Enter the number of overtime hours you worked: "))
    pay = wage * (reg_hours + 1.5 * overtime_hours)
    print(pay)

if __name__ == "__main__":
    main()
