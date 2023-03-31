import datetime
import pandas as pd
import json


def verificar_dados(id, nome, idade, cpf, cidade):
    if nome == '' and idade is None and cpf is None:
        return 'Vazio'
    if id == '':
        return "Id vazio"
    
    if nome == '':
        return "Nome vazio"
    
    if nome.isdigit():
        return 'Nome invalido, digite apenas letras'
    
    if idade == '':
        return "Idade vazia"
    
    if not idade.isdigit():
        return 'Idade invalido, digite apenas numeros'
    
    if not cpf and cidade == '':
        return "Campos cidade e CPF vazios"
    
    if not cpf:
        return 'CPF vazio'

    if cidade == '':
        return 'Cidade vazio'
    
 

    return 'Preenchido'

def dados_main():
    with open('Dados.txt', 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
        dados = [linha.strip().split(',') for linha in linhas]
        colunas = ['ID', 'Nome Completo', 'Idade', 'CPF', 'Cidade']
        
        df = pd.DataFrame(dados, columns=colunas)

        # Verifica se os campos ID, Nome, Idade e CPF estão preenchidos e adiciona uma nova coluna para mostrar mensagem
        df['Verificação Dados'] = df.apply(lambda row: verificar_dados(row['ID'], row['Nome Completo'], row['Idade'], row['CPF'], row['Cidade']), axis=1)

        # Cria uma nova coluna 'Data' e preenche com a data atual
        data_atual = datetime.date.today()
        df['Data'] = data_atual.strftime("%d/%m/%Y")

        # Salva o DataFrame em um arquivo Excel com a data atual no nome
        nome_arquivo = data_atual.strftime("dados_%Y-%m-%d.xlsx")
        df.to_excel(nome_arquivo, index= False)


dados_main()
