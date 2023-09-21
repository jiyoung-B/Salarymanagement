# print the data of salary
# sal_no / level/ ho/ sudang/ payment/ tax / tot_payment / diff(조정액)

def myoutput (employee) :
    print("                          <<급여 관리 프로그램>>                          ")
    print("-------------------------------------------------------------------------")
    print("사번\t급수\t호\t수당\t지급액\t세금\t차인지급액")
    print("-------------------------------------------------------------------------")
    print(f"{employee['sal_no']}\t{employee['sal_level']}\t{employee['sal_ho']}\t{employee['sal_sudang']}\t{employee['sal_payment']}\t{employee['sal_tax']}\t{employee['sal_tot_payment']}")