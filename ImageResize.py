#This python script take all the images in folder and sub folder and resize them into 3 different size and produce new images in one folder 

from PIL import Image
import os
size_300 = (300,300)
size_500 = (500,500)
size_80  = (80, 80)
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.jpg'):
            j= os.path.join(root,file)
            i = Image.open(j)
            fn, fext = os.path.splitext(file)
            i.thumbnail(size_500)
            i.save('{}_500{}'.format(fn,fext))
        
            i.thumbnail(size_300)
            i.save('{}_300{}'.format(fn,fext))

            i.thumbnail(size_80)
            i.save('{}_80{}'.format(fn,fext))
print("Done")
