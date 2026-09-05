# Bilbiotecas para obter a opção de limpar tela:
import os
import platform

# Função de limpar tela:
def limpar_tela():
  if platform.system() == 'Windows':
    os.system('cls')
  else:
    os.system('clear')

#Bilbioteca para obter a opção de timer:
import time

#Biblioteca para abrir links externos:
import webbrowser

#----------------------------------VARIÁVEIS----------------------------------#

global ultima_funcao

#----------------------------------FUNÇÕES GENÉRICAS----------------------------------#

def MatrizA():
   A = []
   linhaA = int(input("Insira o número de linhas: "))
   colunaA = int(input("Insira o número de colunas: "))
   print("")
   
   for x in range(linhaA):
      A_linha = []
      for y in range(colunaA):
         valorA = float(input(f"Digite o valor da posição A({x},{y}): "))
         A_linha.append(valorA)
      A.append(A_linha)
   return A, linhaA, colunaA

def MatrizB():
   B = []
   linhaB = int(input("Insira o número de linhas: "))
   colunaB = int(input("Insira o número de colunas: "))
   print("")
   
   for z in range(linhaB):
      B_linha = []
      for w in range(colunaB):
         valorB = float(input(f"Digite o valor da posição B({z},{w}): "))
         B_linha.append(valorB)
      B.append(B_linha)
   return B, linhaB, colunaB

def MatrizI(linhaA, colunaA):
   I = []
   linhaI = linhaA
   colunaI = colunaA
   for a in range(linhaI):
      I_linha = []
      for b in range(colunaI):
         if a == b:
            valorI = 1.0
         else:
            valorI = 0.0
         I_linha.append(valorI)
      I.append(I_linha)
   return I, linhaI, colunaI

class CABECALHO:
   def __init__(self, tipo):
      self.tipo = tipo

   def printar(self):
      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print(self.tipo)
      print("")

def OPCAO():
   global ultima_funcao
   time.sleep(5)
   print("")
   selecao = input("Deseja fazer outro cálculo?: S - Sim | N - Não: ")
   if selecao == "S":
      ultima_funcao()
   if selecao == "N":
      menu()
   else:
      print("OPÇÃO INCORRETA")
      time.sleep(2)
      menu()

#----------------------------------MATRIZ----------------------------------#

#Soma:
def soma():
   global ultima_funcao
   ultima_funcao = soma
   CABECALHO("MATRIZ - SOMA").printar()
   print("Matriz A:")
   print("")
   A, linhaA, colunaA = MatrizA()
   print("")
   print("Matriz B:")
   print("")
   B, linhaB, colunaB = MatrizB()

   if linhaA == linhaB and colunaA ==  colunaB:
      C = []
      for i in range(linhaA):
         C_linha = []
         for j in range(colunaA):
            C_linha.append(A[i][j] + B[i][j])
         C.append(C_linha)

      CABECALHO("MATRIZ - SOMA").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("+")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("C =")
      print(C)
      OPCAO()
      
   else:
      CABECALHO("MATRIZ - SOMA").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("+")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("NÃO É POSSÍVEL REALIZAR ESTE CÁLCULO")
      OPCAO()

#Subtração:       
def subtracao():
   global ultima_funcao
   CABECALHO("MATRIZ - SUBTRAÇÃO").printar()
   ultima_funcao = subtracao
   print("")
   print("Matriz A:")
   print("")
   A, linhaA, colunaA = MatrizA()
   print("")
   print("Matriz B:")
   print("")
   B, linhaB, colunaB = MatrizB()

   if linhaA == linhaB and colunaA ==  colunaB:
      C = []
      for i in range(linhaA):
         C_linha = []
         for j in range(colunaA):
            C_linha.append(A[i][j] - B[i][j])
         C.append(C_linha)

      CABECALHO("MATRIZ - SUBTRAÇÃO").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("-")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("C =")
      print(C)
      OPCAO()

   else:
      CABECALHO("MATRIZ - SUBTRAÇÃO").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("+")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("NÃO É POSSÍVEL REALIZAR ESTE CÁLCULO")
      OPCAO()

#Multiplicação:
def multiplicacao():
   global ultima_funcao
   CABECALHO("MATRIZ - MULTIPLICAÇÃO").printar()
   ultima_funcao = multiplicacao
   print("Matriz A:")
   print("")
   A, linhaA, colunaA = MatrizA()
   print("")
   print("Matriz B:")
   print("")
   B, linhaB, colunaB = MatrizB()

   if colunaA == linhaB:
      C = []
      for i in range(linhaA):
         C_linha = []
         for j in range(colunaB):
            soma = 0
            for k in range(colunaA):
               soma += (A[i][k] * B[k][j])
            C_linha.append(soma)
         C.append(C_linha)

      CABECALHO("MATRIZ - MULTIPLICAÇÃO").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("-")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("C =")
      print(C)
      OPCAO()

   else:
      CABECALHO("MATRIZ - MULTIPLICAÇÃO").printar()
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("+")
      print("")
      print("B =")
      print(B)
      print("")
      print("=")
      print("")
      print("NÃO É POSSÍVEL REALIZAR ESTE CÁLCULO")
      OPCAO()

