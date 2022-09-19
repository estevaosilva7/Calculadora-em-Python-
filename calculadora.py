print('  Calculadora em Python')
print('Digite um número por favor: ')
numero1 = int(input())
print('Digite uns dos operadores a seguir: ', '+, -, * ou /')
operador = input()
print('Digite o segundo número do cálculo: ')
numero2 = int(input())

if operador == '+':
    resultado = numero1 + numero2
    print('O resultado da Soma é:',resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print('O resultado da Divisão é:',resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print('O resultado da Multiplicação é:',resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print('O resultado da Divisão é:',resultado)
else:
    print('  OPERADOR INCORRETO \n(MAIS ATENÇÃO POR FAVOR)')
