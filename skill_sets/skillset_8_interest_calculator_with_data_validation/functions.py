#!/usr/bin/env python3
"""
Defines five functions:

1. get_requirements()
2. get_principal()
3. get_rate()
4. get_years()
5. calculate_interest()

Simple Interest Formula: Interest = P * R * T
P = Principal amount (the beginning balance).
R = Interest rate (usually per year, expressed as a decimal).
T = Number of time periods (generally one-year time periods).

Example:
Principal: $10,000
Rate: 5% (per year)

Interest = $10,000 * 0.05 * 1 = $500

Rate of compounded interest earned over a year is annual percentage yield (APY).
Most banks pay interest monthly, but compounding interval can vary.
Compounding Formula (monthly): CI = P(1 + (r/12))**12t
P = principal (decimal)
r = interst rate (decimal)
t time (integer)
"""

def get_requirements():
    """Accepts 0 args. Displays program requirements."""
    print("Developer: Tanner Morlan."
          + "\nAnnual Compound Interest Investment Report."
          + "\n\nProgram Requirements:"
          + "\n1. Write a program that points a yearly compound interest report table."
          + "\nMust perform data validation."
          + "\n3. ***Extra credit (10pts.):***"
          + "\n\tInstead of annual compound interest rate formula, calculate interest based on a monthly compound interest rate formula."
          + "\n\n***Resource(s):***"
          + "\nhttps://www.fool.com/saving/how-often-is-interest-accrued-on-a-savings-account.aspx"
          + "\nhttps://www.nerdwallet.com/article/banking/how-to-calculate-interest-in-a-savings-account"
          + "\nVerify calculation: https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator"
          + "\n\nInput:")
    
# Input/Process/Output: IPO

def get_principal():
    """Accepts 0 args. Prompts for principal amount, returns user-entered value. With data validation!"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            principal = 0.0 # could leave out this initialization

            # prompt initial investment amount
            principal = float(input("Enter principal: $"))

            is_within_range = False
            while not is_within_range:
                if principal >= 1 and principal <= 1000000:
                    is_within_range = True
                else:
                    print("Principal must be between $1 and $1,000,000.\n")
                    principal = float(input("Enter principal: "))
        
        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return principal
        
def get_rate():
    """Accepts 0 args. Prompts for interest rate, returns user-entered value. With data validation!"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            rate = 0 # could leave out this initialization

            # prompt user interest rate
            rate = float(input("Enter rate (%): "))

            is_within_range = False
            while not is_within_range:
                if rate >= 1 and rate <= 10:
                    is_within_range = True
                else:
                    print("Rate must be between 1% and 10% (no percent sign!).\n")
                    rate = float(input("Enter rate(%): "))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return rate

def get_years():
    """Accepts 0 args. Prompts for number of years, returns user-entered value. With data validation!"""
    # test valid int and w/in range
    while True:
        try:
            # initialize variable(s)
            years = 0 # could leave out this initialization
            # prompt investment years
            years = int(input("Enter years: "))

            is_within_range = False
            while not is_within_range:
                if years >= 1 and years <= 50:
                    is_within_range = True
                else:
                    print("Years must be between 1 and 50.\n")
                    years = int(input("Enter years: "))

        except ValueError:
            print("Not an int! Try again.\n")
            continue
        else:
            return years
"""
def calculate_interest(principal, rate, years):
    total_interest = 0.0 # initialize accumulator for interest
    rate = rate / 100 # convert rate to decimal value
    print() # give vertical space

    # display table header
    print("{0:<4s}{1:>12s}{2:>12s}{3:>12s}".format("Year", "Starting", "Interest", "Ending"))

    # compute and display yearly results
    for year in range(1, years + 1):
        interest = principal * rate
        end_principal = principal + interest

        print("{0:>4d}{1:>12,.2f}{2:>12,.2f}{3:>12,.2f}".format(year, principal, interest, end_principal))

        principal = end_principal
        total_interest += interest

    #display totals
    print("\nEnding principal: ${0:,.2f}".format(end_principal))
    print("Total interest earned: ${0:,.2f}".format(total_interest))
"""

# calculate_interest function edited for extra credit
def calculate_interest(principal, rate, years):
    total_interest = 0.0 # initialize accumulator for interest
    rate = rate / 100 # convert rate to decimal value
    print() # give vertical space

    # display table header
    print("{0:<4s}{1:>12s}{2:>12s}{3:>12s}".format("Year", "Starting", "Interest", "Ending"))

    # compute and display yearly results
    for year in range(1, years + 1):
        starting_principal = principal
        # monthly compound
        principal = principal * (1 + rate / 12) ** 12
        interest = principal - starting_principal

        print("{0:>4d}{1:>12,.2f}{2:>12,.2f}{3:>12,.2f}".format(year, starting_principal, interest, principal))

        total_interest += interest

    #display totals
    print("\nEnding principal (using monthly compound formula): ${0:,.2f}".format(principal))
    print("Total interest earned (using monthly compound formula): ${0:,.2f}".format(total_interest))