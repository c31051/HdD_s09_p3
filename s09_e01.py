import numpy as np
import pandas as pd
A=np.array([5, 1, 15, 6, 2, 3])
dsA=pd.Series(A).std()
T=pd.DataFrame(A)
print(A)
print(np.mean(A))
print(dsA)
T.to_excel('notas.xlsx', index=False)
