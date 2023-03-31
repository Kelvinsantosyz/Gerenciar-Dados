import pandas as pd
import json

df = pd.read_excel('dados_2023-03-31.xlsx')

objeto = df.to_json(orient='index', indent=2, force_ascii= False)

with open('dados.json', 'w', encoding='utf8') as arquivo:
    arquivo.write(objeto)


