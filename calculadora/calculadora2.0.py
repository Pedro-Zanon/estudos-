

#criar uma classe para a calculadora
class calculadora():
  #função sempre executada ao iniciar a class, geralmente usada para iniciar variaveis
  def __init__ (self):
    self.num1 = float(input("escolha um mother fucker number: "))
    self.num2 = float(input("escolha um outro numero: "))
    self.opr = input("Escolha uma operação: ")
    self.salv = f"{self.num1} {self.opr} {self.num2}"
    self.verificacao() 
  #função para verificar se o usuario digitou algo errado
  def verificacao(self):
    if  "/ 0" in self.salv:
      print ("ipossivel dividir por zero")
      self.__init__()
  #verifica se a operação é valida
    elif self.opr not in ("+", "-", "*","/"):
      print("Operação inválida")
      self.opr = input("Escolha novamente uma operação para a conta: ")
      self.verificacao()
    else: 
      self.operacao()
  #função para realizar a operação
  def operacao(self):
        if   self.opr == "+":
           resultado = self.num1 + self.num2
        elif self.opr == "-":
           resultado = self.num1 - self.num2
        elif self.opr == "*":
           resultado = self.num1 * self.num2
        elif self.opr == "/":
           resultado = self.num1 / self.num2
        print (f"O resultado da sua conta é igual a {resultado:g}")

        
#self e def  não nescessitam ser chamados por ordem,
# posso chamar eles de qualquer lugar dentro da class
#self cria uma variavel global dentro da class
# def é usado para criar funções dentro da class

      











#inicar a classe/executar o código
conta = calculadora()