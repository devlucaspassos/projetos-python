# xxx.xxx.xxx-xx    ---> CPF
# 1º digito       2º digito

# x * 10           x * 11
# x * 9            x * 10
# x * 8            x * 9
# x * 7            x * 8
# x * 6            x * 7
# x * 5            x * 6
# x * 4            x * 5
# x * 3            x * 4
# x * 2            x * 3
#                  x * 2 --> primeiro dígito.

# Primeiro digito: 11 - (soma dos valores multiplicados % 11) = x 
# se x > 9 o primeiro digito é igual a 0. o primeiro digito será adicionado na próxima multiplicação.
# Primeiro digito: 11 - (soma dos valores multiplicados % 11) = x 

from statistics import multimode

while True:
    cpf = input('Digite seu CPF completo: ') # --> CPF que será inserido
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
    novo_cpf = cpf_backup[:12] + str(digit_1) + str(digit_2)

    # Abaixo há a verficação do CPF junto com uma varificação de que os números não são sequências
    if novo_cpf == cpf_backup and cpf_backup[0:3] != cpf_backup[4:7] and cpf_backup[0:3] != cpf_backup[8:11]: 
        print('Válido.')
    else:
        print('Inválido.')