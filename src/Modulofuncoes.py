
def converter_nomes_minusculos(dataframe):
    if 'nome' in dataframe.columns:
        dataframe['nome'] = dataframe['nome'].str.lower()
        return dataframe
    else:
        print("Erro: A coluna 'nome' não existe no DataFrame.")
        return None


