# Utilize shift + enter para executar somente um conjunto de linhas

# Importing pandas library
import pandas as pd

# Create an empty DataFrame
import pandas as pd
df = pd.DataFrame()
print(df)

# Create DataFrame from List of Lists
import pandas as pd

#list of lists
data = [['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3']]

df = pd.DataFrame(data)
print(df)

# Create DataFrame from Dictionary
import pandas as pd

#list of lists
data = {'col1': ['a1', 'a2', 'a3'],
        'col2': ['b1', 'b2', 'b3'],
        'col3': ['c1', 'c2', 'c3']}

df = pd.DataFrame(data)
print(df)

# Check if DataFrame is empty – Positive Scenario
import pandas as pd

# Initialize a DataFrame 
df = pd.DataFrame()
# Check if DataFrame is empty
if df.empty:
    print('The DataFrame is empty.')
else:
    print('The DataFrame is not empty.')
    
# Check for a non-empty DataFrame

# Syntax to create DataFrame
# The syntax to create a DataFrame from dictionary object is shown below.
# mydataframe = DataFrame(dictionary)

# Create DataFrame from Dictionary
import numpy as np
import pandas as pd

mydictionary = {'names': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'physics': [68, 74, 77, 78],
	'chemistry': [84, 56, 73, 69],
	'algebra': [78, 88, 82, 87]}

#create dataframe using dictionary
df_marks = pd.DataFrame(mydictionary)
print(df_marks)

# Create DataFrame from Python Dictionary
import numpy as np
import pandas as pd
mydictionary = {'names': ['Somu', 'Kiku', 'Amol', 'Lini'],
	'roll_no': [1, 2, 3, 4]
	}
#create dataframe using dictionary
df_students = pd.DataFrame(mydictionary)
print(df_students)

# Initialize a DataFrame     
import pandas as pd
df = pd.DataFrame(
	[[21, 72, 67.1],
	[23, 78, 69.5],
	[32, 74, 56.6],
	[52, 54, 76.2]],
	columns=['a', 'b', 'c'])

# Check if DataFrame is empty
if df.empty:
    print('The DataFrame is empty.')
else:
    print('The DataFrame is not empty.')


# Criando do Dataframe - Creating DataFrame
# Lista de Listas      - List of Lists 
import pandas as pd
listPepper = [ 
            [50, "Bell pepper", "Not even spicy"], 
            [5000, "Espelette pepper", "Uncomfortable"], 
            [500000, "Chocolate habanero", "Practically ate pepper spray"]
            ]

dataFrame1 = pd.DataFrame(listPepper)
print(dataFrame1, '\n'*2)

# Out =

#         0                   1                             2
# 0      50         Bell pepper                Not even spicy
# 1    5000    Espelette pepper                 Uncomfortable
# 2  500000  Chocolate habanero  Practically ate pepper spray


# You may have noticed that the column and row labels aren't very informative in the DataFrame we've created. 
# You can pass additional information when creating the DataFrame, and one thing you can do is give the row/column 
# labels you want to use:

import pandas as pd
listScoville = [50, 5000, 500000]
listName = ["Bell pepper", "Espelette pepper", "Chocolate habanero"]
listFeeling = ["Not even spicy", "Uncomfortable", "Practically ate pepper spray"]
dataFrame = pd.DataFrame(zip(listScoville, listName, listFeeling), columns = ['Scoville', 'Name', 'Feeling'])
print(dataFrame, '\n'*2)
# Out =

#    Scoville                Name                       Feeling
# 0        50         Bell pepper                Not even spicy
# 1      5000    Espelette pepper                 Uncomfortable
# 2    500000  Chocolate habanero  Practically ate pepper spray

# obs: o pandas cria um indice automaticamente vc pode usar o set_index => dataFrame1.set_index('Scoville')
dataFrame = dataFrame.set_index('Scoville') 
# utilizar ao inplace=True para manter a alteração
dataFrame.set_index('Scoville', inplace=True)
print(dataFrame)

