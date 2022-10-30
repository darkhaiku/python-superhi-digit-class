import glob
import os
import shutil

inputs = glob.glob('inputs\*.jpg')

class Digitizer:
    def __init__(self, filepath) -> None:
        print(filepath)

os.makedirs('outputs_file', exist_ok=True)

for filepath in inputs:
    Digitizer(filepath)