import os
import subprocess

# Folder where your .asd files are
input_folder = '.'

# Loop through all files in the folder
for filename in os.listdir(input_folder):
    if filename.endswith('.asd'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.splitext(input_path)[0] + '.csv'

        print(f"Converting: {filename} -> {os.path.basename(output_path)}")

        # Run the ASDtoCSV script
        subprocess.run(['python', 'asd2csv.py', input_path, output_path])
