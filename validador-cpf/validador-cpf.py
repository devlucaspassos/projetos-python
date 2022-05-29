# xxx.xxx.xxx-xx

# 1º digito / 2º digito

# x * 10 / # x * 11
# x * 9 / # x * 10
# x * 8 / # x * 9
# x * 7 / # x * 8
# x * 6 / # x * 7
# x * 5 / # x * 6
# x * 4 / # x * 5
# x * 3 / # x * 4
# x * 2 / # x * 3
#         # x * 2 --> primeiro dígito.

# Primeiro digito: 11 - (soma dos valores multiplicados % 11) = x 
# se x > 9 o primeiro digito é igual a 0. o primeiro digito será adicionado na próxima multiplicação.
# Primeiro digito: 11 - (soma dos valores multiplicados % 11) = x 

from statistics import multimode

while True:
    cpf = input('Digite seu CPF completo: ')
    cpf_backup = cpf # --> Armazenando o valor do CPF inserido antes de tirar as pontuações.
    cpf = cpf.replace('.', '') # --> Removendo as pontuações
    cpf = cpf.replace('-', '') # --> 
    cpf = cpf[0:9]

    multiplicador = 10
    soma = 0

    for n in cpf: # --> multiplicação e soma do primeiro dígito
        n = int(n)
        soma += n * multiplicador
        multiplicador -= 1
    digit_1 = 11 - (soma % 11) # --> Primeiro dígito

    if digit_1 > 9: # --> Transformando o número em "0" caso ele seja maior que 9.
        digit_1 = 0
    cpf += str(digit_1) # --> Inserção do primeiro dígito para ser iterado no próximo laço.

    multiplicador = 11
    soma = 0 
    
    for n in cpf: # --> multiplicação e soma do segundo dígito
        n = int(n)
        soma += n * multiplicador
        multiplicador -= 1
    digit_2 = 11 - (soma % 11) # Segundo dígito

    # --> Fazendo a junção dos dígitos 
    novo_cpf = cpf_backup[:12] + str(digit_1) + str(digit_2)

    if novo_cpf == cpf_backup: # --> Validando o CPF
        print('Válido.')
    else:
        print('Inválido.')