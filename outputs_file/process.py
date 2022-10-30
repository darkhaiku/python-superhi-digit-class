import glob
import os
import shutil

inputs = glob.glob('inputs\*')

os.makedirs('outputs_file', exist_ok=True)

for filepath in inputs:
    output_path = filepath.replace('inputs', 'outputs_file')
    shutil.copyfile(filepath, output_path)