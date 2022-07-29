def leiainteiro(n):
    while True:
        try:
            x = int(input(n))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;34mO usuário não preencheu os dados.\033[m')
        else:
            return x


def leiareal(n):
    while True:
        try:
            x = float(input(n))
        except (TypeError,ValueError):
            print('\033[1;31mDigite um número real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;34mO usuário preferiu não preencher.\033[m')
        else:
            return x


print('\033[1;42m---BEM-VINDO!---\033[m')
nume = leiareal('Digite um número real:')
num = leiainteiro('Digite um número inteiro:')
print(f'O valores digitados foram {num} e {nume}.')
print('\033[1;42m------FIM-------\033[m')