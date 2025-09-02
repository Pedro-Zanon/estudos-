#criar as escolhas do usuario 
num1 = float(input("Escolha um número: "))
num2 = float(input("Escolha outro número: "))
opr = input("Escolha uma operação para a conta: ")
#caso o usuario não escolha  a operação certa da erro 
if opr not in ("+", "-", "*","/"):
  print(f"operação inválida")
  opr = input("Escolha novamente uma operação para a conta: ")
elif opr == "+":
  resultado = num1 + num2
elif opr == "-":
  resultado = num1 - num2
elif opr == "*":
  resultado = num1 * num2
elif opr == "/":
  resultado = num1 / num2 
print (f"O resultado da sua conta é igual a {resultado:g}")





  
