# coding=UTF-8

import sys, math

def aplicaFuncao(funcao, x):
	valor = 0.0
	fator = funcao.strip().split(' ')
	for i in fator:
		i = i.replace("(", "*(")
		valor += eval(i)
	print "\nO valor de", x, "em Pn(x) é", valor, "\n"

aplicaFuncao(sys.argv[1], float(sys.argv[2]))
	
