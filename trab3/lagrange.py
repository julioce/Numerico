# coding=UTF-8

import sys, os, math
from fractions import Fraction

# valores iniciais do programa e da matriz
i = 0
j = 0
linhas = 0
colunas = 0
matriz = []
NUMERADOR = 100
BOLD = "\033[1m"
ERROR = "\033[91m"
END = "\033[0m"
mensagemInicial = "Olá! Por favor, digite o nome do arquivo que contem a matriz de pontos a ser lida: "
mensagemErro = ERROR+"\nNão foi possível ler o arquivo!\n"+END
mensagemErroIvalida = ERROR+"O arquivo não contem uma matriz válida!\n"+END

# método para imprimir uma matriz bonitinha
def imprime(matriz):

	align = "<"
	maximo = 0
	
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if len(str(matriz[i][j])) > maximo:
				maximo = len(str(matriz[i][j]))
	print "  x :",
	for i in range(len(matriz)):
		if i!=0:
			print "f(x):",
		for j in range(len(matriz[i])):
			print BOLD+'{0:{align}{width}}'.format(Fraction.from_float(matriz[i][j]).limit_denominator(NUMERADOR), width=maximo, align=align)+END,
		print

# calcula os valores de cada fração
def calcula_Lagrange():

	for i in range(colunas):
	
		#se f(x) ou seja, y == 0 o P(x) é zero
		if matriz[1][i] != 0.0:
			if matriz[1][i] == 1.0:
				print "[",
			else:
				print str(Fraction.from_float(matriz[1][i]).limit_denominator(NUMERADOR))+"*[",
			
			#itera sobre todos os x, fazendo X - Xn
			for j in range(colunas):
				if i!=j:
					#numerador -> detecta se é divisao por 1.0
					if matriz[0][i]-matriz[0][j] == 1.0:
						numerador = ""
					else:
						numerador = "/"+str(Fraction.from_float(matriz[0][i]-matriz[0][j]).limit_denominator(NUMERADOR))

					#numerador/denominador -> com a formatação de sinais de x
					if matriz[0][j] > 0.0:
						print "(x-"+str(Fraction.from_float(matriz[0][j]).limit_denominator(NUMERADOR))+numerador+")",
					elif matriz[0][j] == 0.0:
						print "(x"+numerador+")",
					else:
						print "(x+"+str(Fraction.from_float(abs(matriz[0][j])).limit_denominator(NUMERADOR))+numerador+")",
			
			#fecha o polinômio
			if i < colunas:
				print "]",
			if i < colunas-1 and matriz[1][i+1] >= 0.0:
				print "+"
			else:
				print
		else:
			print "[ 0.0 ] +"
			
		

######################
# Inicio de execução #
######################

# verifica e lê o arquivo da matriz
try:
	os.system('clear')
	file_name = str(raw_input(mensagemInicial))
	if file_name != "":
		file = open('./'+file_name, 'r')
	else:
		file = open('./matriz.txt', 'r')

	#Trasforma o arquivo lido em uma matriz 2D
	for linha in file:
		linha = linha.strip().split(' ')
		matriz.append([])
		matriz[i] = linha
		i += 1
		
	linhas = len(matriz)
	for c in matriz[0]:
		colunas += 1
		
	file.close()
	
except Exception:
	print mensagemErro
	exit()

# transforma os valores lidos de string para float
try:
	for i in range(linhas):
		for j in range(colunas):
			matriz[i][j] = float(matriz[i][j])
			
except Exception:
	print mensagemErro + mensagemErroIvalida
	exit()

print "Este programa leu a seguinte matriz de pontos para x e f(x):"

imprime(matriz)

linhas = len(matriz)
colunas = 0
for c in matriz[0]:
	colunas += 1

#Calcula Lagrange
print "\nPolinômio P"+str(colunas-1)+":"
print BOLD,
calcula_Lagrange()
print END

