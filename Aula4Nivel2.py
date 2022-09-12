print('OLÁ SEJA BEM VINDO!!!')

nome = input('Digite seu nome!')

nota1 = float(input('Olá {}, digite sua primeira nota:'.format(nome)))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))

mediaTotal = (nota1 + nota2 + nota3) / 3

if mediaTotal >= 7:
    print('PARABÉNS {}!!! Você foi aprovado!, MÉDIA: {}'.format(nome, mediaTotal))
else:
    if mediaTotal >= 5.1 or mediaTotal <= 6.9:
        print('Sinto muito {}, Você está de recuperação, MÉDIA: {}!'.format(nome, mediaTotal))
    else:
        print('Sinto Muito, {}, você está reprovado, MÉDIA: {}'.format(nome, mediaTotal))
