# Introduction
Pandas is an open-source Python library for data analysis. It is designed for efficient and intuitive handling and processing of structured data.

The two main data structures in Pandas are Series and DataFrame. Series are essentially one-dimensional labeled arrays of any type of data, while DataFrames are two-dimensional, with potentially heterogenous data types, labeled arrays of any type of data. Heterogenous means that not all "rows" need to be of equal size.

In this article we will go through the most common ways of creating a DataFrame and methods to change their structure.

We'll be using the Jupyter Notebook since it offers a nice visual representation of DataFrames. Though, any IDE will also do the job, just by calling a print() statement on the DataFrame object.


# Introdução
Pandas é uma biblioteca Python de código aberto para análise de dados. Ele é projetado para o manuseio e processamento eficiente e intuitivo de dados estruturados.

As duas principais estruturas de dados no Pandas são Series e DataFrames - Conjunto de Dados. Series são essencialmente matrizes rotuladas unidimensionais de qualquer tipo de dados, enquanto os conjuntos de dados são bidimensionais, com tipos de dados potencialmente heterogêneos, matrizes rotuladas de qualquer tipo de dados. Heterogêneo significa que nem todas as "linhas" precisam ser de tamanho igual.SeriesDataFrameSeriesDataFrame

Criando DataFrames
Sempre que você cria um DataFrames, quer esteja criando um manualmente ou gerando um a partir de uma fonte de dados, como um arquivo, os dados devem ser ordenados de forma tabular, como uma sequência de linhas contendo dados.DataFrame

Isso implica que as linhas compartilham a mesma ordem de campos, ou seja, se você quiser ter um com informações sobre o nome e a idade de uma pessoa, você deseja ter certeza de que todas as suas linhas contêm as informações da mesma maneira.DataFrame

Qualquer discrepância fará com que o seja defeituoso, resultando em erros.DataFrame


fonte:https://stackabuse.com/python-with-pandas-dataframe-tutorial-with-examples/
