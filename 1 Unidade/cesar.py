# encoding: utf-8
#Cifra de César com lista.

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encoding: utf-8
def main():
    op = int(input("Criptografia de Cesar!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    cifra = []
    if op == 1:
        print("[Criptografar]")
        mensagem = list(input('Digite a mensagem:\n'))
        rotacao = int(input('Número da Rotação:\n'))
        
        for i in mensagem: 
            if i in alfabeto:
                ind = alfabeto.index(i) + rotacao
                if ind >= 26:
                    ind -= 26
                cifra += alfabeto[ind]
        print("Mensagem:")
        print(''.join(cifra)) 

    elif op == 2:
        print("[Descriptografar]")
        mensagem = list(input('Digite a mensagem:\n'))
        rotacao = int(input('Número da Rotação:\n'))

        for i in mensagem:
            ind = alfabeto.index(i) - rotacao
            if ind < 0:
                ind += 26
            cifra += alfabeto[ind]
        print("Mensagem:")
        print(''.join(cifra))

    else:
        print('Opção Inválida!')