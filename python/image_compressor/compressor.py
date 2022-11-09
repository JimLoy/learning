#python -m pip install Pillow
import os
from PIL  import Image 

downloads_folder = '/Users/Jim Loy/Downloads'
compressor_folder = f'{downloads_folder}compressed/'

if not os.path.exists(compressor_folder):
    os.makedirs(compressor_folder)

if __name__ == '__main__':
    for filename in os.listdir(downloads_folder):
        address_file = f'{downloads_folder}{filename}'
        name,extension = os.path.splitext(address_file)

        if extension in ['.jpg','.jpeg','.png']:
            picture = Image.open(address_file)
            picture.save(f'{compressor_folder}compressed_{filename}', optimize=True, quality=60)
            os.remove(address_file)
            print(f'{name}{extension}')

        #if extension in ['.mp3']:
        #    music_folder = ''
        #    os.rename(address_file, music_folder + filename)
