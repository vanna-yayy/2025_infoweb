def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media >= 60


nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))

if aprovado(nota1, nota2):
    print("Aluno aprovado!")
else:
    print("Aluno em prova final.")
