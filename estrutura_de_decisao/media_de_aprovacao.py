nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
if media == 10:
  print(f'A média do aluno é {media}. Aprovado com distinção.')
elif media >= 7:
  print(f'A média do aluno é {media}. Aprovado.')
else:
  print(f'A média do aluno é {media}. Reprovado.')