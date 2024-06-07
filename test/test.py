def get_requirements():
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
        + "\nEvaluate Calculation: https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html")
    
def calculate_bmi(weight, height):
# Formula: weight (lb) / [height (in)]^2 x 703
bmi = (weight / (height ** 2)) * 703

get_requirements()