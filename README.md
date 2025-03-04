## This code tries to explore the pybaselines package and its parameters, which is very instructive. Many manipulations can be performed.

https://pypi.org/project/pybaselines/

The provided code reads and processes FTIR spectra from an Excel file, performs baseline correction using various methods, and plots the results. Here is a step-by-step explanation:  

# Import Libraries:  

pandas for reading Excel files.
matplotlib.pyplot for plotting.
pybaselines for baseline correction.

# Read Excel File:  
The path to the Excel file is specified.
The Excel file is read, and the sheet names are printed.
# Select Sheets:  
The background and sample sheets are specified.

# Read Background Data:  
The background sheet is read and transposed.
Only numeric data is retained.
The data is converted to a NumPy array, and the wavenumbers and background data are extracted.

# Read Sample Data:  
The sample sheet is read and transposed.
Only numeric data is retained.
The data is converted to a NumPy array, and the wavenumbers and sample data are extracted.

# Subtract Background:  
The background data is subtracted from the sample data.

# Baseline Correction:  
A Baseline object is created with the wavenumbers.
Various baseline correction methods (modpoly, asls, iasls, mor, snip) are applied to the data.

# Plotting:  
The background spectrum, sample spectrum, background-subtracted spectrum, and baseline-corrected spectra are plotted.

Results example :
![image](https://github.com/user-attachments/assets/d302f25b-b5de-48b8-8182-b912fb26c12f)
![image](https://github.com/user-attachments/assets/54ce766e-c46c-4c91-bc7b-86251c619d64)

