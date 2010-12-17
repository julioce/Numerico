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

# método para imprimir a matriz lida bonitinha
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


# método para imprimir uma matriz das divisões divididas
def imprime_Newton(matriz):

	align = "<"
	maximo = 0
	
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if len(str(matriz[i][j])) > maximo:
				maximo = len(str(matriz[i][j]))
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] != "":
				print BOLD+'{0:{align}{width}}'.format(Fraction.from_float(matriz[i][j]).limit_denominator(NUMERADOR), width=maximo, align=align)+END,
			else:
				print BOLD+'{0:{align}{width}}'.format(matriz[i][j], width=maximo, align=align)+END,
		print


# percorre a diagonal principal da matriz dos f[x0], f[x1] ... em busca dos coeficientes
def seleciona_Coeficientes(matriz_Fxn, matriz):

	print "\nPolinômio P"+str(colunas-1)+":"

	fator = ""

	for i in range(colunas):
		for j in range(colunas):
			#pula se der 0
			if i==j and i==0:
				print BOLD+str(Fraction.from_float(matriz_Fxn[i][j]).limit_denominator(NUMERADOR))+fator+END,
			
			#coeficiente diferente de 0 
			elif i==j:
				#imprime a diferenca
				if matriz[0][j-1] != 0.0:
					if matriz[0][j-1] > 0.0:
						fator += "(x-"+str(Fraction.from_float(abs(matriz[0][j-1])).limit_denominator(NUMERADOR))+")"
					else:
						fator += "(x+"+str(Fraction.from_float(abs(matriz[0][j-1])).limit_denominator(NUMERADOR))+")"
				else:
					fator += "(x)"

				#coeficiente da matriz com sinal
				if matriz_Fxn[i][j] > 0.0:
					print BOLD+"+"+str(Fraction.from_float(matriz_Fxn[i][j]).limit_denominator(NUMERADOR))+fator+END,
				else:
					print BOLD+str(Fraction.from_float(matriz_Fxn[i][j]).limit_denominator(NUMERADOR))+fator+END,
	print "\n"


# calcula uma matriz dos f[x0], f[x1] ...
def calcula_Newton(matriz):

	print "\nMatriz associada de diferenças divididas:"

	#cria matriz de F[xn] a primeira coluna igual aos pontos xn
	matriz_Fxn = []
	for i in range(colunas):
		matriz_Fxn.append([])
		if i!=colunas-1:
			print "fx"+str(i)+"\t\t",
		else:
			print "fx"+str(i)+"\t\t"
		for j in range(colunas):
			matriz_Fxn[i].append([])
			matriz_Fxn[i][j] = ""
		#inverte as linhas e colunas
		matriz_Fxn[i][0] = matriz[1][i]

	#faz o cálculo efetivo das diferenças divididas
	for j in range(colunas):
		for i in range(colunas):
			#define a linha em que se quer fazer a diferenca
			if i<=j and j<(colunas-1):
				matriz_Fxn[j+1][i+1] = (matriz_Fxn[j+1][i]-matriz_Fxn[j][i])/(matriz[0][j+1]-matriz[0][j-i])

	#matriz associada
	imprime_Newton(matriz_Fxn)

	#busca os coeficientes do polinômios
	seleciona_Coeficientes(matriz_Fxn, matriz)



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

#Calcula Newton
calcula_Newton(matriz)

