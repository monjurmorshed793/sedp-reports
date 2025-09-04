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
general_information = pd.read_excel('data/general_information_bkp.xlsx', engine='openpyxl')

#%%
filtered_data = general_information[general_information.eiin=='123456']