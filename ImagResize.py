#This image recizer that produce 3 different sizes in 3 different folders

from PIL import Image
import os

size_300 = (300,300)
size_500 = (500,500)
size_80  = (80, 80)
os.mkdir('500')
os.mkdir('300')
os.mkdir('80')
for f in os.listdir("."):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
      
        i.thumbnail(size_500)
        i.save('500/{}_500{}'.format(fn,fext))
        
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))

        i.thumbnail(size_80)
        i.save('80/{}_80{}'.format(fn,fext))
