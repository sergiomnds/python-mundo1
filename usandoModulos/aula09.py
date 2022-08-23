frase = 'Curso em Vídeo Python'
###? Python vai colocar cada caractere em um espaço de 0 a 20 que pode ser acessado depois
#? C u r s o   e m   V  í  d  e  o    P  y  t  h  o  n
#? 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

#! Fatiamento
a = frase[9] #* Saída: V. Pega o caractere 9.
b = frase[9:13] #* Saída: Víde. NÃO PEGA O ULTIMO VALOR, nesse caso 'o'.
c = frase[9:21] #* Saída: Vídeo Python. Passa em 1 o tamanho dá string, mas não traz erro.
d = frase[9:21:2] #* Saída: VdoPto. Imprime o 1º e depois pula de 2 em 2 para imprimir e imprime o 2º.
e = frase[:5] #* Saída: Curso. Quando usa :5 começa o caractere 0 "até" o valor 5. Vai de 0 a 4.
f = frase[15:] #* Saída: Python. Começa no caractere 15 e vai até o final, seja qual for e imprimirá tudo.
g = frase[9::3] #* Saída: VePh. Começa do 9 e vai até o final, mas nesse caso pulará de 3 e 3 e imprime o 3º.
print('FATIAMENTO \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n'.format(a, b, c, d, e, f, g))

#! Análise
h = len(frase) #* length da string. Saída: 21
i = frase.count('o') #* Conta a qnt. de 'o' na string. Saída: 3
#! Count diferencia minúsculo de maiúsculo.
j = frase.count('o', 0, 13) #* Do caractere 0 a 13(sem incluir o 13) conta a qnt. de 'o'. Saída: 1
k = frase.find('deo') #* Mostra onde ele encontrou 'deo'. Saída: 11, pq é onde o caractere começa.
l = frase.find('android') #* Tem como Saída: -1, porque não encontra na string.
m = 'Curso' in frase #* É boolean, se tiver retorna True e se não False. Saída: True
print('ANÁLISE \n', h, i, j, k, l, m, '\n')

#! Transformação
n = frase.replace('Python', 'Android') #* Faz a substituição, mas não direto na String. Saída: Curso em Vídeo Android
#? Como a string é imutável, precisa fazer a atribuição: frase = frase.replace('Python', 'Android') para substituir mesmo a String.
o = frase.upper() #* Joga toda a String para maiúscula. Saída: CURSO EM VÍDEO PYTHON
p = frase.lower() #* Joga toda a String para minúsculo. Saída: curso em vídeo python
q = frase.capitalize() #* Toda string em minúsculo menos o 1º caractere. Saída: Curso em vídeo python
r = frase.title() #* Cada palavra da string com a 1º letra em maiúsculo. Saída: Curso Em Vídeo Python

frase2 = '   Aprenda Python  '
s = frase2.strip() #* Remove os espaços vazios no começo e no fim da string. Saída: 'Aprenda Python'
t = frase2.rstrip() #* Remove apenas o espaço do fim (direita) da string, r de right. Saída: '   Aprenda Python'
u = frase2.lstrip() #* Remove apenas o espaço do começo (esquerda) da string, l de left. Saída: 'Aprenda Python  '
print('TRANSFORMAÇÃO \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n{} \n'.format(n, o, p, q, r, s, t, u))

#! Divisão
print('DIVISÃO')
v = frase.split() #*Separa as palavras pelos em espaços em branco. Cada uma vira uma string separada e são agrupadas como lista. Saída: ['Curso', 'em', 'Vídeo', 'Python']
#? Posso printar só algum item da lista, assim como também só algum caractere:
print(v[2]) #* Saída: Vídeo
print(v[2][3]) #* Saída: e
w = '-'.join(v) #*Junta as palavras separadas por espaço em branco com '-' no lugar. Saída: Curso-em-Vídeo-Python
print('{} \n{} \n'.format(v, w))

#! Frases Longas
print('FRASES LONGAS')
#? Usa da aspas triplas ###
print("""Lorem ipsum dolor sit amet. 
Ea facilis minima sed exercitationem pariatur eos necessitatibus corporis ex distinctio tempora! 
Rem provident galisum qui quia eaque et ipsam eligendi. \n""")

#! Mistura de métodos
print('MÉTODOS MISTURADOS')
print(frase.upper().count('O')) #* Saída: 3
print(frase.lower().find('vídeo')) #* Saída: 9, onde a começa.
