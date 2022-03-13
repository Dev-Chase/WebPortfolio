print("")


def convert(n):
    ans = ""
    while True:
        ans = ans + str(int(n%2))
        n = n - (int(n%2))
        n = n/2
        if n == 1:
            ans = ans + "1"
            break
    return str(ans[::-1])


while True:
    n = input("What number would you like to convert?: ")
    try:
        int(n)
        if int(n) > 0:
            print(n + " is equivalent to " + str(convert(int(n))) + " in binary format.")
        else:
            print("Sorry, the number must be positive and bigger than 0. Try again.")
    except ValueError:
        if n == "break":
            print("Ending Program.")
            break
        print("Sorry, that didn't work. Try inputing a number.")
