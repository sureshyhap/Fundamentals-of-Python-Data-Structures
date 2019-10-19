"""
Calculates payments for a computer payment plan.
"""

def main():
    """Reads in a total amount and
    outputs several payment quantities."""
    total_balance = float(input("Wnat is the total price? "))
    month_number = 1
    current_tot_balance = total_balance
    down_payment = .1 * total_balance
    interest_rate = .12
    current_tot_balance -= down_payment
    print("%30s" % "Month number", end="")
    print("%30s" % "Total balance left", end="")
    print("%30s" % "Interest this month", end="")
    print("%30s" % "Principal this month", end="")
    print("%30s" % "Total payment this month", end="")
    print("%30s" % "Total balance remaining", end="")
    print()
    while current_tot_balance > 0:
        interest_this_month = current_tot_balance * interest_rate / 12
        payment_this_month = (.05 * total_balance) + interest_this_month
        principal_this_month = payment_this_month - interest_this_month
        remaining_balance = current_tot_balance - principal_this_month
        # If negative remaining balance, remove the absolute value to the last payment
        if remaining_balance < 0:
            payment_this_month += remaining_balance
            remaining_balance = 0
        print("%30d%30.2f%30.2f%30.2f%30.2f%30.2f" % (
            month_number, current_tot_balance, interest_this_month,
            principal_this_month, payment_this_month, remaining_balance))
        current_tot_balance = remaining_balance
        month_number += 1
        


if __name__ == "__main__":
    main()
