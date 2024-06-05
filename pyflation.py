import cpi

def inflation_adjustment():
    """
    Adjusts the initial amount for inflation to the specified comparison year.

    Args:
        initial_amount (int): The amount to adjust for inflation.
        comparison_year (int): The year to which the amount should be adjusted.

    Returns:
        None

    Prints the adjusted amount to the console.
    """
    initial_amount = int(input("Enter the amount you would like to adjust for inflation: $"))
    comparison_year = int(input("Enter the year you would like to adjust the amount to: "))
    inflated_amount = cpi.inflate(initial_amount, comparison_year)
    print(f"In the year {comparison_year}, ${initial_amount} was equivalent to ${inflated_amount:.2f}.")

inflation_adjustment()
