










# opcoes do menu principal que mostram as ações que o usuário quer escolher na gerenciamento da rede de transportes
def menu_principal ():
    print()
    print('##################### MENU PRINCIPAL ############################################')
    print("############# SISTEMA DE GERENCIAMENTO DE UMA REDE DE TRANSPORTES ###############")
    print("1. Criar")
    print("2. Mostrar")
    print("3. Adicionar")
    print("4. Alterar")
    print ("5. Deletar")
    print("6. Sair do Programa")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4','5', '6')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha

def menu_criar ():  
    print()
    print('##################### MENU CRIAR ############################################')
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


    
def criar_onibus ():
    print("Não implementado")

def criar_ponto_de_parada ():
    print("Não implementado")

def criar_motorista ():
    print("Não implementado")

def criar_fiscal ():
    print("Não implementado")
    
    
def menu_mostrar ():  
    print()
    print('##################### MENU MOSTRAR ############################################')
    print("1. Ônibus")
    print("2. Rotas")
    print("3. Motoristas")
    print("4. Fiscais")
    print("5. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4','5')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha


    
def mostrar_onibus ():
    print("Não implementado")

def mostrar_rotas ():
    print("Não implementado")

def mostrar_motoristas ():
    print("Não implementado")

def mostrar_fiscais ():
    print("Não implementado")

def menu_adicionar ():  
    print()
    print('##################### MENU ADICIONAR ############################################')
    print("1. Motorista ao ônibus")
    print("2. Fiscal ao ônibus")
    print("3. ponto de parada ao ônibus")
    print("4. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha


    
def adicionar_motorista_ao_onibus ():
    print("Não implementado")

def adicionar_fiscal_ao_onibus ():
    print("Não implementado")

def adicionar_ponto_de_parada_ao_onibus ():
    print("Não implementado")
    

def menu_alterar ():  
    print()
    print('##################### MENU ALTERAR ############################################')
    print("1. Dados do ônibus")
    print("2. Dados da parada")
    print("3. Dados do motorista")
    print("4. Dados do dados do fiscal")
    print("5.Rota do ônibus")  
    print("6. Voltar ao Menu Principal")
    print('#################################################################################')
    print()
    
    escolha = input("Digite o número da opção desejada: ")
    
    while (escolha not in ('1','2','3','4','5', '6')):
        escolha = input("Opção inválida. Digite novamente: ")
                            
    return escolha



def alterar_dados_onibus ():
    print("Não implementado")

def alterar_dados_parada ():
    print("Não implementado")
    
def alterar_dados_motorista ():
    print("Não implementado")

def alterar_dados_fiscal ():
    print("Não implementado")

def alterar_rota_onibus ():
    print("Não implementado")


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


    
def deletar_onibus ():
    print("Não implementado")

def deletar_ponto_de_parada ():
    print("Não implementado")

def deletar_motorista ():
    print("Não implementado")

def deletar_fiscal ():
    print("Não implementado")
    
# Mostra na tela que o programa terminará
def finalizar_programa ():
    print ("\n##################### Fim do Programa ###############################\n")
        
########################### Main #####################################

def main():
    sair_do_programa = False


    while (sair_do_programa == False):
        
        escolha_menu_principal = menu_principal ()
        
        
        # opcao 1 - criar:
        if (escolha_menu_principal == "1"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):
                escolha_menu_criar = menu_criar ()
                
                # opcao 1 - criar ônibus:
                if (escolha_menu_criar == "1"):
                    criar_onibus ()
                
                # opcao 2 - criar ponto de parada
                if (escolha_menu_criar == "2"):
                    criar_ponto_de_parada ()
                
                # opcao 3 - criar motorista
                if (escolha_menu_criar == "3"):
                    criar_motorista ()
                
                # opcao 4 - criar fiscal
                if (escolha_menu_criar == "4"):
                    criar_fiscal ()
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_criar == "5"):
                    voltar_menu_principal = True
            
            
        
        # opcao 2 - mostrar:    
        if (escolha_menu_principal == "2"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):
                escolha_menu_mostrar = menu_mostrar ()
                
                # opcao 1 - mostrar ônibus:
                if (escolha_menu_mostrar == "1"):
                    mostrar_onibus ()
                
                # opcao 2 - mostrar rotas
                if (escolha_menu_mostrar == "2"):
                    mostrar_rotas ()
                
                # opcao 3 - mostrar motoristas
                if (escolha_menu_mostrar == "3"):
                    mostrar_motoristas ()
                
                # opcao 4 - mostrar fiscais
                if (escolha_menu_mostrar == "4"):
                    mostrar_fiscais ()
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_mostrar == "5"):
                    voltar_menu_principal = True
            
            
            
        # opcao 3 - adicionar:
        if (escolha_menu_principal == "3"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):            
                escolha_menu_adicionar = menu_adicionar ()
                
                # opcao 1 - adicionar motorista ao ônibus:
                if (escolha_menu_adicionar == "1"):
                    adicionar_motorista_ao_onibus ()
                
                # opcao 2 - adicionar fiscal ao ônibus
                if (escolha_menu_adicionar == "2"):
                    adicionar_fiscal_ao_onibus ()
                
                # opcao 3 - adicionar ponto de parada ao ônibus
                if (escolha_menu_adicionar == "3"):
                    adicionar_ponto_de_parada_ao_onibus ()
                    
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
                    alterar_dados_onibus ()
                
                # opcao 2 - alterar dados da parada
                if (escolha_menu_alterar == "2"):
                    alterar_dados_parada ()
                
                # opcao 3 - alterar dados do motorista
                if (escolha_menu_alterar == "3"):
                    alterar_dados_motorista ()
                    
                # opcao 4 - alterar dados do fiscal
                if (escolha_menu_alterar == "3"):
                    alterar_dados_fiscal ()
                
                 # opcao 5 - alterar rota do ônibus
                if (escolha_menu_alterar == "3"):
                    alterar_rota_onibus ()
                    
                # opcao 6 - voltar ao menu principal
                if (escolha_menu_alterar == "4"):
                    voltar_menu_principal = True
            
            
            
        # opcao 5 - deletar:
        if (escolha_menu_principal == "5"):
            voltar_menu_principal = False
            
            while (voltar_menu_principal == False):
                escolha_menu_deletar = menu_deletar ()
                
                # opcao 1 - deletar ônibus:
                if (escolha_menu_deletar == "1"):
                    deletar_onibus ()
                
                # opcao 2 - deletar ponto de parada
                if (escolha_menu_deletar == "2"):
                    deletar_ponto_de_parada ()
                
                # opcao 3 - deletar motorista
                if (escolha_menu_deletar == "3"):
                    deletar_motorista ()
                
                # opcao 4 - deletar fiscal
                if (escolha_menu_deletar == "4"):
                    deletar_fiscal ()
                    
                # opcao 5 - voltar ao menu principal
                if (escolha_menu_deletar == "5"):
                    voltar_menu_principal = True
        
        # opcao 6 - sair do programa:
        if (escolha_menu_principal == "6"):
            sair_do_programa = True
            finalizar_programa ()


#### chamada ao menu
main ()
