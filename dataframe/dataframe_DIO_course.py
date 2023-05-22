import pandas as pd

# leitura dos arquivos excel, planilhas
df1 = pd.read_excel("planilha1.xlsx") 
df2 = pd.read_excel("planilha2.xlsx") 
df3 = pd.read_excel("planilha3.xlsx") 
df4 = pd.read_excel("planilha4.xlsx") 
df5 = pd.read_excel("planilha5.xlsx") 

# junção dos arquivos, concatenar
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas com o head
df.head()
df.head(3)

# Exibindo as 5 últimas linhas com o tail (cauda)
df.tail()
df.tail(4)

# Quantidade de linhas e colunas
df.shape

# Exibindo as amostras de dados, default is 5
df.sample()
df.sample(100)

# Exibindo os tipos de dados de cada coluna
# obs: String são exibidas com object
df.dtypes

# Alterando os topos de dados da coluna LojaID para object
df["LojaID"] = df["LojaID"].astype("object")

# Consulta valores nulos, null values
df.isnull().sum()

#Substituir os valores nulos por zero
df["Vendas"].fillna(0,inplace=True)

#Substituir os valores nulos pelo média
df["Vendas"].fillna(df["Vendas"].mean(),inplace=True)

# Apagando linhas com valores nulos
df.dropna(inplace=True)

# Apagando linhas com valores nulos com base em apenas em uma coluna, apagando os valores somente de uma coluna
df.dropna(subset=["Vendas"],inplace=True)

# Remover linhas que estejam ocom valores faltante em todas as colunasf
df.dropna(how="all", inplace=True)

# Criando novas colunas em um conjunt de dados Exemplos
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Retornando a maior receita
df["Receita"].max()

# Retornando a menor receita
df["Receita"].min()

# As 3 maiores receitas receita, TOP 3
df.nlargest(3,"Receita")

# Os 3 piores com base na receita, Piores 3, Z3
df.nsmallest(3,"Receita")

# Agrupamento por Cidade
df.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de dados, traz as 10 maiores receitas ordenando por Receita
df.sort_values("Receita", ascending=False).head(10)

# TRABALHANDO COM DATAS

#Transformando a coluna de dadta em tipó inteiro
df["Data"] = df["Data"].astype["int64"]

# Verificar o tipo de dados de cada coluna
df.dtypes

# Criando uma nova coluna com o ano
df["Ano_venda"] = df["Data"].dt.year

# Agrupamento por ano
df.groupby(df["Data"].dt.year)["Receita"].sum()

# Extraindo o mês e o dia
df["dia_venda"] = df["Data"].dt.day
df["mes_venda"] = df["Data"].dt.month
#ou
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month,df["Data"].dt.day)

#Retornando a data mais antiga
df["Data"].min()

# Calculando a diferença em dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter


# filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year ==2019) & (df["Data"].dt.month == 3)]

# VISUALIZAÇÃO DE DADOS
# CRIANDO GRÁFICOS

# Contagem de valores agrupada por LojaID
df["LojaID"].value_counts(ascending=False)

# gráfico de barras verticais
df["LojaID"].value_counts(ascending=False).plot.bar()

# gráfico de barras horizontais, usar ponto e virgula quando estiver no jupiter
df["LojaID"].value_counts(ascending=True).plot.barh()

# gráfico de pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

# Total de vendas por cidade
df["Cidade"].value_counts()

# Adicionando um título e alterando o nome dos eixos
import matplotlib as plt

df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

# Adicionando um título e alterando o nome dos eixos e alterando cor
import matplotlib as plt

df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color ="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")

# alterando o estilo
import matplotlib as plt
plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos Vendidos por mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

df.groupby(df["mes_venda"])["Qtde"].sum()

# apenas o ano de 2019
df_2019 = df[df["Ano_venda"] == 2019]
df_2019.groupby(df["mes_venda"])["Qtde"].sum().plot(marker="v") # marker="o" marker="*" 
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()

# Grafico de histograma
plt.hist(df["Qtde"], color="magenta")

# Grafico de dispersão
plt.scatter(x=df_2019["dia_venda"], y=df_2019["dia_venda"])

# Salvando como Png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico Qtde x MÊS.png")

# upload do arquivo
plt.style.use("seaborn")

df = pd.read_excel("adventureWorks.xlsx")
 
# Visualizando as 5 primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# verificando os tipos de dados
df.dtypes

# Qual é a receita total?
df["Valor Venda"].sum()

# Qual é a custo total?
df["Custo"] =df["Custo Unitário"].mul(df["Quantidade"])

# Qual é a custo total? round arredonda o valor em duas casas neste caso
round(df["Custo"].sum(),2)

# Agora que temos a receita, o custo e o total, podemos achar o lucro total
# Vamos criar uma colna de lucro que será Receita - Custo
df["Lucro"] = df["Valor Venda"] - df["Custo"]

# Total Lucro
round(df["Lucro"].sum(),2)

# Criar uma coluna com o total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

# Agora, queremos saber a media do tempo de envio para cada Marca, e para isso precisamos 
# transformar a coluna Tempo_envio em numerica

# Extraindo apenas os dias, retirando o  o days do valor
df["Tempo_envio"] = (df["Data Envio"])- df["Data Venda"].dt.days

# Verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

# Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

# Valores Nullos
df.isnull().sum()

# Lucro por ano e por Marca

df.groupby([df["Data Venda"].dt.year,"Marca"])["Lucro"].sum()


pd.options.display.float_format = "{:20,.2f}".format

# Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()

# Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

# Grafico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title= "Total Produtos Vendidos")
plt.slabel("Total")
plt.ylabel("Produto")

# Gráfico Lucro por ano
df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title = "Lucro x Ano")
plt.slabel("Ano")
plt.ylabel("Receita")

# Filtrar as vendas de 2009
df_2009 = df[df["Ano_venda"].dt.year == 2019]

# Gráficos de linhas
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title = "Lucro x Mês")
plt.slabel("Mês")
plt.ylabel("Lucro")

df_2009.groupby("Marca")["lucro"].sum().plot(title = "Lucro x Marca")
plt.slabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")

df_2009.groupby("Classe")["lucro"].sum().plot(title = "Lucro x Classe")
plt.slabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")


df["Tempo_envio"].describe()

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"])

# Histograma
plt.hist(df["Tempo_envio"])
            
# Tempo minimo de envio
df["Tempo_envio"].min()

# Tempo Maximo de envio
df["Tempo_envio"].max()

# Identificando o Outlier
df[df["Tempo_envio"] == 20] 

# Salvando o arquivo em CSV
df.to_csv("df_vendas_novo.csv", index= False)