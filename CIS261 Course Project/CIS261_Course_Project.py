# India Eiland
# CIS261
# Create and Call Functions with Parameters

from datetime import datetime

def get_date_range():
    while True:
        try:
            from_date + input("Enter FROM date (mm/dd/yyyy): ")
            to_date = input("Enter TO date (mm/dd/yyyy): ")
            datetime.strptime(from_date, "%m%d%Y")
            datetime.strptime(to_date, "%m%d%Y")
            return from_date, to_date
        except ValueError:
            print("Invalid date format! Please enter the date in mm/dd/yyyy format.")

def get_employee_name():
    return input("Enter employee's name (or type 'End' to stop): ")

def get_total_hours():
    while True:
        try:
            return float(input("Enter total hours worked: ").strip())
        except ValueError:
            print("Invalid input: please input a valid number.")
            
def get_hourly_rate():
    while True:
        try:
            return float(input("Enter hourly rate: ").strip())
        except ValueError:
            print("Invalid input! Plese input a valid number.")
            
def get_tax_rate():
    while True:
        try:
            return float(input("Enter tax rate (as a percentage): ").strip()) / 100
        except ValueError:
            print("Invalid input! Please input a valid number.")
        
def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay):
    print("\nEmployee Payroll Information")
    print(f"From Date: {from_date}")
    print(f"To Date: {to_date}")
    print(f"Name: {name}")
    print(f"Total hours: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income tax Rate: {tax_rate * 100:.2f}%")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

def display_total(total_employees, total_hours, total_gross, total_tax, total_net):
    print("\nPayroll Summary")
    print(f"Total Employees: {total_employees}")
    print(f"Total Hours Worked: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross:.2f}")
    print(f"Total Tax Paid: ${total_tax:.2f}")
    print(F"Total Net Pay: ${total_net:.2f}")
    
def main():
    total_employees = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0

    while True:
        name = get_employee_name()
        if name.lower() == 'end':
            break
        
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax = get_tax_rate()
        
        gross, tax_amount, net = calculate_pay(hours, rate, tax)
        display_employee_pay(name, hours, rate, gross, tax, tax_amount, net)
        
        total_employees += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax_amount
        total_net += net
        
    display_total(total_employees, total_hours, total_gross, total_tax, total_net)
    
if __name__ == "__main__":
    main()