# main.py
import sal_input
import sal_calc
import sal_output

print("Program is Start...")
employee = {}
sal_input.myinput(employee) # Call by Reference
sal_calc.mycalc(employee)
sal_output.myoutput(employee)
print("Program is Over...")

