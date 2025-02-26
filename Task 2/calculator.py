print("CALCULATOR ")

while True:
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("0. quit")

    try:
        operation = int(input("choose an operation: "))
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 4.")
        continue
        
    if operation == 0:
        print("Good bye!")
        break
    if operation in [1,2,3,4]:
        try:
            num1 = float(input('ENTER FIRST NUMBER: '))
            num2 = float(input('ENTER SECOND NUMBER: '))
        except ValueError:
            print("Invalid input Please enter number only.")
            continue
        if operation == 1 :
          result = num1 + num2
        elif operation == 2 :
            result = num1 - num2
        elif operation == 3 :
            result = num1 * num2
        elif operation == 4 :
          if num2 != 0:
           result = num1 / num2
          else:
             result = "can't divide by zero."
    else:
        print("invalid operation")

    print(f"Result: {result}")
