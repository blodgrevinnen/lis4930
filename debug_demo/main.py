#!/usr/bin/env python3

import functions as f

def main():

    # fix lack of init variables
    
    base_pay = 0
    overtime_pay = 0
    holiday_pay = 0
    gross_pay = 0

    f.get_requirements() # fix spelling
    f.calculate_payroll(base_pay, overtime_pay, holiday_pay, gross_pay) # fix spelling & add variables


if __name__=="__main__": # fix spelling
    main()
