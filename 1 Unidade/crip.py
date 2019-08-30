# encoding: utf-8
import cesar
import playfair
import vigenere
import transp_linhas
import mono
import autokey
import transp_linhas_colunas
'''
	[X]		Cifra de Cesar
	[X]		Monoalfabetica 
				- Ordem diferente da cifra de cesar
	[X] 	Playfair
	[X]		Vigenère
	[X]		Autokey
	[X]		Transposição de Linhas
	[X]		Transposição de Linhas e Colunas
	
'''

def menu():
	op = int(input("Algoritmo de Criptografia. Digite:\n1 - Cifra de César\n2 - Cifra Monoalfabetica\n3 - Playfair\n4 - Vigenère\n5 - AutoKey\n6 - Transposição de Linhas\n7 - Transposição de Linhas e Colunas\n0 - Exit\n"))
	if op < -1 or op > 7:
		print("Opção Inválida!\n");
	elif(op == 1):
		cesar.main()
	elif(op == 2):
		mono.main()
	elif(op == 3):
		playfair.main()
	elif(op == 4):
		vigenere.main()
	elif(op == 5):
		autokey.main()
	elif(op == 6):
		transp_linhas.main()
	elif(op == 7):
		transp_linhas_colunas.main()
	elif(op == 0):
		print("Obrigado!")
		exit()

menu()