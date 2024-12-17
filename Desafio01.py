Nome = input('Qual seu nome: ')

salario = float(input('Qual seu salário: '))

bonus = float(input('Qual o valor do bônus: '))

salario_bonus = (1000 + salario) * bonus

print(f'{Nome} seu salário com o bônus é de R$ {salario_bonus:.2f}')