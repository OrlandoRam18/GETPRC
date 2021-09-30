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


# ----------------------------------------------------------------------------------
# import initial libraries
import pandas as pd; from datetime import date; import time


#-----------------------------------------------------------------------------------
# Call data
print('$$$$$$$$$$$$     Generation and transmission Expantion planning     $$$$$$$$$$$$')
today = date.today().strftime("%d/%m/%Y")
print('                 ',date.today() ,'  ',time.strftime("%X"))
print("")
print(time.strftime("%X"), "- Start calling data from the network to analyze")
DB = pd.read_excel("14 bus data.xlsx", sheet_name=None)
print(time.strftime("%X"), "- End of data readinng")

