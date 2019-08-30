# encoding: utf-8
import aes
import cbc
import ctr
# import ecb
# import cbc
# import ctc

def menu():
	op = int(input("Algoritmo de Criptografia AES. Digite:\n1 - Padrão\n2 - AES - CBC\n3 - AES - CTR\n0 - Exit\n"))
	if op < -1 or op > 7:
		print("Opção Inválida!\n");
	elif(op == 1):
		aes.main()
	elif(op == 2):
		cbc.main()
	elif(op == 3):
		ctr.main()
	elif(op == 0):
		print("Obrigado!")
		exit()

menu()