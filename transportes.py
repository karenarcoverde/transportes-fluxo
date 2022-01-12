############################################ Dicionario ############################################

dados ={
       "todos_onibus":{}
}


############################################ Classe ##############################################

class Onibus:
    def __init__(self, nome,rotas,motorista,fiscal):
        if ((isinstance(nome,str)) and (isinstance(rotas,list)) and (isinstance(motorista,str)) and (isinstance(fiscal,str))):
            self.nome = nome
            self.rotas = rotas
            self.motorista = motorista
            self.fiscal = fiscal
            
        else:
            print("Algum atributo inválido! ")
        
    def __str__(self):
        return f" Nome ônibus: {self.nome} \n Rotas: {self.rotas} \n Motorista: {self.motorista}  \n Fiscal: {self.fiscal}" 

    def setNome(self,nome):
        if(isinstance(nome,str)):
            self.nome = nome
        else:
            print("Tipo inválido para o nome do ônibus")
        
    def setRotas(self,rotas):  
        if(isinstance(rotas,list)):
            self.rotas = rotas
        else:
            print("Tipo inválido para as rotas")
    
    def setMotorista(self,motorista):
        if(isinstance(motorista,str)):
            self.motorista = motorista
        else:
            print("Tipo inválido para o nome do motorista")
 
    def setFiscal(self,fiscal):
        if(isinstance(fiscal,str)):
            self.fiscal = fiscal
        else:
            print("Tipo inválido para o nome do fiscal")
    
    def criar_onibus (self):
        rotas =[]
    
        # colocando atributos vazios
        onibusAux = Onibus("",[],"","")
        
        # nome do Ônibus
        nome = input("Digite o nome do Ônibus: ")   
        onibusAux.setNome(nome)
        
        # nome do Ponto de parada
        parada = input("Digite SOMENTE um nome do Ponto de parada: ")
        rotas.append(parada)
        onibusAux.setRotas(rotas)
        
        # nome do Motorista
        motorista = input("Digite o nome do Motorista: ")   
        onibusAux.setMotorista(motorista)
        
        # nome do Fiscal
        fiscal = input("Digite o nome do Fiscal: ")   
        onibusAux.setFiscal(fiscal)
        
        print ("\n Ônibus criado com sucesso!\n ")
        return onibusAux
    
    # mostra as informacoes do onibus depois de criá-lo
    def mostrar_onibus (self,onibus):
        print ("---------------------------------------")
        print(f" Nome do ônibus: {onibus.nome}\n") 
        print(" Ponto de parada:") 
        for rota in onibus.rotas:
            print(f" {rota}")
            
        print(f"\n Motorista: {onibus.motorista}\n") 
        print(f" Fiscal: {onibus.fiscal}") 
        print ("---------------------------------------")

    # mostra a lista com todos os onibus e suas respectivas informacoes
    def mostrar_todos_onibus (self, todos_onibus):
        if (len(todos_onibus) > 0 ):
            for onibus in todos_onibus:
                print()
                print ("---------------------------------------")
                print(" Nome ônibus:",todos_onibus[onibus].nome)
                print()
                print (" Rotas:")
                for rota in todos_onibus[onibus].rotas:
                    print(f" {rota}")
                print()
                print(" Motorista:",todos_onibus[onibus].motorista)
                print()
                print(" Fiscal:",todos_onibus[onibus].fiscal)
                print()
                print ("---------------------------------------")
                
        else:
            print ("Nao foi cadastrado nenhum onibus ainda! ")
            
            
    # como so pode um motorista por onibus, eu so vou poder alterar o motorista que já está cadastrado
    def adicionar_motorista_ao_onibus (self, todos_onibus):
        tem_onibus = False
        
        if (len(todos_onibus) > 0):
            # nome do Ônibus
            nome = input("Digite o nome do Ônibus que deseja adicionar o motorista: ")  
            # nome do Motorista
            motorista_nova = input("Digite o motorista que deseja adicionar: ") 
          
            for onibus in todos_onibus:
                if (todos_onibus[onibus].nome == nome):
                    todos_onibus[onibus].motorista = motorista_nova
                    tem_onibus = True
                
            if (tem_onibus == True):
                print("\nMotorista adicionado\n")
                    
            elif (tem_onibus == False):
                print ("\nNão existe esse ônibus na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")


    # como so pode um fiscal por onibus ou nenhum fiscal, eu so vou poder alterar o fiscal que já está cadastrado
    def adicionar_fiscal_ao_onibus (self, todos_onibus):
        tem_onibus = False
        
        if (len(todos_onibus) > 0):
            # nome do Ônibus
            nome = input("Digite o nome do Ônibus que deseja adicionar o fiscal: ")  
            # nome do Fiscal 
            fiscal_nova = input("Digite o fiscal que deseja adicionar: ") 
          
            for onibus in todos_onibus:
                if (todos_onibus[onibus].nome == nome):
                    todos_onibus[onibus].fiscal = fiscal_nova
                    tem_onibus = True
                
            if (tem_onibus == True):
                print("\nFiscal adicionado\n")
                    
            elif (tem_onibus == False):
                print ("\nNão existe esse ônibus na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
    
    # criei uma lista de rotas, entao cada onibus tem uma lista de rotas
    def adicionar_ponto_de_parada_ao_onibus (self, todos_onibus):
        parada_nova=[]
        tem_onibus = False
        
        if (len(todos_onibus) > 0):
            # nome do Ônibus
            nome = input("Digite o nome do Ônibus que deseja adicionar ponto de parada: ")  
            # nome do Ponto de parada
            parada = input("Digite SOMENTE um nome do Ponto de parada que deseja adicionar ao ônibus escolhido: ")
            parada_nova.append(parada)
            for onibus in todos_onibus:
                if (todos_onibus[onibus].nome == nome):
                    todos_onibus[onibus].rotas += parada_nova
                    tem_onibus = True
                    
                    
            if (tem_onibus == True):
                print("\nRotas alteradas!\n")
                    
            elif (tem_onibus == False):
                print ("\nNão existe esse onibus na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
                 
    def alterar_onibus (self, todos_onibus):
        tem_onibus = False
        if (len(todos_onibus) > 0):
            # nome do Ônibus
            nome = input("Digite o nome do ônibus que deseja alterar: ")   
            nome_nova = input("Digite o NOVO nome do ônibus: ")  
            for onibus in todos_onibus:
                if (todos_onibus[onibus].nome == nome):
                    todos_onibus[onibus].nome = nome_nova
                    tem_onibus = True
                    
                    
            if (tem_onibus == True):
                print("\nOnibus alterado!\n")
                    
            elif (tem_onibus == False):
                print ("\nNão existe esse onibus na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
    def alterar_ponto_de_parada (self, todos_onibus):
        tem_parada = False
        if (len(todos_onibus) > 0):
            # nome do Ponto de parada
            parada = input("Digite o nome do Ponto de parada que deseja alterar: ")
            parada_nova = input("Digite o NOVO nome do ponto de parada: ") 
            for onibus in todos_onibus:
                for i in range (len(todos_onibus[onibus].rotas)):
                    if (todos_onibus[onibus].rotas[i] == parada):
                        todos_onibus[onibus].rotas[i] = parada_nova
                        tem_parada = True
                    
            if (tem_parada == True):
                print("\nPonto de parada alterado!\n")
                    
            elif (tem_parada == False):
                print ("\nNão existe esse ponto de parada na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
        
    def alterar_motorista (self, todos_onibus):
        tem_motorista = False
        if (len(todos_onibus) > 0):
            # nome do Motorista
            motorista = input("Digite o nome do motorista que deseja alterar: ")   
            motorista_nova = input("Digite o NOVO nome do motorista: ")  
            for onibus in todos_onibus:
                if (todos_onibus[onibus].motorista == motorista):
                    todos_onibus[onibus].motorista = motorista_nova
                    tem_motorista = True
                    
                    
            if (tem_motorista == True):
                print("\nMotorista alterado!\n")
                    
            elif (tem_motorista == False):
                print ("\nNão existe esse motorista na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
    def alterar_fiscal (self, todos_onibus):
        tem_fiscal = False
        if (len(todos_onibus) > 0):
            # nome do Fiscal
            fiscal = input("Digite o nome do fiscal que deseja alterar: ")   
            fiscal_nova = input("Digite o NOVO nome do fiscal: ") 
          
            for onibus in todos_onibus:
                if (todos_onibus[onibus].fiscal == fiscal):
                    todos_onibus[onibus].fiscal = fiscal_nova
                    tem_fiscal = True
                
            if (tem_fiscal == True):
                print("\nFiscal alterado\n")
                    
            elif (tem_fiscal == False):
                print ("\nNão existe esse fiscal na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
            
    def deletar_onibus (self, todos_onibus):
        
        tem_onibus = False
        if (len(todos_onibus) > 0):
            # nome do Ônibus
            nome = input("Digite o nome do ônibus: ")   
            for onibus in todos_onibus:
                if (todos_onibus[onibus].nome == nome):
                    todos_onibus[onibus].nome = "-"
                    tem_onibus = True
                    
                    
            if (tem_onibus == True):
                print("\nOnibus removido!\n")
                    
            elif (tem_onibus == False):
                print ("\nNão existe esse onibus na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
     
    def deletar_ponto_de_parada (self, todos_onibus): 
         
        tem_parada = False
        if (len(todos_onibus) > 0):
            # nome do Ponto de parada
            parada = input("Digite o nome do Ponto de parada que deseja deletar: ")
            for onibus in todos_onibus:
                for i in range (len(todos_onibus[onibus].rotas)):
                    if (todos_onibus[onibus].rotas[i] == parada):
                        del todos_onibus[onibus].rotas[i]          
                        tem_parada = True
                        pass
                    
                    
            if (tem_parada == True):
                print("\nPonto de parada deletado!\n")
                    
            elif (tem_parada == False):
                print ("\nNão existe esse ponto de parada na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
    def deletar_motorista (self, todos_onibus):
        tem_motorista = False
        if (len(todos_onibus) > 0):
            # nome do Motorista
            motorista = input("Digite o nome do Motorista: ")   
            for onibus in todos_onibus:
                if (todos_onibus[onibus].motorista == motorista):
                    todos_onibus[onibus].motorista = "-"
                    tem_motorista = True
                    
                    
            if (tem_motorista == True):
                print("\nMotorista removido!\n")
                    
            elif (tem_motorista == False):
                print ("\nNão existe esse motorista na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
    
    def deletar_fiscal (self, todos_onibus):
        tem_fiscal = False
        if (len(todos_onibus) > 0):
            # nome do Fiscal
            fiscal = input("Digite o nome do Fiscal: ")   
            for onibus in todos_onibus:
                if (todos_onibus[onibus].fiscal == fiscal):
                    todos_onibus[onibus].fiscal = "-"
                    tem_fiscal = True
                
            if (tem_fiscal == True):
                print("\nFiscal removido!\n")
                    
            elif (tem_fiscal == False):
                print ("\nNão existe esse fiscal na lista! ")
                    
        else:
            print ("\nAinda não existem ônibus criados. ")
         
############################################ Funcoes ##############################################

# opcoes do menu principal que mostram as ações que o usuário quer escolher na gerenciamento da rede de transportes
def menu_principal ():
    print()
    print('##################### MENU PRINCIPAL ############################################')
    print("############# SISTEMA DE GERENCIAMENTO DE UMA REDE DE TRANSPORTES ###############")
    print("1. Criar Ônibus, Ponto de parada, Motorista e Fiscal")
    print("2. Mostrar Ônibus, Ponto de parada, Motorista e Fiscal")
    print("3. Adicionar Relação")
    print("4. Alterar")
    print ("5. Deletar")
    print("6. Sair do Programa")
    print('#################################################################################')
    print()
    print ("OBS:")
    print ("1. Quando não possuir informação sobre algo, preencha com: - ")
    print ("2. As paradas são feitas em ordem")
    print ("3. Um motorista não pode dirigir mais de um ônibus, igual com o fiscal")
    print ("4. Vários ônibus podem parar em um mesmo ponto, mas um ônibus não pode parar mais de uma vez em qualquer ponto")
    print ("5. Cada ônibus tem um motorista e nem sempre um fiscal")
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4','5', '6')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha

def menu_adicionar ():  
    print()
    print('##################### MENU ADICIONAR RELAÇÃO #####################################')
    print("1. Motorista ao ônibus")
    print("2. Fiscal ao ônibus")
    print("3. Ponto de parada ao ônibus")
    print("4. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha

def menu_alterar ():  
    print()
    print('##################### MENU ALTERAR ############################################')
    print("1. Dados do ônibus")
    print("2. Dados da parada")
    print("3. Dados do motorista")
    print("4. Dados do dados do fiscal") 
    print("5. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4','5', '6')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha
  
def menu_deletar ():  
    print()
    print('##################### MENU DELETAR ############################################')
    print("1. Ônibus")
    print("2. Ponto de parada")
    print("3. Motorista")
    print("4. Fiscal")
    print("5. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
        
    escolha = input("Digite o número da opção desejada: ")
        
    while (escolha not in ('1','2','3','4','5')):
        escolha = input("Opção inválida. Digite novamente: ")
                                
    return escolha

# Mostra na tela que o programa terminará
def finalizar_programa ():
    print ("\n##################### Fim do Programa ###############################\n")
         
########################### Main #####################################

def main():
    sair_do_programa = False
    
    # colocando atributos vazios
    onibusObject = Onibus("",[],"","")


    while (sair_do_programa == False):
        
        escolha_menu_principal = menu_principal ()
        
        # opcao 1 - criar Ônibus, ponto de parada, motorista, fiscal:
        if (escolha_menu_principal == "1"):
            onibusAux = onibusObject.criar_onibus ()
            dados["todos_onibus"][onibusAux.nome] = onibusAux
            onibusObject.mostrar_onibus(onibusAux)
            
        
        # opcao 2 - mostrar Ônibus, ponto de parada, motorista, fiscal:  
        if (escolha_menu_principal == "2"):
            onibusObject.mostrar_todos_onibus(dados['todos_onibus'])
            
        # opcao 3 - adicionar relação:
        if (escolha_menu_principal == "3"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):            
                escolha_menu_adicionar = menu_adicionar ()
                
                # opcao 1 - adicionar motorista ao ônibus:
                if (escolha_menu_adicionar == "1"):
                    onibusObject.adicionar_motorista_ao_onibus (dados['todos_onibus'])
                
                # opcao 2 - adicionar fiscal ao ônibus
                if (escolha_menu_adicionar == "2"):
                    onibusObject.adicionar_fiscal_ao_onibus (dados['todos_onibus'])
                
                # opcao 3 - adicionar ponto de parada ao ônibus
                if (escolha_menu_adicionar == "3"):
                    onibusObject.adicionar_ponto_de_parada_ao_onibus (dados['todos_onibus'])
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_adicionar == "4"):
                    voltar_menu_principal = True
            
        
        # opcao 4 - alterar:
        if (escolha_menu_principal == "4"):
             voltar_menu_principal = False
            
             while (voltar_menu_principal == False):
                escolha_menu_alterar = menu_alterar ()
                
                # opcao 1 - alterar dados do ônibus
                if (escolha_menu_alterar == "1"):
                     onibusObject.alterar_onibus(dados['todos_onibus'])
                
                # opcao 2 - alterar dados da parada
                if (escolha_menu_alterar == "2"):
                    onibusObject.alterar_ponto_de_parada(dados['todos_onibus'])
                
                # opcao 3 - alterar dados do motorista
                if (escolha_menu_alterar == "3"):
                    onibusObject.alterar_motorista(dados['todos_onibus'])
                    
                # opcao 4 - alterar dados do fiscal
                if (escolha_menu_alterar == "4"):
                    onibusObject.alterar_fiscal(dados['todos_onibus'])
                
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_alterar == "5"):
                    voltar_menu_principal = True
            
            
            
        # opcao 5 - deletar:
        if (escolha_menu_principal == "5"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):
                escolha_menu_deletar = menu_deletar ()
                
                # opcao 1 - deletar ônibus:
                if (escolha_menu_deletar == "1"):
                    onibusObject.deletar_onibus(dados['todos_onibus'])
                
                # opcao 2 - deletar ponto de parada
                if (escolha_menu_deletar == "2"):
                    onibusObject.deletar_ponto_de_parada(dados['todos_onibus'])
                
                # opcao 3 - deletar motorista
                if (escolha_menu_deletar == "3"):
                    onibusObject.deletar_motorista(dados['todos_onibus'])
                
                # opcao 4 - deletar fiscal
                if (escolha_menu_deletar == "4"):
                    onibusObject.deletar_fiscal(dados['todos_onibus'])
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_deletar == "5"):
                    voltar_menu_principal = True
        
        # opcao 6 - sair do programa:
        if (escolha_menu_principal == "6"):
            sair_do_programa = True
            finalizar_programa ()


#### chamada ao menu
main ()
