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

#----------------------------------MATRIZ----------------------------------#

#Soma:
def soma():
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("MATRIZ - SOMA")
   print("")
   print("Matriz A:")
   print("")

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

   print("")
   print("Matriz B:")
   print("")

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

   if x == z and y == w:
      C = []
      for i in range(linhaA):
         C_linha = []
         for j in range(colunaA):
            C_linha.append(A[i][j] + B[i][j])
         C.append(C_linha)

      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print("MATRIZ - SOMA")
      print("")
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
      time.sleep(5)
      print("")
      selecao = input("Deseja fazer outro cálculo?: S - Sim | N - Não: ")
      if selecao == "S":
         soma()
      if selecao == "N":
        menu()

   else:
      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print("MATRIZ - SOMA")
      print("")
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
      time.sleep(5)
      print("")
      selecao = input("Deseja realizar outro cálculo?: S - Sim | N - Não: ")
      if selecao == "S":
        soma()
      if selecao == "N":
        menu()

#Subtração:       
def subtracao():
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("MATRIZ - SUBTRAÇÃO")
   print("")
   print("Matriz A:")
   print("")

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

   print("")
   print("Matriz B:")
   print("")

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

   if x == z and y == w:
      C = []
      for i in range(linhaA):
         C_linha = []
         for j in range(colunaA):
            C_linha.append(A[i][j] - B[i][j])
         C.append(C_linha)

      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print("MATRIZ - SUBTRAÇÃO")
      print("")
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
      time.sleep(5)
      print("")
      selecao = input("Deseja fazer outro cálculo?: S - Sim | N - Não: ")
      if selecao == "S":
        subtracao()
      if selecao == "N":
        menu()

   else:
      limpar_tela()
      print("PAZZI, La Calculadora Magica")
      print("")
      print("MATRIZ - SUBTRAÇÃO")
      print("")
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
      time.sleep(5)
      print("")
      selecao = input("Deseja realizar outro cálculo?: S - Sim | N - Não: ")
      if selecao == "S":
        subtracao()
      if selecao == "N":
        menu()

#----------------------------------MENUS----------------------------------#

#Seleção de Matriz:
def MATRIZ():
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("Carregando...")
   time.sleep(0)
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

#Seleção de Sistema Linear:
def LINEAR():
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   print("Carregando...")
   time.sleep(0)
   limpar_tela()
   print("PAZZI, La Calculadora Magica")
   print("")
   selecaoLINEAR = input("Digite a quantidade de incognitas a serem calculados:")

#Início:
def menu():
    limpar_tela()
    print("Carregando...")
    time.sleep(0)
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

menu()
