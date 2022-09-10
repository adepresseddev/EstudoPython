print('SEJA BEM VINDO À CALCULADORA DE IMC!!')

nome = input('Digite seu nome!')
altura = float(input('Olá {}, Digite sua altura em metros!'.format(nome)))
peso = float(input('Digite seu peso!'))

resultadoImc = altura**2
resultadoImc = peso / resultadoImc

print('Olá {}, seu peso é: {} kg; sua altura é: {} m; Seu IMC é: {}'.format(nome, peso, altura, resultadoImc.__round__(2)))