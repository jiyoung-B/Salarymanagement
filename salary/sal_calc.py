# sal_calc.py
# sal_no sal_level sal_ho sal_sudang sal_payment sal_tax
# sal_tot_payment

def calc(employee) :
    sal = None
    sal_level = employee["sal_level"]
    sal_ho = employee["sal_ho"]
    sal_sudang = employee["sal_sudang"]
    
    if sal_ho == 1:
        if sal_level == 1:
            sal = 95000
        elif sal_level == 2:
            sal = 80000
    elif sal_ho == 2:
        if sal_level == 1:
            sal = 92000
        elif sal_level == 2:
            sal = 75000
    elif sal_ho == 3:
        if sal_level == 1:
            sal = 89000
        elif sal_level == 2:
            sal = 70000
    elif sal_ho == 4:
        if sal_level == 1:
            sal = 86000
        elif sal_level == 2:
            sal = 65000
    elif sal_ho == 5:
        if sal_level == 1:
            sal = 83000
        elif sal_level == 2:
            sal = 60000
    else:
        sal = 0
        

    sal_diff = None
    
    # 세율과 조정액을 정의합니다.
    tax_rate = 0
    sal_diff = 0
    
    if 70000 <= sal_payment < 80000:
        tax_rate = 0.005
        sal_diff = 300
    elif 80000 <= sal_payment < 90000:
        tax_rate = 0.007
        sal_diff = 500
    elif sal_payment >= 90000:
        tax_rate = 0.012
        sal_diff = 1000
        
    sal_payment = sal + sal_sudang
    sal_tax = (sal_payment * tax_rate) - sal_diff
    sal_tot_payment = sal_payment - sal_tax
    