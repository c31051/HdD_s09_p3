import numpy as np
import pandas as pd
A=np.array([50, 16, 15, 26, 32, 50])
dsA=pd.Series(A).std()
T=pd.DataFrame(A)
print(A)
print(np.mean(A))
print(dsA)
T.to_excel('notas.xlsx', index=False)
