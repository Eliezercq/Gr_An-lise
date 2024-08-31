import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Inicializa a janela do tkinter
Tk().withdraw()

# Abre a janela de diálogo para selecionar o arquivo
file_path = askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV Files", "*.csv")])

# Carrega o arquivo CSV selecionado
if file_path:
    df = pd.read_csv(file_path, delimiter=';', skipinitialspace=True)
    print("Arquivo carregado com sucesso!")
else:
    print("Nenhum arquivo foi selecionado.")

# Verificar os tipos de dados das colunas
print(df.dtypes)

#Converter colunas numéricas que possam ter sido lidas como strings
df['Lucro_Invest'] = pd.to_numeric(df['Lucro_Invest'], errors='coerce')
df['Lucro_Salario'] = pd.to_numeric(df['Lucro_Salario'], errors='coerce')
df['Desp_fixas'] = pd.to_numeric(df['Desp_fixas'], errors='coerce')
df['Desp_Gerais'] = pd.to_numeric(df['Desp_Gerais'], errors='coerce')

# Verificar os tipos de dados após a conversão
print(df.dtypes)

# Remover linhas com valores não numéricos após a conversão
df = df.dropna()

# Verificar se o DataFrame está vazio após a limpeza
if df.empty:
    print("O DataFrame está vazio após a remoção de valores não numéricos.")
else:
    print(df.head())  # Exibir as primeiras linhas para confirmação

    # Arredondar valores para 2 casas decimais
    df[['Lucro_Invest', 'Lucro_Salario', 'Desp_fixas', 'Desp_Gerais']] = df[['Lucro_Invest', 'Lucro_Salario', 'Desp_fixas', 'Desp_Gerais']].round(2)

    # Combinando Ano e Mês
    df['Ano_Mes'] = df['Ano'].astype(str) + '-' + df['Mês']

    # Mostrar os dados em um gráfico de barras usando a nova coluna como eixo X
    ax = df.plot(x='Ano_Mes', y=['Lucro_Invest', 'Lucro_Salario', 'Desp_fixas', 'Desp_Gerais'], kind='bar', figsize=(10, 6))

    # Configurações do gráfico
    plt.title('Lucro e Despesas ao longo dos anos')
    plt.xlabel('Ano-Mês')
    plt.ylabel('Valores')
    plt.legend(['Lucro Investimento', 'Lucro Salário', 'Despesas Fixas', 'Despesas Gerais'], loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(axis='y')

    # Formatando o eixo Y para mostrar valores com 'R$' e 2 casas decimais
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'R${x:.2f}'))

    # Salvando a imagem
    plt.savefig('Análise_Financeira.png', bbox_inches='tight')

    # Exibir o gráfico
    plt.show()
