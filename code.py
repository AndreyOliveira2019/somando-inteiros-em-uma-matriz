#determine sua matriz:

x = [1,1,1],[1,1,1],[10,20,30]

#crie uma variável para receber a soma:
soma = 0

#for 1 para ler a matriz, for 2 para ler a matriz dentro da outra matriz:
for n in x:
  for n2 in n:
    
#execute a operação de soma:
    soma = soma + n2
print(soma)
