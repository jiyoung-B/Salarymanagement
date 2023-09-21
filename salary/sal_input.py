# input the info
# sal_no / level/ ho/ sudang/ payment/ tax / tot_payment / diff(조정액)

def myinput(employee) :
    sal_no = input("사원번호 : ")
    sal_level = int(input("급수 : "))
    sal_ho = int(input("호 : "))
    sal_sudang = int(input("수당 : "))
    employee['sal_no'] = sal_no
    employee['sal_level'] = sal_level
    employee['sal_ho'] = sal_ho
    employee['sal_sudang'] = sal_sudang
