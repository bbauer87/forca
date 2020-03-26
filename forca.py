#Desenvolvido por Bruno S. Bauer

from random import randint,shuffle,sample

palavra=""
dica=""
erros=0
acertos=0
tentativas=1
esconde=[] # palavra oculta

def ler_txt(): ## função para a opção 2 do menu
    try:
        arquivo=open("palavras.txt", 'r', encoding="utf-8")
    except FileNotFoundError:
        arquivo=open("palavras.txt", 'w'); arquivo.close()
        return "arquivo vazio"

    conteudo=arquivo.readlines();        arquivo.close()
    
    ## remover linhas em branco do arquivo txt e espaços em branco à direita
    contador=0
    while "\n" in conteudo: conteudo.remove("\n")
    for x in conteudo:
        corrige=x.rstrip(); conteudo[contador]=corrige; contador+=1    
    ########################################################################
    
    if conteudo==[] or conteudo==[""]:
        return "arquivo vazio"

    result=[] ## cria uma lista de listas, com as respectivas palavras e dicas: [[palavra1,dica1],[palavra2,dica2],...]
    for linha in conteudo:
        try: ## as palavras devem ser separadas das dicas por um "#"
            indice=linha.index("#")
        except:
            return "mal configurado"
        
        palavra=linha[:indice]
        dica=linha[indice+1:]
        if len(palavra)==0 or len(dica)==0: ## erro na configuração do txt: foi inserida palavra sem dica ou dica sem palavra
            return "mal configurado"
        
        tmp=[palavra,dica]
        result.append(tmp)        
    return result

def menu():
    global palavra,dica,esconde
        
    print("\n\n"," "*20, "          Jogo da Forca","\n"," "*20, "-"*33);    print(" "*22,"Desenvolvido por Bruno S. Bauer")
    while True:
        escolha=input("Opções:\n\n[1] Usuário escolhe a palavra (modo para 2 jogadores)\n[2] O jogo escolhe a palavra (modo para 1 jogador)\n[3] Sair\n\n>>> "); print("-"*44)
        if not escolha.isdigit():
            print("\nESCOLHA uma opção válida!\n")
            continue
        escolha=int(escolha)
        if escolha<1 or escolha>3:
            print("\n1, 2 ou 3!!!!\n")
            continue
        
        elif escolha==3:
            print("Adiós!")
            quit()
            
        elif escolha==2:
            arquivo=ler_txt()
            if "vazio" in arquivo:
                print("\nArquivo \"palavras.txt\" vazio... Alimente-o e tente de novo, ou escolha opção 1...\n")
                continue
            if "mal" in arquivo:
                print("\nArquivo \"palavras.txt\" mal configurado... Examine-o e tente de novo, ou escolha opção 1...\n")
                continue
            for sorteio in range(1234):
                shuffle(arquivo)
                escolha=sample(arquivo,1)[0]
            palavra=escolha[0].upper()
            dica=escolha[1]                           
            break
        
        elif escolha==1:
            print("Serão armazenadas 3 palavras e uma delas será sorteada:\n"+"-"*44+"\n")
            palavra0=input("Digite a primeira palavra: ");           dica0=input("Digite a primeira dica: ")
            palavra1=input("Digite a segunda palavra: ");            dica1=input("Digite a segunda dica: ")
            palavra2=input("Digite a terceira palavra: ");           dica2=input("Digite a terceira dica: ")
            print("-"*44)            
            for sorteio in range(1234):
                num=randint(1,9)
            if num>=1 and num<=3:   palavra=palavra0.upper(); dica=dica0
            elif num>=4 and num<=6: palavra=palavra1.upper(); dica=dica1
            else:                   palavra=palavra2.upper(); dica=dica2
            
            print("-\n"*44) ## serve para ocultar as palavras que alguém escolha, dificultando que a outra pessoa tente adivinhar
            break

    for ctesc in range(len(palavra)): ## forma a palavra oculta com base no número de letras da palavra
        esconde.append('_')
    print("\nSorteio realizado!\n")

