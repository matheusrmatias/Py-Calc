from math import sqrt
from operator import le
from tkinter import *

buttoncolor='#F2AE30'
operationcolor='#593E25'
numcolor='#FFFFFF'
displaycolor = '#F2C12E'

def calcular(operacao):
    operadores = ['+','-','×','÷',',','^']
    operacao=operacao.replace(',','.')
    try:
        if '+' in operacao:
            inicioconta=float(operacao[0:operacao.index('+')])
            fimconta=float(operacao[operacao.index('+')+1:len(operacao)])
            operacao = str(inicioconta+fimconta)
            operacao = operacao.replace('.',',')
            tela['text']=operacao
        elif '×' in operacao:
            inicioconta=float(operacao[0:operacao.index('×')])
            fimconta=float(operacao[operacao.index('×')+1:len(operacao)])
            operacao = str(inicioconta*fimconta)
            operacao = operacao.replace('.',',')
            tela['text']=operacao
        elif '÷' in operacao:
            inicioconta=float(operacao[0:operacao.index('÷')])
            fimconta=float(operacao[operacao.index('÷')+1:len(operacao)])
            operacao = str(inicioconta/fimconta)
            operacao = operacao.replace('.',',')
            tela['text']=operacao
        elif '^' in operacao:
            inicioconta=float(operacao[0:operacao.index('^')])
            fimconta=float(operacao[operacao.index('^')+1:len(operacao)])
            operacao = str(inicioconta**fimconta)
            operacao = operacao.replace('.',',')
            tela['text']=operacao
        elif '-' in operacao:
            if operacao[0]=='-':
                inicioconta=float(operacao[1:operacao[1:len(operacao)-1].index('-')])
                fimconta=float(operacao[operacao[1:len(operacao)-1].index('-')+1:len(operacao)])
                operacao = str(-inicioconta+fimconta)
                operacao = operacao.replace('.',',')
                tela['text']=operacao
            else:
                inicioconta=float(operacao[0:operacao.index('-')])
                fimconta=float(operacao[operacao.index('-')+1:len(operacao)])
                operacao = str(inicioconta-fimconta)
                operacao = operacao.replace('.',',')
                tela['text']=operacao
    except:
        tela['text']='Syntax Error'

def adicionar(evt):
    operadores = ['+','-','×','÷','^']
    if evt == '«':
        if len(tela['text']) == 1:
            tela['text']='0'
        else:
            tela['text'] = tela['text'][:-1]

    elif evt == 'C' or evt == 'c':
        tela['text']='0'
    else:
        if tela['text'] == '0' and not(evt in operadores):
            tela['text']=str(evt)
        elif len(tela['text'])==34:
            None
        elif evt in operadores:
            if '+' in tela['text'] or '-' in tela['text'] or '×' in tela['text'] or '÷' in tela['text'] or '^' in tela['text'] or '√' in tela['text']:
                if tela['text'][len(tela['text']) - 1] == '+' or tela['text'][len(tela['text']) - 1] == '-' or tela['text'][len(tela['text']) - 1] == '×' or tela['text'][len(tela['text']) - 1] == '÷' or tela['text'][len(tela['text']) - 1] == '^' or tela['text']=='Syntax Error':
                    None
                else:
                    calcular(tela['text'])
                    tela['text']+=str(evt)
                    
            else:
                tela['text']+=str(evt)

        else:
            if '√' in tela['text'] and evt=='√' or len(tela['text'])!=0 and evt=='√':
                None
            else:
                tela['text']+=str(evt)

janela = Tk()

janela.title('Calculadora')
janela.geometry('260x400')
janela.maxsize(260,400)
janela.minsize(260,400)

janela.configure(bg='#F2C12E')

tela=Label(janela, font=('arial',20,'bold'), bg=displaycolor, fg=numcolor, text='0', wraplength=260)
tela.place(width=260, height=100)

n0=Button(janela, text='0', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n0['text']))
n0.place(width=60,height=60,y=340,x=0)

n1=Button(janela, text='1', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n1['text']))
n1.place(width=60,height=60,y=280,x=0)

