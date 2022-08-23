n = input('Digite algo: ')
print(type(n))

if(n.isnumeric()):
    print('{} é um número'.format(n))
else:
    print('{} não é um número'.format(n))

if(n.isalpha()):
    print('{} é(são) apenas letra(s)'.format(n))
else:
    print('{} não é(são) apenas letra(s)'.format(n))

if(n.isalnum()):
    print('{} é(são) alphanumérico(s)'.format(n))
else:
    print('{} não é(são) alphanumérico(s)'.format(n))

if(n.isupper()):
    print('{} é todo em maiúsculo'.format(n))
else:
    print('{} não é todo em maiúsculo'.format(n))

if(n.islower()):
    print('{} é todo em minúsculo'.format(n))
else:
    print('{} não é todo em minúsculo'.format(n))
