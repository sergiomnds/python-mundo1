nome = str(input('Qual seu nome? '))

if nome == 'Sérgio':
    print('Que nome lindo!')
else:
    print('Nome sem graça!')

print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! :((((')