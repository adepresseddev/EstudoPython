# EstudoPython

*VARIÁVEL*


----------------------------------------------------------------------------------------------------------

Não é precisa adcionar o prefixo do tipo de variável a ser criado.

Exemplo:

Caso quero um valor:

  int:
  
      idade = 18
  
  string:

    idade = 'Thiago'
  
  float:

    dinheiro = 10.56
  
E assim vai com qualquer tipo de variável.

----------------------------------------------------------------------------------------------------------

*INPUT*

  Dentro da variável podemos também pedir para o usuário digitar os dados usando o comando *INPUT*

   Exemplo:

      nome = input('Digite seu nome!!')
      
      idade = input('Digite sua idade!!')
      
 
----------------------------------------------------------------------------------------------------------

*PRINT*

  O *PRINT* é utilizado para mostrar informações dentro do terminal, poder ser tanto valor inteiros, quanto variáveis.
  
  Exemplo:
  
    print(idade)
    
    print(nome)
    
*.FORMAT*

  O *.FORMAT* é utilizado para quando se quer apresentar as variáveis dentro de um tempo na hora do PRINT.
  
   Exemplo: 
    
      nome = 'Thiago'
      
      idade = 78
      
      print('Nome: {}, Idade: {} '.format(nome, idade))
     
     
  As variáveis dentro do *FORMAT* devem ser apresentados dentro da ordem escrita que você deseja.

----------------------------------------------------------------------------------------------------------

OPERADORES MATEMÁTICOS

  + = Adição
  
  - = Subtração
  
  / = Divisão
  
  * = Multiplicação
  
  ** = Potência
  
  % = Resto da Divisão*
  
  *: Geralmemte bastante utilizado para saber se um número é ímpar ou par.
  
  Exemplos:
  
   Exemplo *ADIÇÃO*:
      
      num1 = 10
      num2 = 30
      
      resultado = num1 + num2
      print(resultado)
      
   Exemplo *SUBTRAÇÃO*:
    
      num1 = 52
      num2 = 49
      
      resultado = num1 - num2
      print(resultado)
      
   Exemplo *DIVISÃO*:
    
      num1 = 75
      num2 = 36
    
      resultado = num1 / num2
      print(resultado)
    
   Exemplo *MULTIPLICAÇÃO*:
    
      num1 = 45
      num2 = 92
      
      resultado = num1 * num2
      print(resultado)
      
   Exemplo *POTÊNCIA*:
    
      num1 = 23
      
      resultado = num1**2
      print(resultado)
      
   Exemplo *RESTO DA DIVSÃO*:
    
      num1 = 15
      num2 = 6
      
      resultado = num1 % num2
      print(resultado)
      
----------------------------------------------------------------------------------------------------------
      
*OPERADORES LÓGICOS*

  *IF*
    
   Usando quando se quer verificar um dado de uma variável, como se ela é verdadeira ou falsa, ou se ela é maior que 10.
    
   Exemplo:
    
      num = 10 
      
      if num >= 6:
        print('Seu número é maior que 6')
        
      else:
        print('Seu número é menor que 6')
        
        
   *AND E OR*
    
   Condições utilizadas para adicionar mais fatores na verificação das variáveis.
      
   Exemplo:
      
      num = 10
      
      if num >= 0 or num <= 20:
        print('Seu número está entre 0 e 20!')
        
      else:
        print('Seu número não está entre 0 e 20!')
        
        
   Exemplo:
   
      num = input('Digite um número!!')
      
      if num >= 10 and num <= 30
        print('Seu número está entre 10 e 30!')
        
      else:
        print('Seu número não está entre 10 e 30!')
        
        
