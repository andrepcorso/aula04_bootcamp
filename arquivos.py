import csv

caminha_do_arquivo: str = "exemplo.csv"

arquivo_csv: list =[]

with open(file=caminha_do_arquivo, mode="r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

    print(arquivo_csv)