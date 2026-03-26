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
 
if __name__ == "__main__": 
    test_incomes = [100000, 250000, 400000, 600000, 1000000] 
    for income in test_incomes: 
        tax = calculate_tax(income) 
        print(f"Income: {income:>10,} THB | Tax: {format_currency(tax)}")