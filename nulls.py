# tratamento de dados nulos

import pandas as pd

dfNull = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios - Null.csv")
print(dfNull)
print('\n')
print(dfNull.isna().sum())
print('\n')
dfNullRemovido = dfNull.dropna(subset=['departamento', 'lucro']) # remova as linhas com valores nulos
print(dfNullRemovido)
print('\n')
print(dfNullRemovido.isna().sum())
print('\n')
dfNullPreenchido_Todos = dfNull.fillna('nenhum') # preenche todos os valore snulos com 'nenhum'
print(dfNullPreenchido_Todos)
print('\n')
dfNullPreenchido_Departamento = dfNull
dfNullPreenchido_Departamento['departamento'] = dfNullPreenchido_Departamento['departamento'].fillna('nenhum') # preenche todos os valores nulos da coluna indicada com 'nenhum'
print(dfNullPreenchido_Departamento)
print('\n')
dfNullPreenchido_Lucro = dfNull
dfNullPreenchido_Lucro['lucro'] = dfNullPreenchido_Lucro['lucro'].fillna(0) 
print(dfNullPreenchido_Lucro)
print('\n')
dfNullPreenchido_DepartamentoLucro = dfNull
dfNullPreenchido_DepartamentoLucro = dfNullPreenchido_DepartamentoLucro.fillna({'departamento':'nenhum', 'lucro':0}) 
print(dfNullPreenchido_Lucro)
print('\n')
dfNullSemDeuplicados = dfNull.drop_duplicates()
print(dfNullSemDeuplicados)
print('\n')
dfTrocadoTipo = dfNull
print(dfNull.info())
dfTrocadoTipo['ativo'] = dfTrocadoTipo['ativo'].astype('str')
print(dfTrocadoTipo.info())
print('\n')
print(dfNull.info())
dfNull['data de nascimento'] = pd.to_datetime(dfNull['data de nascimento']) # se a data original estivesse em formato brasileiro, o codigo seria dfNull['data de nascimento'] = pd.to_datetime(dfNull['data de nascimento']),format='%d/%m/%Y')
print(dfNull.info())