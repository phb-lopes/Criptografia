from os import system, name

def swap_lines(table, line1, line2):
	num_column = len(table[0])
	for i in range(num_column):
		table[line1][i], table[line2][i] = table[line2][i], table[line1][i]

def swap_columns(table, column1, column2):
	num_lines = len(table)
	for i in range(num_lines):
		table[i][column1], table[i][column2] = table[i][column2], table[i][column1]

def make_matrix(lines, column):
	table = list()
	tmp = list()
	i=int(0)
	j=int(0)
	for i in range(lines):
		for j in range(column):
			tmp.append('-')
		table.append(tmp[:])
		tmp.clear()

	for i in range(lines):
		for j in range(column):
			table[i][j] = input("Digite o elemento [%d][%d]:" %(i+1,j+1)).upper()
	return table

def encrypt(table):
	lista = list()
	num_lines = len(table)
	num_column = len(table[0])

	for i in range(1, num_lines, 2):
		swap_lines(table, i, i-1)
	for j in range(1, num_column, 2):
		swap_columns(table, j, j-1)

	for i in table:
		for j in i:
			lista.append(j)
	lista = ''.join(lista)
	return lista

def decrypt(table):
	lista = list()
	num_lines = len(table)
	num_column = len(table[0])
	
	for j in range(1, num_column, 2):
		swap_columns(table, j, j-1)
	for i in range(1, num_lines, 2):
		swap_lines(table, i, i-1)
	
	for i in table:
		for j in i:
			lista.append(j)
	lista = ''.join(lista)
	return lista


def main():
    op = int(input("Transposição de Linhas e Colunas!\nDigite:\n1 - Criptografar Mensagem\n2 - Descriptografar Mensagem\n"))
    if op == 1:
        print("[Criptografar]")
        lines = int(input("Digite o numero de Linhas:\n"))
        column = int(input("Digite o numero de Colunas:\n"))
        table = make_matrix(lines,column)
        print (encrypt(table))
        
    elif op == 2:
        print("[Descriptografar]")
        lines = int(input("Digite o numero de Linhas:\n"))
        column = int(input("Digite o numero de Colunas:\n"))
        table = make_matrix(lines,column)
        print (decrypt(table))
   
    else:
        print ("Opção Inválida!")
