<img width="1254" height="1254" alt="PAZZI logo" src="https://github.com/user-attachments/assets/91dd4e7e-8aea-475e-a2d5-6e45dd796ffc" />


## PAZZI, La Calculadora Magica

> Primeiro projeto de programação da dupla — Engenharia de Controle e Automação, FESA (2º semestre 2026)

## Sobre o projeto

Calculadora de matrizes e sistemas lineares feita **100% em Python puro**, sem NumPy nem qualquer lib de álgebra linear. Todos os algoritmos — soma, subtração, multiplicação, inversa (Gauss-Jordan) e resolução de sistemas `Ax = b` — foram implementados na mão, com listas aninhadas.

O objetivo do projeto é justamente esse: entender o que tá acontecendo por trás das contas, não só chamar uma função pronta.

Atualmente a calculadora roda via terminal (CLI), mas o plano é evoluir para uma **interface gráfica (GUI)**. O projeto serve tanto como entrega da disciplina quanto como peça de **portfólio** da dupla.

### Por que "PAZZI"?

O nome é uma homenagem ao professor **Fernando Pizzo**, de Álgebra Linear do 1º semestre — a disciplina que deu a base matemática pra esse projeto existir.

## Funcionalidades

**Matrizes**
- Soma
- Subtração
- Multiplicação
- Inversa (Eliminação de Gauss-Jordan)

**Sistema Linear**
- Resolução por meio de `A⁻¹*x = b`.

**Outros**
- Créditos dos autores
- Links (LinkedIn, GitHub, Instituição, Trailer)

## Como rodar

```bash
python pazzi.py
```

Só precisa de Python 3. Nenhuma dependência externa (`os`, `platform`, `time` e `webbrowser` são todas built-in).

## Estrutura do menu

```
1 - Matriz
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Inversa
2 - Sistema Linear
3 - Outros
```

## Status do projeto

Este é o **primeiro projeto de programação da dupla**, feito para a disciplina de Eletricidade Aplicada. Ainda em ajuste.

## Autores

- Felipe Gabriel Macedo
- Arthur Américo

**Engenharia de Controle e Automação — 2º Semestre 2026**
**Faculdade Engenheiro Salvador Arena (FESA)**

## Licença

Projeto acadêmico, feito para fins de estudo e avaliação da disciplina.
