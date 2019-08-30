# encoding: utf-8

def railfence_id(tam, key):
    '''
    Retorna um lista de inteiros com a posicao da
    linha que o caracter do texto ira ocupar,
    variando de 0 ate key - 1.
    '''
    j = int(0)
    inc = int(0)
    idx = []
    for i in range(tam):
        if j == key - 1:
            inc = -1
        elif j == 0:
            inc = 1
        idx.append(j)
        j += inc
    return idx

def encrypt(texto, key):
    '''
    Retorna o texto plano cifrado na cifra rail
    fence com a chave key.
    '''
    texto = texto.replace(' ', '')
    tam = len(texto)
    idx = railfence_id(tam, key)

    cifrado = ''
    for i in range(key):
        for z in range(tam):
            if idx[z] == i:
                cifrado += texto[z]
    return cifrado.upper()

def decrypt(texto, key):
    '''
    Retorna o texto plano para um texto cifrado
    com a cifra rail fence com a chave key.
    '''
    texto = texto.replace(' ', '')
    tam = len(texto)
    idx = railfence_id(tam, key)
    idx_sorted = sorted(idx)

    texto_plano = ''
    for i in range(tam):
        for j in range(tam):
            if idx[i] == idx_sorted[j] and idx[i] > -1:
                texto_plano += texto[j]
                idx[i] = -1
                idx_sorted[j] = -1
    return texto_plano.lower()

def main():
    op = int(input("Transposição de Linhas!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    
    if op == 1:
        print("[Criptografar]")
        mensagem = input('Digite a mensagem:\n')
        key = int(input("Quantidade de Linhas\n"))
        print(encrypt(mensagem,key))

    elif op == 2:
        print("[Descriptografar]")
        mensagem = input('Digite a mensagem:\n')
        key = int(input("Quantidade de Linhas\n"))
        print(decrypt(mensagem,key))
    else:
        print('Opção Inválida!')