n2=Button(janela, text='2', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n2['text']))
n2.place(width=60,height=60,y=280,x=60)

n3=Button(janela, text='3', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n3['text']))
n3.place(width=60,height=60,y=280,x=120)

n4=Button(janela, text='4', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n4['text']))
n4.place(width=60,height=60,y=220,x=0)

n5=Button(janela, text='5', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n5['text']))
n5.place(width=60,height=60,y=220,x=60)

n6=Button(janela, text='6', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n6['text']))
n6.place(width=60,height=60,y=220,x=120)

n7=Button(janela, text='7', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n7['text']))
n7.place(width=60,height=60,y=160,x=0)

n8=Button(janela, text='8', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n8['text']))
n8.place(width=60,height=60,y=160,x=60)

n9=Button(janela, text='9', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(n9['text']))
n9.place(width=60,height=60,y=160,x=120)

ponto=Button(janela, text=',', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(ponto['text']))
ponto.place(width=60,height=60,y=340,x=60)

soma=Button(janela, text='+', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(soma['text']))
soma.place(width=80,height=60,y=280,x=180)

subtracao=Button(janela, text='-', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(subtracao['text']))
subtracao.place(width=80,height=60,y=220,x=180)

divisao=Button(janela, text='÷', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(divisao['text']))
divisao.place(width=80,height=60,y=100,x=180)

multiplicacao=Button(janela, text='×', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(multiplicacao['text']))
multiplicacao.place(width=80,height=60,y=160,x=180)

igual=Button(janela, text='=', font=('arial',40,'bold'), bg=buttoncolor, fg='#fff', command=lambda : calcular(tela['text']))
igual.place(width=80,height=60,y=340,x=180)

raiz=Button(janela, text='√', font=('arial',20,'bold'), bg=buttoncolor, fg='#fff', command=lambda : adicionar(raiz['text']))
raiz.place(width=60,height=60,y=100,x=60)

potencia=Button(janela, text='^', font=('arial',20,'bold'), bg=buttoncolor, fg='#fff', command=lambda : adicionar(potencia['text']))
potencia.place(width=60,height=60,y=100,x=120)


apagar=Button(janela, text='«', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=lambda : adicionar(apagar['text']))
apagar.place(width=60,height=60,y=340,x=120)

limpar=Button(janela, text='C', font=('arial',20,'bold'), bg=buttoncolor, fg='red', command=lambda : adicionar(limpar['text']))
limpar.place(width=60,height=60,y=100,x=0)

janela.bind('<Key-minus>', lambda evt: adicionar('-'))
janela.bind('<Key-+>', lambda evt: adicionar('+'))
janela.bind('<Key-x>', lambda evt: adicionar('×'))
janela.bind('<Key-*>', lambda evt: adicionar('×'))
janela.bind('<Key-^>', lambda evt: adicionar('^'))
janela.bind('<Key-/>', lambda evt: adicionar('÷'))
janela.bind('<Key-,>', lambda evt: adicionar(','))

janela.bind('<Key-BackSpace>', lambda evt: adicionar('«'))
janela.bind('<Key-C>', lambda evt: adicionar('c'))
janela.bind('<Key-c>', lambda evt: adicionar('C'))
janela.bind('<Key-9>', lambda evt: adicionar('9'))
janela.bind('<Key-8>', lambda evt: adicionar('8'))
janela.bind('<Key-7>', lambda evt: adicionar('7'))
janela.bind('<Key-6>', lambda evt: adicionar('6'))
janela.bind('<Key-5>', lambda evt: adicionar('5'))
janela.bind('<Key-4>', lambda evt: adicionar('4'))
janela.bind('<Key-3>', lambda evt: adicionar('3'))
janela.bind('<Key-2>', lambda evt: adicionar('2'))
janela.bind('<Key-1>', lambda evt: adicionar('1'))
janela.bind('<Key-0>', lambda evt: adicionar('0'))
janela.bind('<Key-Return>', lambda evt: calcular(tela['text']))
janela.bind('<Key-Delete>', lambda evt: adicionar('C'))

janela.mainloop()