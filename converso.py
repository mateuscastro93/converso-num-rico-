num = int(input('Digite um número :'))
print('''Escolha umas das bases para conversão 
 [1] para BINÁRIO
 [2] para OCTAL
 [3] para HEXADECIMAL     
      ''')
opção = int(input('Digite sua opção : '))

if   opção == 1:
    print(f'Convertido BINÁRIO é igual á {bin(num)[2:]}')
elif opção == 2:
    print(f'Convertido OCTAL é igual á {oct(num)[2:]}')
elif opção == 3:
     print(f'Convertido HEXADECIMAL é igual á {hex(num)[2:]}')
else:
    print('Opção inválida . Tente novamente')