# # Out =
# Scoville            Name                       Feeling
# 50               Bell pepper                Not even spicy
# 5000        Espelette pepper                 Uncomfortable
# 500000    Chocolate habanero  Practically ate pepper spray

# In our example the representation would look like this:
# Another data representation you can use here is to provide the data as a list of dictionaries in the 
# following format:
import pandas as pd
listPepperRepresentation = [
    { 'columnName1' : 'valueForRow1', 'columnName2': 'valueForRow1',  },
    { 'columnName1' : 'valueForRow2', 'columnName2': 'valueForRow2',  },
    { 'columnName1' : 'valueForRow3', 'columnName2': 'valueForRow3',  },
    ...
]

listPepper = [
  {'Scoville' : 50, 'Name' : 'Bell pepper', 'Feeling' : 'Not even spicy'},
  {'Scoville' : 5000, 'Name' : 'Espelette pepper', 'Feeling' : 'Uncomfortable'},
  {'Scoville' : 500000, 'Name' : 'Chocolate habanero', 'Feeling' : 'Practically ate pepper spray'},
]
dataFrame3 = pd.DataFrame(listPepper)
print(dataFrame3)

# Creating a DataFrame From Dictionaries
# Dictionaries are another way of providing data in the column-wise fashion. Every column is given 
# a list of values rows contain for it, in order:
import pandas as pd
dictionaryDataRepresentation = {
	'columnName1' : ['valueForRow1', 'valueForRow2', 'valueForRow3'],
	'columnName2' : ['valueForRow1', 'valueForRow2', 'valueForRow3'],
	
}

dictionaryData = {
    'Scoville' : [50, 5000, 500000],
    'Name' : ["Bell pepper", "Espelette pepper", "Chocolate habanero"],
    'Feeling' : ["Not even spicy", "Uncomfortable", "Practically ate pepper spray"]
}

dataFrame = pd.DataFrame(dictionaryData)

# Print the dataframe
print(dataFrame)

# Reading a DataFrame From a File
# There are many file types supported for reading and writing DataFrames. Each respective filetype function 
# follows the same syntax read_filetype(), such as read_csv(), read_excel(), read_json(), read_html(), etc...
# A very common filetype is .csv (Comma-Separated-Values). The rows are provided as lines, with the values 
# they are supposed to contain separated by a delimiter (most often a comma). You can set another delimiter 
# via the sep argument.
# If you aren't familiar with the .csv file type, this is an example of what it looks like:
import pandas as pd
pepperDataFrame = pd.read_csv('pepper_example.csv')
pepperDataFrame2 = pd.read_csv('pepper_example.csv', sep=',')

# For other separators, provide the `sep` argument
# pepperDataFrame = pd.read_csv('pepper_example.csv', sep=';')

print(pepperDataFrame, '\n'*2)
print(pepperDataFrame2, '\n'*2)

# Manipulating DataFrames
# This section will be covering the basic methods for changing a DataFrame's structure. 
# However, before we get into that topic you should know how to access individual rows 
# or groups of rows, as well as columns.

# Accessing/Locating Elements
# Pandas has two different ways of selecting data - loc[] and iloc[].

# loc[] allows you to select rows and columns by using labels, like row['Value'] and 
# column['Other Value']. Meanwhile, iloc[] requires that you pass in the index of the 
# entries you want to select, so you can only use numbers. You may also select columns 
# just by passing in their name in brackets. Let’s see how this works in action:
import pandas as pd
pepperDataFrame = pd.read_csv('pepper_example.csv')
print(pepperDataFrame.loc[5])
import pandas as pd
pepperDataFrame = pd.read_csv('pepper_example.csv')
print(pepperDataFrame.iloc[1]) 
import pandas as pd
pepperDataFrame = pd.read_csv('pepper_example.csv')
print(pepperDataFrame.loc[:2]) 

