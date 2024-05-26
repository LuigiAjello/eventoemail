import pandas as pd

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
        df_modificado['nome_minusculo'] = df_modificado['nome'].str.replace(' ', '_').str.lower()
        df_modificado['email'] = df_modificado['nome_minusculo'] + '@gmail.com'
        df_modificado['nome'] = df_modificado['nome'].str.replace('_', ' ').str.title()
        df_modificado.drop(columns=['nome_minusculo'], inplace=True)
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
    

def classificar_tipo(df):
    def determinar_tipo(nome):
        doces = ["bolo", "doceria", "Brigadeiro"]
        for doce in doces:
            if doce.lower() in nome.lower():
                return "doce"
            return "salgado"
    df['tipo'] = df['nome'].apply(determinar_tipo)
    return df


def Tratar_df(dict_fornecedor):
    df = pd.DataFrame.from_dict(dict_fornecedor, orient='index')
    df = converter_nomes_minusculos(df)
    df = formatar_nomes(df)
    df = adicionar_repasse(df)
    df = classificar_tipo(df)
    return df

def adicionar_novos_fornecedores(df, novos_fornecedores):
    df_novos = Tratar_df(novos_fornecedores)
    df_combined = pd.concat([df, df_novos], ignore_index=True)
    return df_combined