while True:
 try:
  a = float(input("Enter first number:"))
  o = str(input("Enter operator(+,-,x,/,%,^):"))
  b = float(input("Enter second number:"))
  match o:
   case "+": print(f"{a} {o} {b} = {a+b}")
   case "-": print(f"{a} {o} {b} = {a-b}")
   case "x": print(f"{a} {o} {b} = {a*b}")
   case "/": print(f"{a} {o} {b} = {a/b}")
   case "%": print(f"{a} {o} {b} = {a%b}")
   case "^": print(f"{a} {o} {b} = {a**b}")
   case _:
     print("Invaild Operator.")
     break

 except ValueError:
  print("Invalid Input.")
  break
