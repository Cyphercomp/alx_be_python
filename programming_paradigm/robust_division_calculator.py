def safe_divide(numerator, denominator) :
    try:
        num = float(numerator)
        denum = float(denominator)
    except ValueError:
        print("Enter a numeric value")
    else :
        try:
            num/denum
        except ZeroDivisionError:
            print("You can't divide by 0!")
        else:
            return print(f"the result of the division is {num/denum}")


safe_divide(9,"zero")
