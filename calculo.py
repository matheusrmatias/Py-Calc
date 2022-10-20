def calcular(operacao):
    operadores = ['+','-','×','÷',',','^']
    operacao=operacao.replace(',','.')
    print(operacao)
    if '+' in operacao:
        inicioconta=float(operacao[0:operacao.index('+')])
        fimconta=float(operacao[operacao.index('+')+1:len(operacao)])
        operacao = inicioconta+fimconta