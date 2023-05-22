
# Utilize shift + enter para executar somente um conjunto de linhas

# Criando Series - Creating Series 
# Lista de Series - List of Series
import pandas as pd
series = pd.Series([1, 3, 5, 12, 6, 8])
print(series, '\n'*2)

# Pandas Series with NaN values
import numpy as np
import pandas as pd
s = pd.Series([1, 3, np.nan, 12, 6, 8])
print(s)

# Pandas Series with Strings
import numpy as np
import pandas as pd
s = pd.Series(['python', 3, np.nan, 12, 6, 8])
print(s)

# Access Elements of Pandas Series
import numpy as np
import pandas as pd
s = pd.Series(['python', 3, np.nan, 12, 6, 8])
print(s[0])
print(s[4])


ser = pd.Series([1, 2, 3], index=["a", "b", "c"])

