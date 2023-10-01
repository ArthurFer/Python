# Arthur Fernando
# 13/09/2023
# Programa que recebe um salário base e calcula o imposto de renda a ser descontado

# Tabela base de valores:
#               Base            Aliquota        Dedução
#   Até 2.112                   isento           -
#  De 2.112,01 até 2.826,66     7,50%           158,40
#  De 2.826,67 até 3.751,06       15%           370,40
#  De 3.751,07 até 4.664,68     22,5%           651,73
#  Acima de 4.664,68            27,5%           884,96

base_salario_faixa1 = (2112.01, 2826.66)
base_salario_faixa2 = (2826.67, 3751.06)
base_salario_faixa3 = (3751.07, 4664.68)
base_salario_faixa4 = 4664.68

aliquota_faixa1 = (7.50/100)
aliquota_faixa2 = (15.0/100)
aliquota_faixa3 = (22.5/100)
aliquota_faixa4 = (27.5/100)

deducao_faixa1 = 158.40
deducao_faixa2 = 370.40
deducao_faixa3 = 651.73
deducao_faixa4 = 884.96

instrucao_parada = True

while instrucao_parada:
    try:
        salario_base = float(input("Digite o salario base: "))
    except Exception as erro:
        salario_base = None
        print(erro)

    if salario_base:
        if salario_base >= base_salario_faixa4:
            imposto_devido = (salario_base * aliquota_faixa4) - deducao_faixa4
            salario_liquido = salario_base - imposto_devido
            print(f"Para o salário base R$ {salario_base: .2f} o imposto descontado é R$ {imposto_devido: .2f}")
            print(f"Salário com desconto do imposto de renda é: R$ {salario_liquido: .2f}")

        elif salario_base >= base_salario_faixa3[0] and salario_base < base_salario_faixa3[1]:
            imposto_devido = (salario_base * aliquota_faixa3) - deducao_faixa3
            salario_liquido = salario_base - imposto_devido
            print(f"Para o salário base R$ {salario_base: .2f} o imposto descontado é R$ {imposto_devido: .2f}")
            print(f"Salário com desconto do imposto de renda é: R$ {salario_liquido: .2f}")

        elif salario_base >= base_salario_faixa2[0] and salario_base < base_salario_faixa2[1]:
            imposto_devido = (salario_base * aliquota_faixa2) - deducao_faixa2
            salario_liquido = salario_base - imposto_devido
            print(f"Para o salário base R$ {salario_base: .2f} o imposto descontado é R$ {imposto_devido: .2f}")
            print(f"Salário com desconto do imposto de renda é: R$ {salario_liquido: .2f}")

        elif salario_base >= base_salario_faixa1[0] and salario_base < base_salario_faixa1[1]:
            imposto_devido = (salario_base * aliquota_faixa1) - deducao_faixa1
            salario_liquido = salario_base - imposto_devido
            print(f"Para o salário base R$ {salario_base: .2f} o imposto descontado é R$ {imposto_devido: .2f}")
            print(f"Salário com desconto do imposto de renda é: R$ {salario_liquido: .2f}")

        else:
            print("Salário base isento de imposto de renda")
            print(f"Salário líquido é: {salario_base: .2f}")

    sair = input("Deseja continuar? sim (s), não (n): ")
    if sair != "s":
        instrucao_parada = False





