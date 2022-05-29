
from random import randint # --> Importando módulo
from turtle import back 

numero = str(randint(100000000, 999999999)) # --> Gerando números aleatórios
cpf = numero # --> Nove primeiros dígitos gerados
cpf_backup = cpf # --> Armazenando o valor do CPF inserido para ser utilizado na verificação
cpf = cpf.replace('.', '') # --> Removendo as pontuações
cpf = cpf.replace('-', '') # --> Removendo as pontuações
cpf = cpf[0:9] # --> Fatiando os nove primeiros dígitos já sem as pontuações

multiplicador = 10 # --> Será utilizado para multiplicar os números do CPF
soma = 0 # --> Soma total que será aplicada na fórmula: 11 - (soma % 11)

for n in cpf: # --> Multiplicação e soma do primeiro dígito
    n = int(n)
    soma += n * multiplicador
    multiplicador -= 1
digit_1 = 11 - (soma % 11) # --> Primeiro dígito

if digit_1 > 9: # --> Transformando o número em "0" caso ele seja maior que 9
    digit_1 = 0
cpf += str(digit_1) # --> Inserção do primeiro dígito para ser iterado no próximo laço

multiplicador = 11 # --> Defindo para onze para calcular o segundo dígito do CPF
soma = 0 

for n in cpf: # --> Multiplicação e soma do segundo dígito
    n = int(n)
    soma += n * multiplicador
    multiplicador -= 1
digit_2 = 11 - (soma % 11) # Segundo dígito

# --> Fazendo a junção dos dígitos 
novo_cpf = cpf_backup[0:3] + '.' + cpf_backup[3:6] + '.' + cpf_backup[6:9] + '-' + str(digit_1) + str(digit_2)

print(novo_cpf) # --> Retornará o CPF gerado.