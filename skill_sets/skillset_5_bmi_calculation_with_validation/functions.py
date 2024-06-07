#!/usr/bin/env python3
"""
Defines four functions:
1. get_requirements()
2. get_height()
3. get_weight()
4. calculate_bmi()
"""

def get_requirements():
    """Accepts 0 args. Displays program requirements and resources."""
    # header and requirements
    print("Developer: Tanner Morlan"
        + "\nBMI Calculator--***No Data Validation!***"
        + "\nProgram Requirements:"
        + "\n1. Research: BMI *English System* formula."
        + "\n2. Must use float data type for user input and calculation."
        + "\n3. Format and round conversion to two decimal places."
        + "\n\n***Resources:***"
        + "\nAccessing Your Weight and Health Risk: https://www.nhlbi.nih.gov/health/educational/lose_wt/risk.htm"
        + "\nBody Mass Index Tables: https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm"
        + "\nEvaluate Calculation: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html"
        + "\nData Validation: https://easypythondocs.com/validation.html"
        + "\n\nInput:")

def get_height():
    """Accepts 0 args. Prompts for height, returns user-entered value. With data validation!"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            height = 0.0 # could leave out this initialization

            # get height (can't change after initial input)
            height = float(input("Enter height (inches): "))

            is_within_range = False
            while not is_within_range:
                if height >= 45 and height <= 80:
                    is_within_range = True
                else:
                    print("Height must be between 45 and 80 inches.\n")
                    height = float(input("Enter height (inches): "))
        
        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return height

def get_weight():
    """Accepts 0 args. Prompts for weight, returns user-entered value. With data validation!"""
    # test valid float and w/in range
    while True:
        try:
            # initialize variable(s)
            weight = 0.0 # could leave out this initialization

            # get weight (can test multiple weights)
            weight = float(input("Enter weight (lbs) (Enter -1 to stop program.): "))

            is_within_range = False
            while not is_within_range:
                if weight == -1:
                    return weight
                
                elif weight >= 80 and weight <= 400:
                    is_within_range = True

                else:
                    print("Weight must be between 80 and 400 pounds.\n")
                    weight = float(input("Enter weight (lbs): "))

        except ValueError:
            print("Not a float! Try again.\n")
            continue
        else:
            return weight

def calculate_bmi(height, weight):
    """Accepts 2 args. Calculate BMI, and prints output."""

    if weight == -1:
        print("Thank you for using the BMI program!")
    else:
        # BMI formula: weight (lb) / [height(in)]^2 x 703
        bmi = weight / height**2 * 703

        print("\nOutput:")
        print("{0}{1:,.2f}{2}{3:,.2f}{4}{5:,.2f}{6}".format("height(inches) = ", height, " | weight(lbs) = ", weight, " | BMI = ", bmi, "\n")) 