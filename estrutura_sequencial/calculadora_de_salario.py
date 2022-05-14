valor_hora = int(input('Digite quanto você recebe por hora: '))
qtd_hora_mes = int(input('Digite quantas horas você trabalha por mês: '))
salario_bruto = valor_hora * qtd_hora_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos
print(f'''
      + Salário Bruto: R$ {salario_bruto}
      - IR: R$ {ir}
      - INSS: R$ {inss}
      - Sindicato: R$ {sindicato}
      = Total Descontos: R$ {total_descontos}
      = Salário Líquido: R$ {salario_liquido}''')