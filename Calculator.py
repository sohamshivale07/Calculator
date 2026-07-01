def parse_no(s):
    s=s.strip()

    if not s:
        print("Not a no Error..")
        return None
    
    s=s.replace(',','')
    return float(s)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b==0:
        print("Division by zero Error..")
        return
    return a/b

def accept_no():
    a=parse_no(input("Enter the 1st no:"))
    b=parse_no(input("Enter the 2nd no:"))
    return a,b

def main():
    menu="""
    Simple Calculator:
    1.Additon
    2.Substraction
    3.Multiplication
    4.Division
    5.Exit
    6.Please select a Menu:
    """
    while True:
        choice=int(input(menu).strip())
        if choice==1:
            a,b=accept_no()
            print("Addition is:",add(a,b))

        elif choice==2:
            a,b=accept_no()
            print("Substraction is:",sub(a,b))

        elif choice==3:
            a,b=accept_no()
            print("Multiplication is:",multi(a,b))

        elif choice==4:
            a,b=accept_no()
            print("Divsion is:",div(a,b))

        elif choice==5:
            print("Bye")
            break
        else:
            print("Please choose the menu between 1-5")

        


main()
