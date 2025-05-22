
while True:
 try:
  a = float(input("Enter first number:"))
  o = str(input("Enter operator(+,-,x,/,%,^):"))
  b = float(input("Enter second number:"))
  r = None
  match o:
   case "+": r = a + b
   case "-": r = a - b
   case "x" | "*": r = a * b
   case "/": r = a / b
   case "%": r = a % b
   case "^": r = a ** b
   case _:
     print("Invaild Operator.")
     break
  print(f"{a} {o} {b} = {format(r, '.20f').rstrip('0').rstrip('.')}")
 except ValueError:
  print("Invalid Input.")
  break
 except Exception as e:
  print(f"An error occurred:{e}")
