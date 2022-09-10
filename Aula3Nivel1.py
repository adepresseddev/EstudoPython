kmperco = int(input('Digite a quantidade de kms percorridos??'))
gasgasto = float(input('Digite a quantidade de gasolina gasta??'))

resultado = kmperco / gasgasto
print('Kilometros percorridos: {} km, Gasolina gasta: {} l, Resultado: {} km/l'
      .format(kmperco, gasgasto, resultado))