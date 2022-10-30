import glob
import os
import shutil
from PIL import Image

inputs = glob.glob('inputs\*.jpg')

class Digitizer:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.img = Image.open(filepath)

    def make_upside_down(self):
        print("make upside down!")
        self.img = self.img.rotate(180)

    def save(self, output_filepath):
        print('This has saved!!!')
        self.img.save(output_filepath)

os.makedirs('outputs_file', exist_ok=True)

for filepath in inputs:
    output = filepath.replace('inputs', 'outputs_file')

    image = Digitizer(filepath)
    image.make_upside_down()
    image.save(output)