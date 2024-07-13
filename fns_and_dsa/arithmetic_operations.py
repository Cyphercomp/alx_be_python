def perform_operation (num1, num2, operation) : 
    match operation :
        case "add" :
            result= num1 + num2
            print(result)
        case "substract" :
            result= num1 - num2
            print(result)
        case "multiply" :
            result= num1 * num2
            print(result)
        case "divide" :
            if num2 == 0 :
                print("can't divide with zero")
            result= num1 / num2
            print(result)
        case _:
            print("Invalid operation entered.")