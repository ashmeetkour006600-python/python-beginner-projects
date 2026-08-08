#  Password validator

def password():
    ch=str(input("enter your password:"))
    has_digit=False
    for i in ch:
        if  i.isdigit():
            has_digit=True
            break
    has_alpha=False
    for i in ch:
        if i.isalpha():
            has_alpha=True
            break
    has_special=False
    for i in ch:
        if not i.isalnum():
            has_special=True
            break

            
    if has_digit and has_alpha and has_special and len(ch)>=8:
        print("valid password")
        #a=count("ch")
        #print(a)
    else:
        print("not valid")
        print("WHY PASSWOD IS INVALID?")
    if len(ch)<8:
        print("the password must contain 8 digits")
    elif not has_digit:
        print("the password must contaion al least one digit")
    elif not has_special:
        print("password must contain atleast one special character")
    else:
        print("all is well")
    
password()
