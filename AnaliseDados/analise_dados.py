import matplotlib.pyplot as plt

notaA = []
notaB = []
notaC = []
notaD = []
notaE = []


def separaNotas(dados):
    for i in dados:
        if i == 'A':
            notaA.append(i)
        elif i == 'B':
            notaB.append(i)
        elif i == 'C':
            notaC.append(i)
        elif i == 'D':
            notaD.append(i)
        elif i == 'E':
            notaE.append(i)


dados = ['A','B','B','B','B','C','C','C','C','D','C','C','D','C','C','C','C','A','D','E','E','C','C','C','E','E','D','D','B','D','A','C','C','D','D','B','B','C','A','B','C','A','A','A','B','E','B','C','C','C','B','B','B','C','C','A','A','A','C','B','C','C','A','B','B','B','C','A','A']



print(f'Quantidade de Respostas: {len(dados)}')

separaNotas(dados)

# print(f"Nota A: {len(notaA)} de 69")
# print(f"Nota B: {len(notaB)} de 69")
# print(f"Nota C: {len(notaC)} de 69")
# print(f"Nota D: {len(notaD)} de 69")
# print(f"Nota E: {len(notaE)} de 69")

qualidadeAbsoluta = (len(notaA) + len(notaB) +
                     len(notaC) + len(notaD) + len(notaE)) / 5
qualidadeRelativaA = (len(notaA))/69
qualidadeRelativaB = (len(notaB))/69
qualidadeRelativaC = (len(notaC))/69
qualidadeRelativaD = (len(notaD))/69
qualidadeRelativaE = (len(notaE))/69
porcentagemQualitativaA = qualidadeRelativaA * 100
porcentagemQualitativaB = qualidadeRelativaB * 100
porcentagemQualitativaC = qualidadeRelativaC * 100
porcentagemQualitativaD = qualidadeRelativaD * 100
porcentagemQualitativaE = qualidadeRelativaE * 100
print(f'Qualidade Absoluta: {qualidadeAbsoluta}')
print(f'Qualidade Relativa A: {qualidadeRelativaA:.2f}')
print(f'Qualidade Relativa B: {qualidadeRelativaB:.2f}')
print(f'Qualidade Relativa C: {qualidadeRelativaC:.2f}')
print(f'Qualidade Relativa D: {qualidadeRelativaD:.2f}')
print(f'Qualidade Relativa E: {qualidadeRelativaE:.2f}')

print(f'Percentagem Relativa A: {porcentagemQualitativaA:.0f}%')
print(f'Percentagem Relativa B: {porcentagemQualitativaB:.0f}%')
print(f'Percentagem Relativa C: {porcentagemQualitativaC:.0f}%')
print(f'Percentagem Relativa D: {porcentagemQualitativaD:.0f}%')
print(f'Percentagem Relativa E: {porcentagemQualitativaE:.0f}%')


data = {
    'A': porcentagemQualitativaA,
    'B': porcentagemQualitativaB,
    'C': porcentagemQualitativaC,
    'D': porcentagemQualitativaD,
    'E': porcentagemQualitativaE
}
names = list(data.keys())
values = list(data.values())
fig, axs = plt.subplots(1, 2, figsize=(7, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
fig.suptitle('Avaliação Restaurante')
plt.show()
