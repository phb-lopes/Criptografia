# encoding: utf-8
from random import randrange, getrandbits
# ========================================================================
# 					Testa se o numero é primo
# (n numero a ser testado, k = numero de vezes para fazer o teste)
def is_prime(n, k = 128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

# ========================================================================
# 					Gerador de números candidatos a ser primo
# (length é o tamanho em bits do número a ser gerado)
def generate_prime_candidate(length):
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

# ========================================================================
# 					Gerador de número primo
# (length é o tamanho em bits do número a ser gerado)
def generate_prime_number(length=512):
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p
 
# ========================================================================
# 					Função para saber qual numero é maior
def maior(a,b):
    if a > b:
        return a
    else:
        return b

# ========================================================================
#			Descorbrir o D a partir do E calculando o módulo inverso
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# ========================================================================
#						Criptografar

def criptografar(mensagem,e,n):
    cifra = []   
    print("-   ",mensagem,"   -")
    ind = pow(mensagem,e,n)
    print("Mensagem:")
    print(ind)
# ========================================================================
#						Descriptografar
def descriptografar(mensagem,d,n):
    cifra = []
    print("-   {}   - D = {}".format(mensagem,d))
    ind = pow(mensagem,d,n)
    print("Mensagem:")
    print(ind)


# ========================================================================
#						Menu principal
op = int(input("Criptografia RSA!\nDigite:\n1 - Usar chaves gerados pelo Sistema\n2 - Entrar com os próprios chaves\n"))


# ========================================================================
#						Geração automática dos números
if op == 1:
    
    opp = 1
    print("Chaves Gerados")
    p = generate_prime_number()
    q = generate_prime_number()
    n = p*q
    fi_n = (p-1)*(q-1)
    e = generate_prime_number()
    d = modinv(e, fi_n)

    print("P = {}\nQ = {}\nN = {}\nFi de N = {}\n[\nE = {}\nD = {}\n]".format(p,q,n,fi_n,e,d))

    while opp:
        cifra = []
        opp = int(input("Digite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n0 - Sair\n"))
        if opp == 1:
            print("[Criptografar]")
            mensagem = int(raw_input('Digite a mensagem:\n'))
            if(mensagem > n):
                mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
                while (mensagem > n):
                    mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
            criptografar(int(mensagem),e,n)
        elif opp == 2:
            print("[Descriptografar]")
            mensagem = int(raw_input('Digite a mensagem:\n'))
            if(mensagem > n):
                mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
                while (mensagem > n):
                    mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
            descriptografar(int(mensagem),d,n)
        elif opp == 0:
            print('Obrigado!')
            exit()
        else:
            print('Opção Inválida!')    

# ========================================================================
#						Entrar com os dados
elif op == 2:
    opp = 1
    print("Entrada de Dados")
    p = int(input('Digite o Primeiro número [P]\n'))
    if is_prime(p) == False:
        p = int(input("O número precisa ser primo, Por favor selecione outro!\n"))
        while is_prime(p) == False:
            p = int(input("O número precisa ser primo, Por favor selecione outro!\n"))


    q = int(input('Digite o Segundo número [Q]\n'))
    if is_prime(q) == False:
        q = int(input("O número precisa ser primo, Por favor selecione outro!\n"))
        while is_prime(q) == False:
            q = int(input("O número precisa ser primo, Por favor selecione outro!\n"))

    n = p*q
    fi_n = (p-1)*(q-1)
    

    e = int(input('Digite o E\nEle precisa ser Primo e menor que {}\n'.format(maior(p,q))))
    if is_prime(e) == False:
        e = int(input("O número precisa ser primo, Por favor selecione outro\n"))
        while is_prime(e) == False:
            e = int(input("O número precisa ser primo, Por favor selecione outro\n"))
    
    d = modinv(e, fi_n)

    # ========================================================================
    # p = 13
    # q = 17
    # e = 7
    # n = p*q
    # fi_n = (p-1)*(q-1)
    # d = modinv(e, fi_n)

    print("P = {}\nQ = {}\nN = {}\nFi de N = {}\n[E = {} | D = {}]".format(p,q,n,fi_n,e,d))
    while opp:
        opp = int(input("Digite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n0 - Sair\n"))
        if opp == 1:
            print("[Criptografar]")
            mensagem = int(raw_input('Digite a mensagem:\n'))
            if(mensagem > n):
                mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
                while (mensagem > n):
                    mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
            criptografar(int(mensagem),e,n)
        elif opp == 2:
            print("[Descriptografar]")
            mensagem = int(raw_input('Digite a mensagem:\n'))
            if(mensagem > n):
                mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
                while (mensagem > n):
                    mensagem = int(raw_input('A mensagem precisa ser menor que {}\nDigite a mensagem:\n'.format(n)))
            descriptografar(int(mensagem),d,n)
        elif opp == 0:
            print("Obrigado!")
            exit()
elif op == 0:
    print("Obrigado!")
    exit()