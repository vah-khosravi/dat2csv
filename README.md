# dat2csv
This repository will help to convert .dat files recorded by ASD FieldSpec spectroradiometers to .csv
To do so:
All codes and spectra should be in the "ASDtoCSV" directory.
[Path to your directory which contains the code and .dat files]>python asd2csv.py Spectrum00001.asd Spectrum00001.csv	      # Convert single spectra to .csv format
[Path to your directory which contains the code and .dat files]>python batch_convert.py                                     # Convert all spectra to .csv format
[Path to your directory which contains the code and .dat files]>python merge_spectra.py                                     # Merge all spectra into 'merged_spectra.csv'
