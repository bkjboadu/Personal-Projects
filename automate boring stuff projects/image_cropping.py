from zip_processor import ZipProcessor
import sys
from PIL import Image
from pathlib import Path

'''trying something new for me to see
more comments to verify how things work on github
we will work on all these now 
Thank you lord for the position i am in 
you are great oh lord'''

'''trying something new for me to see
more comments to verify how things work on github
we will work on all these now 
Thank you lord for the position i am in 
you are great oh lord'''

'''trying something new for me to see
more comments to verify how things work on github
we will work on all these now 
Thank you lord for the position i am in 
you are great oh lord'''


class ScaleZip(ZipProcessor):

    def process_files(self):
        '''Scale each image in the directory to 640x480'''
        for filename in Path(self.temp_directory).iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640,480))
            scaled.save(str(filename))

if __name__ == "__main__":
    ScaleZip(*sys.argv[1:4]).process_zip()