def procura(): ## função onde o jogador escolhe uma letra, verificando se ela consta ou não na palavra oculta
    global erros,acertos,tentativas
    
    while True:
        if acertos==len(palavra): ## acertou a palavra
            break
        elif erros>5: ## forca
            break
        else: ## segue tentando
            print("-"*44,"\n\n","A palavra tem ", len(palavra), " caracteres.","\n\n",sep="")
            print(esconde,"\n")
            print("-"*44,"\n\n","A dica é: ",dica,"\n\n","-"*44,"\n",sep="")
            
            if erros==5:
                print("-"*44,"\n")
                print("Aviso! Última chance para errar!!!\n"*3)
                print("-"*44,"\n")
            
            print("Tentativa número: ", tentativas)
            print("Acertos | Erros (6 chances): ", acertos," | ", erros, " / 6","\n-"*5,sep="")

            while True:
                letra=input("Digite um caractere ou espaço em branco a procurar: ").upper();                print("-"*44)
                if len(letra)>1:       ## usuário digitou mais de um caractere
                    print("\n>>> Erro: apenas UM caractere!!!!\n"); print("-"*44+"\n"+"-"*44)
                    continue
                elif letra=="":        ## usuário não digitou
                    print("\n>>> Erro: digite um caractere ou um espaço em branco!!\n"); print("-"*44+"\n"+"-"*44)
                    continue            
                elif letra in esconde: ## usuário tentou uma letra já adivinhada
                    print("\n>>> Erro: esse caractere já foi... Tente novamente!\n"); print("-"*44+"\n"+"-"*44)
                    continue                
                else:
                    break            
            
            if letra==" ": print("Numero de vezes que espaço em branco consta:", palavra.count(letra));       print("-"*44,"\n")
            else:          print("Numero de vezes que o caractere \"",letra,"\" consta: ", palavra.count(letra)); print("-"*44,"\n")

            if letra in palavra: acertos+=palavra.count(letra)
            else:                erros+=1; enforcado()

            for ct in range(len(palavra)):
                if palavra[ct]==letra: ## se o caractere escolhido consta na palavra ele é revelado na palavra oculta
                    if letra==" ":  print("Espaço em branco encontrado na posição:     ", ct+1); esconde[ct]=letra
                    else:           print("Caractere encontrado na posição:     ", ct+1);        esconde[ct]=letra
                
                else:
                    if letra==" ":  print("Espaço em branco não encontrado na posição: ", ct+1)
                    else:           print("Caractere não encontrado na posição: ", ct+1)

            print("\n","-"*44,sep="");            print(esconde);            print("-"*44)
            tentativas+=1
            return

def chute(): ## função que pergunta ao jogador se está pronto para tentar adivinhar a palavra
    global acertos,erros
    
    while True:
        escolha=input("\nDeseja chutar ? [1] Sim ou [2] Não  ")
        print("-"*44)
        if not escolha.isdigit():
            print("\nESCOLHA uma opção válida!\n")
            continue
        escolha=int(escolha)
        if escolha<1 or escolha>2:
            print("\n1 ou 2 !!!!\n")
            continue
        elif escolha==2:
            return
        elif escolha==1:
            print("\nAtenção! O jogo termina se errares!!!\n")
            chuta=input("Qual é a palavra??\n>>> ").upper()
            if chuta==palavra:
                acertos=len(palavra)                
            else:
                erros+=10
                print("""
                      #######
                      #     #
                      #     O
                      #  ===|===
                      #     |
                      #     |
                      #   __|__
                      #
                 ###########
                         """)
            return

def jogo(): ## laço que verifica se jogador ganhou, perdeu ou se deve continuar tentando
    while True:
        if erros>5:
            print("-"*44);            print(f"\nFORCA! A palavra era: {palavra}\n")
            break
        if acertos==len(palavra):
            print("-"*44);            print(f"\nGANHOU! A palavra é: {palavra}\n")
            break
        else:
            if tentativas==1:
                procura()
            else:
                chute()
                procura()

def enforcado(): ## função invocada a cada erro do jogador, mostrando a forca com base no número de erros
    if erros==1:
        print("""
              #######
              #     #
              #     O
              #
              #
              #
              #
              #
         ###########
         """)
              
    elif erros==2:
        print("""
              #######
              #     #
              #     O
              #     |
              #
              #
              #
              #
         ###########
         """)
    elif erros==3:
        print("""
              #######
              #     #
              #     O
              #     |===
              #
              #
              #
              #
         ###########
         """)
    elif erros==4:
        print("""
              #######
              #     #
              #     O
              #  ===|===
              #
              #
              #
              #
         ###########
         """)
    elif erros==5:
        print("""
              #######
              #     #
              #     O
              #  ===|===
              #     |
              #     |
              #     |__
              #
         ###########
         """)
    else:
        print("""
              #######
              #     #
              #     O
              #  ===|===
              #     |
              #     |
              #   __|__
              #
         ###########
         """)

def jogar(): ## função que verifica se usuário quer jogar novamente ou não, resetando as variáveis
    global palavra,dica,erros,acertos,tentativas,esconde
    
    while True:
        de_novo=input("Jogar novamente? [1] Sim ou [2] Não  ")
        print("-"*44)
        if not de_novo.isdigit():
            print("\nESCOLHA uma opção válida!\n")
            continue
        de_novo=int(de_novo)
        if de_novo<1 or de_novo>2:
            print("\n1 ou 2 !!!!\n")
            continue
        elif de_novo==2:
            print("Tchau!")
            break
        elif de_novo==1:
            palavra="";    dica="";   tentativas=1
            erros=0;       acertos=0; esconde=[]            
            menu()
            jogo()
            jogar()
            return

menu()
jogo()
jogar()
