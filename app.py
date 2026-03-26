# app.py - Simple Tax Calculator
def format_currency(amount):
    """Format amount as Thai Baht currency."""
    return f"{amount:,.2f} THB"


def calculate_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150000) * 0.05
    elif income <= 500000:
        return 7500 + (income - 300000) * 0.10
    elif income <= 750000:
        return 27500 + (income - 500000) * 0.15
    else:
        return 65000 + (income - 750000) * 0.20


def calculate_net_income(income):
    """Calculate net income after tax."""
    tax = calculate_tax(income)
    return income - tax


def calculate_deduction(expense_type, amount):
    """Calculate allowable tax deductions."""
    deductions = {
        "insurance": min(amount, 100000),
        "education": min(amount, 50000),
        "donation": min(amount, 100000),
    }
    return deductions.get(expense_type, 0)


if __name__ == "__main__":
    test_incomes = [100000, 250000, 400000, 600000, 1000000]
    for income in test_incomes:
        tax = calculate_tax(income)
        net = calculate_net_income(income)
        print(f"Income: {format_currency(income)} | Tax: {format_currency(tax)} | Net: {format_currency(net)}")
