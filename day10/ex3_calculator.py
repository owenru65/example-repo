
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
  
  print(logo)
  loop = True

  for symbol in operations:
    print(symbol)

  num1 = float(input("What's the first number: "))

  while loop:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    func = operations [operation_symbol]
    answer = func (num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    reply = input(f"Type y to continue calculating with {answer} or type n to exit: ")
    if reply == "n":
      loop = False
      calculator()

    num1 = answer



calculator()





