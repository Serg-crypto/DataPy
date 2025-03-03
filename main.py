import numpy as np
import pandas as pd

data = np.random.randint(10,21, size=(3,3))

tagColumn = ['Week1','Week2','Week3']
tagMembers = ["Jim","Dimas","Shon"]

firstTable = pd.DataFrame(data, columns=tagColumn)
firstTable.index = tagMembers
print(firstTable)
