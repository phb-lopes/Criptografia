# encoding: utf-8
#Cifra de César com lista.

alfabeto1 = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
alfabeto2 = ['p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a','z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q']
alfabeto3 = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
alfabeto4 = ['v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f']
alfabeto5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l']
alfabeto6 = ['z', 'y', 'x', 'w', 'v', 'u', 't','a', 'b', 'c', 'd', 'e', 'f', 'g', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'h', 'i', 'j', 'k', 'l']
alfabeto7 = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
alfabeto8 = [ 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a','z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n']
alfabeto9 = ['h', 'i', 'j', 'k', 'l', 'm','z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
alfabeto10 = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','z', 'y', 'x', 'w', 'v','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'k', 'j', 'i',]

def main():
    op = int(input("Criptografia Monoalfabetica!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    cifra = []
    if op == 1:
        print("[Criptografar]")
        mensagem = list(input('Digite a mensagem:\n'))
        num = int(input('Digite um número entre 1 e 10:\n'))
        if num < 1 or num > 10:
            num = int(input("Número inválido!\nDigite um numero entre 1 e 10!"))
        
        if num == 1:
            alfabeto = alfabeto1
        elif num == 2:
            alfabeto = alfabeto2
        elif num == 3:
            alfabeto = alfabeto3
        elif num == 4:
            alfabeto = alfabeto4
        elif num == 5:
            alfabeto = alfabeto5
        elif num == 6:
            alfabeto = alfabeto6
        elif num == 7:
            alfabeto = alfabeto7
        elif num == 8:
            alfabeto = alfabeto8
        elif num == 9:
            alfabeto = alfabeto9
        elif num == 10:
            alfabeto = alfabeto10

        for i in mensagem: 
            if i in alfabeto:
                ind = alfabeto.index(i) + num
                if ind >= 26:
                    ind -= 26
                cifra += alfabeto[ind]
        
        print("Mensagem:")
        print(''.join(cifra)) 

    elif op == 2:
        print("[Descriptografar]")
        mensagem = list(input('Digite a mensagem:\n'))
        num = int(input('Digite um número entre 1 e 10:\n'))
        if num < 1 or num > 10:
            num = input("Número inválido!\nDigite um numero entre 1 e 10!")

        if num == 1:
            alfabeto = alfabeto1
        elif num == 2:
            alfabeto = alfabeto2
        elif num == 3:
            alfabeto = alfabeto3
        elif num == 4:
            alfabeto = alfabeto4
        elif num == 5:
            alfabeto = alfabeto5
        elif num == 6:
            alfabeto = alfabeto6
        elif num == 7:
            alfabeto = alfabeto7
        elif num == 8:
            alfabeto = alfabeto8
        elif num == 9:
            alfabeto = alfabeto9
        elif num == 10:
            alfabeto = alfabeto10

        for i in mensagem:
            ind = alfabeto.index(i) - num
            if ind < 0:
                ind += 26
            cifra += alfabeto[ind]
        print("Mensagem:")
        print(''.join(cifra))

    else:
        print('Opção Inválida!')