# It's important to note that iloc[] always expects an integer. loc[] supports other data types as well. 
# We can use an integer here too, though we can also use other data types such as strings.
# You can also access specific values for elements. For example, we might want to access the element in 
# the 2nd row, though only return its Name value:
# print(pepperDataFrame1.iloc[4, 2]) 
# Manipulating Indices
# Indices are row labels in a DataFrame, and they are what we use when we want to access rows. Since we didn't 
# change the default indices Pandas assigns to DataFrames upon their creation, all our rows have been labeled
# with integers from 0 and up.

# Manipulando índices
# Os índices são rótulos de linha em um , e eles são o que usamos quando queremos acessar linhas. Como não alteramos 
# os índices padrão que o Pandas atribui a s após sua criação, todas as nossas linhas foram rotuladas com inteiros de 
# 0 para cima.DataFrameDataFrame

# A primeira maneira de alterar a indexação do nosso é usando o método. Passamos qualquer uma das colunas em nosso para 
# este método e ele se torna o novo índice. Assim, podemos criar índices nós mesmos ou simplesmente atribuir uma coluna 
# como índice.DataFrameset_index()DataFrame

# Observe que o método não altera o original, mas retorna um novo com o novo índice, portanto, temos que atribuir o valor 
# de retorno à variável se quisermos manter a alteração ou definir o sinalizador

import pandas as pd
listPepper = [
  {'Scoville' : 50, 'Name' : 'Bell pepper', 'Feeling' : 'Not even spicy'},
  {'Scoville' : 5000, 'Name' : 'Espelette pepper', 'Feeling' : 'Uncomfortable'},
  {'Scoville' : 500000, 'Name' : 'Chocolate habanero', 'Feeling' : 'Practically ate pepper spray'},
]

dataFrame = pd.DataFrame(listPepper)
# print(dataFrame)
dataFrame.set_index('Scoville') # Não altera efetivamente o indice'
print(dataFrame)
dataFrame.set_index('Scoville', inplace=True) # Inplace altera/remove o indice
print(dataFrame)


# Agora que temos um índice não padrão, podemos usar um novo conjunto de valores, usando o , 
# o Pandas preencherá automaticamente os valores com para cada índice que não puder ser correspondido com uma linha existente:reindex()NaN

import pandas as pd
new_index = [50, 5000, 'New value not present in the data frame']
dataFrame.reindex(new_index)
print(dataFrame)

# Você pode controlar qual valor o Pandas usa para preencher os valores ausentes definindo o parâmetro opcional:
import pandas as pd
new_index = [50, 5000, 'New value not present in the data frame']

dataFrame.reindex(new_index, fill_value=0)    
print(dataFrame)
# Adicionar e remover linhas torna-se simples se você estiver confortável com o uso do . 
# Se você definir uma linha que não existe, ela será criada:loc[]

import pandas as pd
listPepper = [
  {'Scoville' : 50, 'Name' : 'Bell pepper', 'Feeling' : 'Not even spicy'},
  {'Scoville' : 5000, 'Name' : 'Espelette pepper', 'Feeling' : 'Uncomfortable'},
  {'Scoville' : 500000, 'Name' : 'Chocolate habanero', 'Feeling' : 'Practically ate pepper spray'},
]

dataFrame = pd.DataFrame(listPepper)
dataFrame.loc[50] = [10000, 'Serrano pepper', 'I regret this']
print(dataFrame)
# E se você quiser remover uma linha, especifique seu índice para a função. Ele usa um parâmetro opcional,
# O aceita / ou /. Dependendo disso, a função descarta a linha em que é chamada ou a coluna em que é chamada.
# drop()axisaxis0index1columnsdrop()
# Não especificar um valor para o parâmetro excluirá a linha correspondente por padrão, como é por padrão:axisaxis0

dataFrame.drop(50, inplace=True) 
print(dataFrame)


