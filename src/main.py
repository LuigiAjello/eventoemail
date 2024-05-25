import pandas as pd
from dicionario import df 
from Modulofuncoes import converter_nomes_minusculos
df_convertido = converter_nomes_minusculos(df)
from Modulofuncoes import formatar_nomes
df_convertido = formatar_nomes (df_convertido)
from Modulofuncoes import adicionar_repasse 
df_convertido = adicionar_repasse (df_convertido)
print(df_convertido)