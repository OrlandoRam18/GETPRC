# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### Generation and expantion transmission planning includding reactive compensation
###
### Deterministic version SD
###
### 29/09/2021
###
### Update 1.000





#-----------------------------------------------------------------------------------
# Call data
import pandas as pd
print('$$$$$$$$$$$$     Discretizador de la demanda determinístico     $$$$$$$$$$$$')
print("")
print("- Inicia etapa de lectura de datos de demanda y factores de planta")
DB = pd.read_excel("14 bus data.xlsx", sheet_name=None)
print("- Finaliza etapa de lectura de datos")

