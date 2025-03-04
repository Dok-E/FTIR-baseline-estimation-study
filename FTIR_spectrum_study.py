# on va essayer de lire et corriger des spectres FTIR des datasets accessibles publiquement

import pandas as pd
import matplotlib.pyplot as plt
from pybaselines import Baseline, utils


# Le chemin du fichier avec dataset
file_path = '/media/eva/DATA/DATA/FTIR_study/SiFuBouleau1.xlsx'
xls = pd.ExcelFile(file_path)
sheets = xls.sheet_names
print (sheets)

# Selectionner la feuille de background
background_sheet = ("SiWaferAVG")
sp_to_process = ("SiFuBouleauTrialThird1")


# Lire le fichier Excel - BACKGROUND
df = pd.read_excel(file_path, background_sheet)
print(df.shape)
df = df.transpose()  # Transposer le dataframe
print(df.shape)

# Ne conserver du tableau que les données numériques
df2 = df.select_dtypes(include=['int32','float32','int64','float64'])
print(df2.shape)
print(df2)

bkg_tab =  df2.to_numpy()   # Convertir le dataframe en un tableau numpy
bkg_waves = bkg_tab [0,:]   # Afficher les 2 premières lignes et 5 premières colonnes
bkg_data = bkg_tab [1,:]

# Lire le fichier Excel - BACKGROUND
df = pd.read_excel(file_path, sp_to_process)
print(df.shape)
df = df.transpose()  # Transposer le dataframe
print(df.shape)

# Ne conserver du tableau que les données numériques
df2 = df.select_dtypes(include=['int32','float32','int64','float64'])
print(df2.shape)
print(df2)

sp_tab =  df2.to_numpy()   # Convertir le dataframe en un tableau numpy
sp_waves = sp_tab [0,:]   # Afficher les 2 premières lignes et 5 premières colonnes
sp_data = sp_tab [1,:]

sp = sp_data - bkg_data
baseline_fitter = Baseline(x_data=bkg_waves)
y=sp
x=bkg_waves

bkg_1, params_1 = baseline_fitter.modpoly(y, poly_order=3)
bkg_2, params_2 = baseline_fitter.asls(y, lam=1e5, p=0.01)
bkg_21, params_21 = baseline_fitter.iasls(y, lam=1e7, lam_1=1e-5, p=0.1)
bkg_3, params_3 = baseline_fitter.mor(y, half_window=50)
bkg_4, params_4 = baseline_fitter.snip(    y, max_half_window=50, decreasing=True, smooth_half_window=2)


plt.plot(bkg_waves, bkg_data,label='Background Spectrum', linestyle='--', color='b')
plt.plot(sp_waves, sp_data,label='Pollen Sample Spectrum',linestyle='-', color='g')
plt.plot(sp_waves, sp ,label='Background substracted',linestyle='-', color='r')

plt.plot(x, y, label='raw data', lw=1.5)
plt.plot(x, bkg_1, '--', label='modpoly')
plt.plot(x, bkg_2, '--', label='asls')
plt.plot(x, bkg_3, '--', label='mor')
plt.plot(x, bkg_4, '--', label='snip')
plt.plot(x, bkg_21, '--', label='iasls')

plt.legend()
plt.show()