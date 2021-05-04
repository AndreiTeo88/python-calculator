from art import logo

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
def exponent(n1, n2):
  return n1 ** n2
def percentage(n1, n2):
  return (n1 / n2) * 100
def modulo_operator(n1, n2):
  return n1 % n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  "**": exponent,
  "percentage": percentage,
  "modulo": modulo_operator,
}

def the_calculator():
  print(logo)

  num1 = float(input("What's the first number: "))

  for sign in operations:
    print(sign)

  should_continue = True
  while should_continue:
    operation_sign = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))

    calculator = operations[operation_sign]
    answer = round(calculator(num1, num2), 4)
    
    print(f"{num1} {operation_sign} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      the_calculator()

the_calculator()
