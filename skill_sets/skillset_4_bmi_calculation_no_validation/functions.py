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
        + "\n\nInput:")
    
def get_height():
    """Accepts 0 args. Prompts for height, returns user-entered value. No data validation!"""
    # initialize variable(s)
    height = 0.0

    #get height
    height = float(input("Enter height (inches): "))
    return height

def get_weight():
    """Accepts 0 args. Prompts for weight, returns user-entered value. No data validation!"""
    # initialize variable(s)
    weight = 0.0

    #get weight
    weight = float(input("Enter weight (lbs): "))
    return weight

def calculate_bmi(height, weight):
    """Accepts 2 args. Calculates BMI, and prints output."""
    # BMI formula: weight(lb) / [height(in)]^2 x 703
    bmi = weight / height**2 * 703

    print("\nOutput:")
    print("{0}{1:,.2f}{2}{3:,.2f}{4}{5:,.2f}".format("height(inches) = ", height, " | weight(lbs) = ", weight, " | BMI = ", bmi))