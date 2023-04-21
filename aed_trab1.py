def encontrapadrao(mensagem, padrao, qtd):
    ap = 0
    for i in range(0,len(mensagem)):
        if(mensagem[i]==padrao[ap]):
            ap +=1
            if ap == len(padrao):
                return True
                break
    return False

mensagem = input("Digite a Mensagem: ")
while (len(mensagem) == 0 or len(mensagem)>1000):
    mensagem = input("Mensagem nao aceita \nDigite a mensagem novamente: ")

padrao = input("Digite o padrao escolhido: ")
while(len(padrao)== 0 or len(padrao)>100):
    padrao = input("Padrao nao aceito \nDigite novamente o padrao: ")

qtd = int(input("Digite o numero de repeticoes desejada: "))
while (qtd == 0 or qtd>1000):
    qtd = input("Numero de repetiçoes nao permitido \ndigite novamente: ")

#print(type(padrao))
padrao *= qtd

verifica = encontrapadrao(mensagem, padrao, qtd)

if verifica == True:
    print("Essa mensagem é da Alice")
else:
    print("Essa mensagem nao é da Alice")

#print(padrao)