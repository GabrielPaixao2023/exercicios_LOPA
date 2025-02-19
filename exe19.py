contAlunos = 1
qtdAlunos = 6
qtdNotas = 2
qtdAprovados = 0
qtdReprovados = 0
qtdExame = 0
somaMedia = 0 

while contAlunos <= qtdAlunos:
    print('\n') #imprime um e pula a linha no console
    print('##############')
    print(f'Aluno {contAlunos}')

    notaUm = int(input('Insira a primeira nota'))
    notaDois = int(input('Insira a segunda nota'))

    media = (notaUm + notaDois) / qtdNotas
    somaMedia += media 

    if media < 3:
        print('reprovado')
        qtdReprovados += 1
    elif media > 3 and media < 7:
        print('Exame')
        qtdExame += 1
    elif media > 7:
        print('Aprovado')
        qtdAprovados += 1

    contAlunos += 1   

mediaClasse = somaMedia / qtdAlunos