#Inversa:
def inversa():
   global ultima_funcao
   CABECALHO("MATRIZ - INVERSA").printar()
   ultima_funcao = inversa
   print("Matriz A:")
   print("")
   A, linhaA, colunaA = MatrizA()
   I, linhaI, colunaI = MatrizI(linhaA, colunaA)

   if linhaA == colunaA:
      n = linhaA
      aumentada = []
      for i in range(n):
         aumentada.append(A[i] + I[i])

      for col in range(n):
         if aumentada[col][col] == 0:
            troca = None
            for linha in range(col + 1, n):
               if aumentada[linha][col] != 0:
                  troca = linha
                  break
            if troca is None:
               print("MATRIZ SINGULAR - NÃO POSSUI INVERSA")
               print("")
               OPCAO()
               return None
            aumentada[col], aumentada[troca] = aumentada[troca], aumentada[col]

         pivo = aumentada[col][col]
         for j in range(2 * n):
            aumentada[col][j] = aumentada[col][j] / pivo

         for i in range(n):
            if i != col:
               fator = aumentada[i][col]
               for j in range(2 * n):
                  aumentada[i][j] = aumentada[i][j] - fator * aumentada[col][j]

      C = []
      for i in range(n):
         C.append(aumentada[i][n:2*n])

      CABECALHO("MATRIZ - INVERSA").printar()
      print("")
      print("Resultado:")
      print("")
      print("A =")
      print(A)
      print("")
      print("=")
      print("")
      print("Inversa:")
      print(C)
      OPCAO()
   else:
      print("")
      print("MATRIZ NÃO É QUADRADA - NÃO POSSUI INVERSA")
      OPCAO()
 
#----------------------------------MENUS----------------------------------#

#Seleção de Matriz:
def MATRIZ():
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("Selecione tipo de calculo entre matrizes a ser feito:\n1 - Soma \n2 - Subtração\n3 - Multiplicação\n4 - Inversa")
   print("")
   selecaoMATRIZ = input("Seleção: ")

   if selecaoMATRIZ == "1":
      soma()

   if selecaoMATRIZ == "2":
      subtracao()

   if selecaoMATRIZ == "3":
      multiplicacao()

   if selecaoMATRIZ == "4":
      inversa()

   else:
      print("OPÇÃO INCORRETA")
      time.sleep(2)
      MATRIZ()

#Seleção de Sistema Linear:
def LINEAR():
   global ultima_funcao
   ultima_funcao = LINEAR
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   n = int(input("Digite a quantidade de incognitas a serem calculados: "))

   A = []
   for i in range(n):
      A_linha = []
      for j in range(n):
         valorA = float(input(f"Insira o valor da posição A({i},{j}): "))
         A_linha.append(valorA)
      A.append(A_linha)

   b = []
   print("")
   for i in range(n):
      valorB = float(input(f"Insira a constante do sistema em b({i}): "))
      b.append([valorB])

   aumentada = []
   for i in range(n):
      aumentada.append(A[i] + b[i])

   for col in range(n):
      if aumentada[col][col] == 0:
         troca = None
         for linha in range(col + 1, n):
            if aumentada[linha][col] != 0:
               troca = linha
               break
         if troca is None:
            print("SISTEMA IMPOSSÍVEL OU INDETERMINADO - SEM SOLUÇÃO ÚNICA")
            return None
         aumentada[col], aumentada[troca] = aumentada[troca], aumentada[col]

      pivo = aumentada[col][col]
      for j in range(n + 1):
         aumentada[col][j] = aumentada[col][j] / pivo

      for i in range(n):
         if i != col:
            fator = aumentada[i][col]
            for j in range(n + 1):
               aumentada[i][j] = aumentada[i][j] - fator * aumentada[col][j]

   VARIAVEL = []
   for i in range(n):
      VARIAVEL.append(aumentada[i][n])

   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("SISTEMA LINEAR")
   print("")
   print("Resultado:")
   print("")
   print(VARIAVEL)
   print("")
   OPCAO()

#Seleção de Outros:     
def OUTROS():
   while(True):
      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print("Criado por:\nFelipe Gabriel Macedo\nArthur Américo\n\nENGENHARIA DE CONTROLE AUTOMAÇÃO 2º Semestre 2026\n\nFaculdade Engenheiro Salvador Arena\n")
      time.sleep(5)
      selecaoOUTROS = input("Digite uma das opções abaixo:\n1 - Trailer (YOUTUBE)\n2 - Linkedlin: Felipe Gabriel Macedo\n3 - Instituição\n4 - GitHub\n\n")
      if selecaoOUTROS == "1":
        webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ") #NOTA: Como o trailer oficial ainda não foi criado, o link colocado é do clip da música de Rick Astley
      if selecaoOUTROS == "2":
        webbrowser.open_new("https://br.linkedin.com/in/felipegabrielmacedo") # Link do meu Linkedln
      if selecaoOUTROS == "3":
         webbrowser.open_new("https://faculdadesalvadorarena.org.br/sobre-a-faculdade/") # Site da nossa instituição
      if selecaoOUTROS == "4":
         webbrowser.open_new("https://github.com/felipegabriel6x/Pazzi-La-Calculadora-Magica") # Link do repertório do GitHub
       
#Início:
def menu():
    limpar_tela()
    print("PAZZI, La Calculadora Magica")
    print("")
    print("O que deseja calcular?\n1 - Matriz \n2 - Sistema Linear\n3 - Outros")
    print("")
    selecao = input("Digite o número para selecionar a opção desejada: ")

    if selecao == "1":
       MATRIZ()
    if selecao == "2":
       LINEAR()
    if selecao == "3":
       OUTROS()
    else:
       print("OPÇÃO INCORRETA")
       time.sleep(2)
       menu()

# ATIVADORES:
menu()