
def converter_nomes_minusculos(dataframe):
    if 'nome' in dataframe.columns:
        dataframe['nome'] = dataframe['nome'].str.lower()
        return dataframe
    else:
        print("Erro: A coluna 'nome' não existe no DataFrame.")
        return None


def formatar_nomes(dataframe):

    df_modificado = dataframe.copy()
    if 'nome' in df_modificado.columns:
        df_modificado['nome'] = df_modificado['nome'].str.replace(' ', '_')
        df_modificado['email'] = df_modificado['nome'] + '@gmail.com' 
        return df_modificado
    else:
        print("Erro: A coluna 'nome' não existe no DataFrame.")
        return None

def adicionar_repasse(dataframe):

    df_modificado = dataframe.copy()
    if 'vendas' in df_modificado.columns:
        df_modificado['repasse'] = df_modificado['vendas'] * 0.5
        return df_modificado
    else:
        print("Erro: A coluna 'vendas' não existe no DataFrame.")
        return None