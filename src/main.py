from dicionario import dict_fornecedor , novos_fornecedores
from Modulofuncoes import Tratar_df

df_final = Tratar_df(dict_fornecedor)
from dicionario import dict_fornecedor
from Modulofuncoes import Tratar_df, adicionar_novos_fornecedores


df_original = Tratar_df(dict_fornecedor)

df_final = adicionar_novos_fornecedores(df_original, novos_fornecedores)

print(df_final)
print(df_final)