# Você também pode renomear linhas que já existem na tabela. A função aceita um dicionário de alterações 
# que você deseja fazer:

dataFrame.rename({0:"First", 1:"Second"}, inplace=True)
print(dataFrame)

# Observe que e também aceite o parâmetro opcional - . Definir isso como (por padrão) dirá ao Pandas 
# para alterar o original em vez de retornar um novo. Se não estiver configurado, você terá que empacotar 
# o resultado em um novo para manter as alterações.drop()rename()inplaceTrueFalseDataFrameDataFrame
# Outro método útil que você deve estar ciente é a função que remove todas as linhas duplicadas do . 
# Vamos demonstrar isso adicionando duas linhas duplicadas:

dataFrame.loc[3] = [60.000, "Bird's eye chili", "4th stage of grief"]
dataFrame.loc[4] = [60.000, "Bird's eye chili", "4th stage of grief"]

print(dataFrame)

# Now we can call drop_duplicates():
# Excluindo Duplicados

dataFrame.drop_duplicates(inplace=True)
print(dataFrame)

# Manipulating Columns
# New columns can be added in a similar way to adding rows:

dataFrame['Color'] = ['Green', 'Bright Red', 'Brown','Blue']
print(dataFrame)

# Removendo Colunas - Drop Columns - Excluir Colunas
# Also similarly to rows, columns can be removed by calling the drop() function, 
# the only difference being that you have to set the optional parameter axis to 1 
# so that Pandas knows you want to remove a column and not a row:

dataFrame.drop('Feeling', axis=1, inplace=True)
print(dataFrame)

# Renomear Colunas - Set Columns
# When it comes to renaming columns, the rename() function needs to be told 
# specifically that we mean to change the columns by setting the optional parameter 
# columns to the value of our "change dictionary":

dataFrame.rename(columns={"Name":"Nome"}, inplace=True)
print(dataFrame)

# Examples

# Constructing DataFrame from a dictionary.

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df)
#index col1  col2
#  0     1     3
#  1     2     4

# Notice that the inferred dtype is int64.
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df.dtypes)
# col1    int64
# col2    int64
# dtype: object

# To enforce a single dtype:
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d, dtype=np.int8)
print(df.dtypes)
# col1    int8
# col2    int8
# dtype: object

# Constructing DataFrame from a dictionary including Series:

d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
df = pd.DataFrame(data=d, index=[0, 1, 2, 3])
print(df)
# index    col1  col2
# 0     0   NaN
# 1     1   NaN
# 2     2   2.0
# 3     3   3.0

# Constructing DataFrame from numpy ndarray:

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
print(df2)
#    a  b  c
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# Constructing DataFrame from a numpy ndarray that has labeled columns:

data = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)],dtype=[("a", "i4"), ("b", "i4"), ("c", "i4")])
df3 = pd.DataFrame(data, columns=['c', 'a'])
print(df3)
print(df3.dtypes)
#    c  a
# 0  3  1
# 1  6  4
# 2  9  7

# Constructing DataFrame from dataclass:
from dataclasses import make_dataclass
Point = make_dataclass("Point", [("x", int), ("y", int)])
pd.DataFrame([Point(0, 0), Point(0, 3), Point(2, 3)])
#    x  y
# 0  0  0
# 1  0  3
# 2  2  3

# Constructing DataFrame from Series/DataFrame:

ser = pd.Series([1, 2, 3], index=["a", "b", "c"])
df = pd.DataFrame(data=ser, index=["a", "b", "c"], columns=["x"])
print(ser)
print(df)
#    0
# a  1
# c  3

df1 = pd.DataFrame([1, 2, 3], index=["a", "b", "c"], columns=["x"])
df2 = pd.DataFrame(data=df1, index=["a", "c"])
print(df2)
#    x
# a  1
# c  3

df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=["a", "b", "c"], columns=["x","y","z"])
df2 = pd.DataFrame(data=df1, index=["a", "c"])
print(df2)    
    