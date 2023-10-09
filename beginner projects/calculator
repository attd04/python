
#add
def add(n1, n2):
    return n1 + n2

#sub
def sub(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2



operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide, 
}



def calculator():

    num1 = float(input("\nWhat's the first number?: "))
    num2 = float(input("What's the second number?: "))
    print("                                       ")
    
    for symbols in operations:
        print(symbols) 
    
    operate = input("\nChoose an operation from the line above: ")
    
    
    defin = (operations[operate])
        
    answer1 = defin(num1, num2)
    
    print(f"\n{num1} {operate} {num2} = {answer1}")
    print("--------------------------------------------")
    
    more = input(f"\nType 'y' to continue calculating with {answer1}, or type 'n' to start a new calculation: ")
    
    
    cont = True
    num1 = answer1
    
    while cont:
        op = input("\nPick another operation: ")
        num3 = float(input("\nWhat's the next number?: "))
        
        calc = operations[op]
        answer2 = calc(num1, num3)
    
        print(f"\n{num1} {op} {num3} = {answer2}")
        print("--------------------------------------------")
    
        more = input(f"\nType 'y' to continue calculating with {answer2}, or type 'n' to start a new calculation: \n")
    
        if more == "y":
            num1 = answer2
            
        if more == "n": 
            cont = False
            print("               \n"*3)
            calculator()
  
    
calculator()

    
    
