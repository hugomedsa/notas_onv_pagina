lista = []
cont = 0

with open('meu_arquivo.txt', 'r', encoding='utf-8' ) as file:
    linhas = file.readlines()
    for linha in linhas:

        if 'º' in linha:
            cont = 0

        cont+=1

        if cont == 15:
            if linha[2:6].replace('\n','') != '':
                lista.append(linha[2:6].replace('\n',''))


with open('dados.txt', 'a', encoding='utf-8') as file:
    for item in lista:
        file.write(item + '\n')
