from sys import displayhook
from tkinter import *

buttoncolor='#F2AE30'
operationcolor='#593E25'
numcolor='#FFFFFF'
displaycolor = '#F2C12E'

def apagando():
    if tela['text']=='0':
        None
    else:
        tstr=tela['text']
        tstr2=str()
        for i in range(len(tstr)-1):
            tstr2+=tstr[i]
        if len(tstr2)<1:
            tela['text']='0'
        else:
            tela['text']=tstr2
def apagandob(evt):
    if tela['text']=='0':
        None
    else:
        tstr=tela['text']
        tstr2=str()
        for i in range(len(tstr)-1):
            tstr2+=tstr[i]
        if len(tstr2)<1:
            tela['text']='0'
        else:
            tela['text']=tstr2

def clear():
    tela['text']='0'
def clearb(evt):
    tela['text']='0'

def num1():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='1'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='1'
def num1b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='1'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='1'

def num2():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='2'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='2'
def num2b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='2'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='2'

def num3():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='3'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='3'
def num3b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='3'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='3'

def num4():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='4'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='4'
def num4b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='4'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='4'

def num5():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='5'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='5'
def num5b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='5'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='5'

def num6():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='6'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='6'
def num6b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='6'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='6'

def num7():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='1'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='7'
def num7b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='1'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='7'

def num8():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='8'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='8'
def num8b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='8'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='8'

def num9():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='9'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='9'
def num9b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='9'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='9'

def num0():
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='0'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='0'
def num0b(evt):
    if tela['text']=='0' or tela['text']=='Indefinido':
        tela['text']='0'
    elif len(tela['text'])==15:
        None
    elif tela['text']!='0':
        tela['text']+='0'

def soma():
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='+'
def somab(evt):
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='+'

def subt():
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='-'
def subtb(evt):
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='-'

def multi():
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='*'
def multib(evt):
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='*'

def divi():
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='/'
def divib(evt):
    if  '*' in tela['text']:
        None
    elif  '/' in tela['text']:
        None
    elif  '+' in tela['text']:
        None
    elif  '-' in tela['text']:
        None
    elif tela['text']=='Indefinido':
        None
    elif len(tela['text'])==15:
        None
    else:
        tela['text']+='/'

def igual():
    if '+' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('+')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('+')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1+termo2
            tela['text']=str(resultado)
            cont=1
            return cont
        except ValueError:
            None

    elif '-' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('-')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('-')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1-termo2
            tela['text']=str(resultado)
        except ValueError:
            None

    elif '*' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('*')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('*')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1*termo2
            tela['text']=str(resultado)
        except ValueError:
            None

    elif '/' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('/')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('/')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            if termo2!=0:
                resultado=termo1/termo2
                tela['text']=str(f'{resultado:.0f}')
            else:
                tela['text']='Indefinido'
        except ValueError:
            None
    else:
        None
def igualb(evt):
    if '+' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('+')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('+')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1+termo2
            tela['text']=str(resultado)
            cont=1
            return cont
        except ValueError:
            None

    elif '-' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('-')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('-')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1-termo2
            tela['text']=str(resultado)
        except ValueError:
            None

    elif '*' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('*')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('*')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            resultado=termo1*termo2
            tela['text']=str(resultado)
        except ValueError:
            None

    elif '/' in tela['text']:
        tstr=tela['text']
        tstr2=''
        for i in range(tstr.find('/')):
            tstr2+=tstr[i]
        try:
            termo1=int(tstr2)
            tstr2=''
            for i in range(tstr.find('/')+1,len(tstr)):
                tstr2+=tstr[i]
            termo2=int(tstr2)
            if termo2!=0:
                resultado=termo1/termo2
                tela['text']=str(f'{resultado:.0f}')
            else:
                tela['text']='Indefinido'
        except ValueError:
            None
    else:
        None

interface=Tk()

interface.iconbitmap('Content/Imagens/calculadora.ico')
interface.title('Calculadora')
interface.geometry('260x400')
interface.maxsize(260,400)
interface.minsize(260,400)

nigual=Button(interface, text='=', font=('arial',40,'bold'), bg=buttoncolor, fg='#fff', command=igual)
nigual.place(width=200,height=60,y=340,x=0)

n0=Button(interface, text='0', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num0)
n0.place(width=60,height=60,y=340,x=200)

n1=Button(interface, text='1', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num1)
n1.place(width=60,height=60,y=280,x=200)

n2=Button(interface, text='2', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num2)
n2.place(width=60,height=60,y=280,x=140)

n3=Button(interface, text='3', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num3)
n3.place(width=60,height=60,y=280,x=80)

n4=Button(interface, text='4', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num4)
n4.place(width=60,height=60,y=220,x=80)

n5=Button(interface, text='5', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num5)
n5.place(width=60,height=60,y=220,x=140)

n6=Button(interface, text='6', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num6)
n6.place(width=60,height=60,y=220,x=200)

n7=Button(interface, text='7', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num7)
n7.place(width=60,height=60,y=160,x=80)

n8=Button(interface, text='8', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num8)
n8.place(width=60,height=60,y=160,x=140)

n9=Button(interface, text='9', font=('arial',20,'bold'), bg=buttoncolor, fg=numcolor, command=num9)
n9.place(width=60,height=60,y=160,x=200)

nmais=Button(interface, text='+', font=('arial',20,'bold'), bg=buttoncolor, fg=operationcolor,command=soma)
nmais.place(width=80,height=60,y=280,x=0)

nmenos=Button(interface, text='-', font=('arial',20,'bold'), bg=buttoncolor, fg=operationcolor, command=subt)
nmenos.place(width=80,height=60,y=220,x=0)

nmulti=Button(interface, text='x', font=('arial',20,'bold'), bg=buttoncolor, fg=operationcolor, command=multi)
nmulti.place(width=80,height=60,y=160,x=0)

ndiv=Button(interface, text='÷', font=('arial',20,'bold'), bg=buttoncolor, fg=operationcolor, command=divi)
ndiv.place(width=80,height=60,y=100,x=0)

nlimp=Button(interface, text='C', font=('arial',40,'bold'), bg=buttoncolor, fg='#f00', command=clear)
nlimp.place(width=120,height=60,y=100,x=80)

napaga=Button(interface, text='←', font=('arial',40,'bold'), bg=buttoncolor, fg=operationcolor, command=apagando)
napaga.place(width=60,height=60,y=100,x=200)

tela=Label(interface, font=('arial',20,'bold'), bg=displaycolor, fg=numcolor, text='0', wraplength=260)
tela.place(width=260, height=100)

interface.bind('<Key-0>', num0b)
interface.bind('<Key-1>', num1b)
interface.bind('<Key-2>', num2b)
interface.bind('<Key-3>', num3b)
interface.bind('<Key-4>', num4b)
interface.bind('<Key-5>', num5b)
interface.bind('<Key-6>', num6b)
interface.bind('<Key-7>', num7b)
interface.bind('<Key-8>', num8b)
interface.bind('<Key-9>', num9b)
interface.bind('<Key-+>', somab)
interface.bind('<Key-minus>', subtb)
interface.bind('<Key-/>', divib)
interface.bind('<Key-*>', multib)
interface.bind('<Key-=>', igualb)
interface.bind('<Key-BackSpace>', apagandob)
interface.bind('<Key-c>', clearb)
interface.bind('<Key-C>', clearb)
interface.bind('<Key-x>', multib)
interface.bind('<Key-X>', multib)
interface.bind('<Key-Delete>', clearb)
interface.bind('<Return>', igualb)

interface.mainloop()