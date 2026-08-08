# CALCULATOR
print("let's start the calculator")
def calculator():
    ch=str(input("enter your choice from (+,-,*,/,%):"))
    a=int(input("enter value:"))
    b=int(input("enter value:"))

    match ch:
        case "+":
            print("addition:",a+b)
        case "-":
            print("substraction:",a-b)

        case"*":
            print("multiplication:",a*b)
        case "/":
            print("division:",a/b)
        case "%":
            print("ramainder:",a%b)
        case _:
            print("invalid chOice")

calculator()
          
