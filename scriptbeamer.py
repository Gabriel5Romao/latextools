#coding: utf-8
'''
Algoritmo para criação de um slide em beamer,
com auxílio de imagens via tikz.

Acho que o interessante aqui é armazenar os slides numa lista
'''
import os

def menu():
    print('Criação de Slides em beamer.')
    print('Digite a opção desejada:')
    print('0 - sair')
    print('1 - Slide de Título')
    print('2 - Criar um slide')

def slide_titulo():
    a = input('Título do slide: \n')
    b = input('Autor: \n')
    c = input('Data: \n')
    d = input('Instituição:\n')

    lista_slides.append(f'\\title{{{a}}} \n\\author{{{b}}} \n\\date{{{c}}} \n\\institute{{{d}}} \n')
    lista_slides.append('\\begin{document} \n')
    lista_slides.append('\\begin{frame} \n')
    lista_slides.append('\\maketitle \n')
    lista_slides.append('\\end{frame} \n')

def criar_bloco():
    titulo_bloco = input('Digite o título do bloco')
    lista_slides.append(f'\\begin{{block}}{{{titulo_bloco}}}')
    texto = input('Digite o texto do bloco \n')
    lista_slides.append(texto) 
    lista_slides.append('\\end{block} \n')


def criar_slide():
    titulo_slide = input('Digite o título do slide: \n')
    lista_slides.append(f'\\begin{{frame}} \n\\frametitle{{{titulo_slide}}}\n')
    escolha = input('Deseja adicionar um bloco nesse slide? \n( S / N )\n')

    if escolha.upper() == 'S':
       criar_bloco()
    texto = input('Digite o texto do slide')
    lista_slides.append(texto)



lista_slides = ['\\documentclass{beamer} \n\\usepackage[utf8]{inputenc} \n']

saida = True

while saida:
    menu()
    opcao = int(input(''))
    
    if opcao == 0:
        saida = False
    elif opcao == 1:
        slide_titulo()
    elif opcao == 2:
        criar_slide()
        while True:
            opcao = input('Deseja adicionar outro bloco nesse slide?\n( S / N) \n')
            if opcao.upper() == 'N':
                break
            else:
                criar_bloco()
    
    os.system('cls')

                
lista_slides.append('\\end{document} \n')

tamanho = len(lista_slides)

with open('teste.tex','w', encoding = 'utf8') as arquivo:
    for i in range(0,tamanho):
        arquivo.write(lista_slides[i])






