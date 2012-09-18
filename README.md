UFRJ - Universidade Federal do Rio de Janeiro
=============
Compilação de códigos para a disciplina de Cálculo Numérico
=============

Trabalho 1 - Cálculo de Raízes de uma função
-----------

	Parâmetros de chamada: python trab1.py
	Parâmetros do problema: Função definida no código
	Arquivos auxiliares utilizados: N/A
	Programa auxiliar: N/A
	Forma de uso:
		1. Execução do programa
		2. Escolha do método a ser usado
		3. Exibição da raiz calculada
	
Trabalho 2 - Resolução de Sistemas Lineares
-----------

	Parâmetros de chamada: python <método a ser escolhido>.py ou python LU.py <arquivo da matriz a ser lida>
	Parâmetros do problema: N/A
	Arquivos auxiliares utilizados: matriz.txt matrizHilbert.txt
	Programa auxiliar: fazmatrizHilbert.py <numero de linhas ou colunas>
	Forma de uso:
		1. Execução do programa
		2. Exibição do vetor solução

Trabalho 3 - Interpolação de pontos
-----------

	Parâmetros de chamada: python <método a ser escolhido>.py
	Parâmetros do problema: N/A
	Arquivos auxiliares utilizados: matriz.txt
	Programa auxiliar: N/A
	Forma de uso:
		1. Execução do programa
		2. Exibição da função interpoladora
	
Trabalho 4 - Ajuste de curvas (Método dos Mínimos Quadrados)
-----------

	Parâmetros de chamada: python quadrados.py <arquivos da matriz de pontos a ser lida>
	Parâmetros do problema: N/A
	Arquivos auxiliares utilizados: N/A
	Programa auxiliar: N/A
	Forma de uso:
		1. Execução do programa
		2. Escolha do método de ajuste
			2a. Ajuste polinomial
			2b. Ajuste Hiperbólico (linearização)
			2c. Ajuste Logarítico/exponencial (linearização)
		3. Exibição da função de ajuste
	
Trabalho 5 - Integração numérica
-----------

	Parâmetros de chamada: python integral.py <função a ser calculada> <início do intervalo> <fim do intervalo> <range de subdivisões>
	Parâmetros do problema: N/A
	Arquivos auxiliares utilizados: N/A
	Programa auxiliar: N/A
	Forma de uso:
		1. Execução do programa
		2. Escolha do método de cálculo
			2a. Método dos Trapézios Repetidos
			2b. Método de 1/3 de Simpson Repetido
			2c. Comparativo entre 1 e 2 (Executa ambos os métodos)
		3. Exibição do resultado da integral
	
Trabalho 6 - Cálculo da EDO
-----------

	Parâmetros de chamada: python edo.py <função a ser calculada> <x inicial> <f(x) inicial> <x final> <range de subdivisões> <a1> <a2> <b1> <b2> <f'(x) - resposta exata para cálculo do erro>
	Parâmetros do problema: N/A
	Arquivos auxiliares utilizados: N/A
	Programa auxiliar: N/A
	Forma de uso:
		1. Execução do programa
		2. Escolha do método de cálculo
			2a. Método de Euler
			2b. Método de Runge-Kutta (segunda ordem)
			2c. Método de Runge-Kutta (quarta ordem)
		3. Exibição da função da EDO
	

Este README tem apenas como função analisar brevemente o uso/utilidade de cada programa assim como o seu funcionamento básico. Mais detalhes sobre o uso de cada um deve ser feito através da depuração do código fonte.
	
Todos os programas foram escritos a fim de demonstrar as caracterísitcas individuais de cada método envolvido, assim como as suas interpretações matemáticas. Portanto a qualidade da engenharia de software empregada não é um ponto de destaque. Dessa forma, cada programa tem como finalidade educacional e se comporta de forma independente dos demais. O seu uso em aplicações de alto risco e missão crítica não é recomendado.

Não há intenções por parte do desenvolvedor na manutenção deste repositório nem atualizações referentes a implementações de novos métodos/funcionalidades.
No entanto, você é livre para utilizá-lo e prosseguir em seu desenvolvimento de acordo com as normas BY-NC-SA - Creative Commons License. 

