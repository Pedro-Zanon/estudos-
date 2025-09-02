#fazer algo usando booleanos

#coisa para melhorar
#quando pego ou guardo algo eu volto para o menu ao inves de voltar para o local

class Geladeira:

    def __init__(self):
        self.pg = False
        self.pf = False
        self.itemg = ["leite", "tênis", "reator de fusão nuclear"]
        self.itemf = ["gelo", "sorvete","corpo morto"]
        self.bag = ["glock 48", "dvd do filme click", "sansung j2"]
        self.menu_principal()
       

    def menu_principal(self):
        while True:
            esc = input(
                "Escolha: \n"
                "1 - Abrir porta da geladeira\n"
                "2 - Abrir porta do freezer\n"
                "3 - Abrir bag\n"
                "4 - Sair\n"
                "Digite a opção desejada: "
            )
            if esc == "1":
              self.abrir_geladeira()
            elif esc == "2":
              self.abrir_freezer()
            elif esc == "3":
                print ("Itens na bag ", self.bag)
                print ("voltando para o menu...")
            elif esc == "4":
              print("Saindo...")
              break
            else:
              print("opção inválida!")
           
    def abrir_geladeira(self):
       self.pg == True
       print("Você abriu a geladeira. O que você quer?: ")
       ação = input(
            "Escolha: \n"
            "1 - Fechar porta da geladeira\n"
            "2 - Pegar algo\n"
            "3 - Guadar algo\n"
            "4 - Voltar ao menu\n"
            "Digite a opção desejada: "
       )
       if ação == "1":
          self.pg = False
          print("Você fechou a geladeira.")
       elif ação == "2":
          if self.itemg:
             print("Itens na geladeira:", self.itemg) 
             item = input("Qual item você quer pegar?\n"
             "")
             if item in self.itemg:
                 self.itemg.remove(item)
                 self.bag.append(item)
                 print(f"Você pegou {item}.")
             else:
                 print("A geladeira está vaiza.")    
       elif ação == "3":
                if self.itemg:
                 print("Itens na bag:", self.bag)
                 print("Itens na geladeira:", self.itemg)
                 item = input("Qual item você quer colocar?\n"
                 "")
                 if item not in self.bag:
                    print("você não possui esse item!")
                 elif item not in self.itemg:
                    self.bag.remove(item)
                    self.itemg.append(item)
                    print(f"Você adicionou {item} na geladeira")
                 elif item.lower() == "sair":
                     print("Voltando para o menu principal...")
                     return
                
             
                 else:
                  print("Esse item não está na geladeira")
          
       elif ação == "":
          print("Voltando para o menu principal...")
       else:
          print("Opção inválida!")
    
    def abrir_freezer(self):
        self.pf = True
        print("Você abriu o freezer. O que você quer?: ")
        ação = input(
            "Escolha: \n"
            "1 - Fechar porta do freezer\n"
            "2 - Pegar algo\n"
            "3 - Guardar algo\n"
            "4 - Voltar ao menu\n"
            "Digite a opção desejada: "
        )
        if ação == "1":
            self.pf = False
            print("Você fechou a porta do freezer.")
        elif ação == "2":
            if self.itemf:
                print("Itens disponíveis na geladeira:", self.itemf)
                item = input("Qual item você quer pegar?\n"
                "")
                if item in self.itemf:
                    self.itemf.remove(item)
                    self.bag.append(item)
                    print(f"Você pegou {item}.")                    
                elif item.lower() == "sair":
                     print("Voltando para o menu principal...")
                     return
                
                else:
                    print("Esse item não está no freezer.")
            else:
                print("O freezer está vazio.")
        elif ação == "3":
            if self.itemf:
                print("Itens na bag:", self.bag)
                print("Itens no freezer:", self.itemf)
                item = input("Qual item você quer colocar?\n"
                "")
                if item not in self.bag:
                    print("você não possui esse item!")
                elif item not in self.itemf:
                    self.bag.remove(item)
                    self.itemf.append(item)
                    print(f"Você adicionou {item} no freezer")
                elif item.lower() == "sair":
                     print("Voltando para o menu principal...")
                     return
                
                else:
                    print("Esse item já está no freezer.")
        
        elif ação == "4":
          print("Voltando para o menu principal...")
        else:
            print("Opção inválida!")   

       
       
       
       
c = Geladeira()