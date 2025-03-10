# India Eiland
# CIS261
# Create and Call Functions with Parameters

from datetime import datetime

def get_date_range():
    while True:
        try:
            from_date = input("Enter FROM date (mm/dd/yyyy): ").strip()
            to_date = input("Enter TO date (mm/dd/yyyy): ").strip()
            from_date_obj = datetime.strptime(from_date, "%m%d%Y")
            to_date_obj = datetime.strptime(to_date, "%m%d%Y")
            if from_date_obj > to_date_obj:
                print("FROM date cannot be later than TO date. Please try again.")
                continue
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
            tax_rate = float(input("Enter tax rate (as a percentage): ").strip()) / 100
            if tax_rate < 0 or tax_rate > 1:
                print("Invalid input! Please enter a tax rate between 0 and 100.")
                continue
            return tax_rate
        except ValueError:
            print("Invalid input! Please input a valid number.")
        
def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
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

def display_totals(totals):
    print("\nPayroll Summary")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours Worked: {totals['total_hours']}")
    print(f"Total Gross Pay: ${totals['total_gross']:.2f}")
    print(f"Total Tax Paid: ${totals['total_tax']:.2f}")
    print(F"Total Net Pay: ${totals['total_net']:.2f}")
    
def main():
    employees = []
    totals = {"total_employees": 0, "total_hours": 0, "total_gross": 0, "total_tax": 0, "total_net": 0}

    while True:
        from_date, to_date = get_date_range()
        name = get_employee_name()
        if name.lower() == 'end':
            break
        
        hours = get_total_hours()
        rate = get_hourly_rate()
        tax_rate = get_tax_rate()
        
        employees.append([from_date, to_date, name, hours, rate, tax_rate])
        
    for emp in employees:
        from_date, to_date, name, hours, rate, tax_rate = emp
        gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
        display_employee_info(from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax, net_pay)
        
        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross'] += gross_pay
        totals['total_tax'] += income_tax
        totals['total_net'] += net_pay
        
    display_totals(totals)
    
if __name__ == "__main__":
    main()