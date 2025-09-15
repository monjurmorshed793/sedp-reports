#%%

# Install dependencies
!pip install pandas
!pip install openpyxl

# %%
import pandas as pd

#%%
import os
print(os.getcwd())
file_path = 'data/general_information_bkp.xlsx'
print(os.path.exists(file_path))

#%%
import pandas as pd

#%%
general_information = pd.read_csv('data/general_information_bkp.csv')

#%%
print(general_information)