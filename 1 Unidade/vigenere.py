# encoding: utf-8

plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def format_str( text):
    return text.replace(' ', '').upper()                # Retorna text sem espacos e em maiusculas

def shift_alphabet( alphabet, shift):
    return alphabet[shift:] + alphabet[:shift]          # Retorna alphabet com deslocamento de valor shift

def repeat_password( password, text):
    if len(password) < len(text):                       # Repete a password ate o tamanho de text
        new_pass = password * int((len(text)/len(password)))
        if len(new_pass):
            new_pass += password[:len(new_pass)]
        return new_pass
    return password

def encrypt( plaintext, password, decrypt=False):
    password = repeat_password(password, plaintext)
    plaintext = format_str(plaintext)
    textout = []
    for idx, char in enumerate(plaintext):              # Indice da letra da cifra
        idx_key = plain.find(password[idx])             # Gera alfabeto cifrado
        c_alphabet = shift_alphabet(plain, idx_key)

        if decrypt:
            idx_p = c_alphabet.find(char)
            textout += plain[idx_p]
        else:
            idx_p = plain.find(char)
            textout += c_alphabet[idx_p]
    
    textout = ''.join(textout)
    return textout

def decrypt(ciphertext, password):
    return encrypt(ciphertext, password, True)

def main():
    op = int(input("Cifra Vigenère!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    if op == 1:
        print("[Criptografar]")
        message = input("Digite a mensagem:\n")
        key = input("Digite a Palavra Chave:\n")
        print(encrypt(message,key))
        
    elif op == 2:
        print("[Descriptografar]")
        cipher = input("Digite a mensagem:\n")
        key = input("Digite a Palavra Chave:\n")
        print ("Plaintext:")
        print (decrypt(cipher, key))
    
    else:
        print ("Opção Inválida!")
