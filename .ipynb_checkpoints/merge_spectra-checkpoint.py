import os
import pandas as pd

# Get all .csv files (skip the merged file if it already exists)
csv_files = [f for f in os.listdir('.') if f.endswith('.csv') and f != 'merged_spectra.csv']

merged_data = []
wavelengths = None

for file in csv_files:
    df = pd.read_csv(file)

    # First column is wavelength, second is reflectance
    if wavelengths is None:
        wavelengths = df.iloc[:, 0].values  # Save wavelengths from first file
        header = ['Filename'] + list(wavelengths)

    reflectance = df.iloc[:, 1].values
    merged_data.append([file] + list(reflectance))

# Create DataFrame
final_df = pd.DataFrame(merged_data, columns=header)

# Save to one CSV file
final_df.to_csv('merged_spectra.csv', index=False)

print("Merged all spectra into 'merged_spectra.csv'")
