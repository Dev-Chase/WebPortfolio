def get_hyp(a, b):
    return ((a**2)+(b**2))**0.5

def get_cath(c, a):
    return ((c**2)-(a**2))**0.5

while True:
    hyp_or_cath = input("Would you like to find the length of the hypotenus or the cathetus?: ")
    if hyp_or_cath.lower() == "hyp" or hyp_or_cath.lower() == "hypotenuse":
        a = input("What would you like the length of the first cathetus to be?: ")
        b = input("What would you like the length of the second cathetus to be?: ")
        try:
            float(a)
            float(b)
            print("The length of the hypotenuse is equal to", get_hyp(float(a), float(b)))
        except ValueError:
            print("Sorry that didn't work. Try inputing a number.")
    elif hyp_or_cath.lower() == "cath" or hyp_or_cath.lower() == "cathetus":
        c = input("What would you like the length of the hypotenuse to be?: ")
        a = input("What would you like the length of the known cathetus to be?: ")
        try:
            float(a)
            float(c)
            print("The length of the other cathetus is equal to", get_cath(float(c), float(a)))
        except ValueError:
            print("Sorry that didn't work. Try inputing a number.")
    elif hyp_or_cath.lower() == "break":
        print("Ending Program.")
        break
    else:
        print("Sorry, that's not an option")