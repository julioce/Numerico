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
	
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print BOLD+'{0:{align}{width}}'.format(Fraction.from_float(matriz[i][j]).limit_denominator(NUMERADOR), width=maximo, align=align)+END,
		print

#formata o polinomio com índices fracionários e tal
def formata_Pol(resolucaoX):
	polinomio = ""
	contador = 0
	
	for i in resolucaoX:
		i = str(Fraction.from_float(i).limit_denominator(NUMERADOR))
		if i[:1]!="-":
			i = "+"+i
			
		if contador==0:
			polinomio += i+" "
		elif contador==1:
			polinomio += i+"x "
		else:
			polinomio += i+"xˆ"+str(contador)+" "
		contador += 1
		
	print BOLD+polinomio+END+"\n"


def monta_matriz_SL():

	matriz_SL = []
	
	for i in range(colunas):
		matriz_SL.append([])
		for j in range(colunas):
			matriz_SL[i].append(math.pow(matriz[0][i], j))
			
	imprime(matriz_SL)
	
	return matriz_SL
	

def initMatriz(dim):
	m = []
	for i in range (0, dim):
		m.append([])
		for j in range(0, dim):
			m[i].append(0)
	return m


def termoM(matriz, l, c):
	m = matriz[l][c] / float(matriz[c][c])
	return m


def linhaMenosLinha(l1, fator, l2):
	tam = len(l1)
	for i in range(0, tam):
		l1[i] = l1[i] - fator*l2[i]
	return l1


def calcularLU(matrizA):
	dim = len(matrizA[0])
	tempA = matrizA[:]
	matrizL = initMatriz(linhas)

	for i in range(0, dim):
		matrizL[i][i] = 1

	for c in range(0, dim):
		for l in range(c+1, dim):
			tm = termoM(tempA, l, c)
			tempA[l] = linhaMenosLinha(tempA[l], tm, tempA[c])

			matrizL[l][c] = tm

	return (matrizL, tempA)

# vetor y parcial do cálculo do SL
def calcularY(matriz, resolucaoY, vetor_b):

	for k in range(linhas):
		somatorio = 0.0
		for i in range(k):
			somatorio += matriz[k][i]*resolucaoY[i]
			
		resolucaoY.append( (vetor_b[k]-somatorio) / matriz[k][k] )

# calcula o vetor final x solução do SL
def calcularX(matriz, resolucaoX, resolucaoY):
	
	for k in range(linhas):
		somatorio = 0.0
		for i in range(k):
			somatorio += matriz[linhas-k-1][linhas-i-1]*resolucaoX[i]
		resolucaoX.append( (resolucaoY[linhas-k-1]-somatorio) / matriz[linhas-k-1][linhas-k-1] )


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

print "\nA matriz de Polinômios é:"
matriz_SL = monta_matriz_SL()
linhas = len(matriz_SL)
colunas = 0
for c in matriz_SL[0]:
	colunas += 1

#Resolve o SL associado 
res = calcularLU(matriz_SL)

resolucaoY = []
calcularY(res[0], resolucaoY, matriz[1])

resolucaoX = []
calcularX(res[1], resolucaoX, resolucaoY)
resolucaoX.reverse()

#formata o polinomio
print "\nPolinômio P"+str(colunas-1)+":"
formata_Pol(resolucaoX)

