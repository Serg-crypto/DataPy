import numpy as np
import pandas as pd



#Información sobre el entorno virtual creado para la ejecución del proyecto;

#crear el entorno virtual: python -m venv venv
#activar el entorno virtual: venv\Scripts\activate
#Cambiar el interprete de python CTRL + SHIFT + P

#desactivar el entorno virtual: deactivate







data = np.random.randint(10,21, size=(3,3))

tagColumn = ['Week1','Week2','Week3']
tagMembers = ["Jim","Dimas","Shon"]

firstTable = pd.DataFrame(data, columns=tagColumn)
firstTable.index = tagMembers
print(firstTable)
