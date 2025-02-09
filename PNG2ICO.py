import pathlib, os ,sys
from PIL import Image

path = pathlib.Path(sys.argv[1])
if path.is_dir():
    for icon in path.iterdir():
        if icon.is_file():
            img = Image.open(icon)
            outpot_folder = os.path.join(icon.parent , 'outpot')
            if pathlib.Path(outpot_folder).exists():img.save(os.path.join(outpot_folder,icon.name.split('.')[0]+".ico"))
            else:
                pathlib.Path.mkdir(outpot_folder)
                img.save(os.path.join(outpot_folder,icon.name.split('.')[0]+".ico"))
else:
    img = Image.open(path)
    outpot_folder = os.path.join(path.parent , 'outpot')
    if pathlib.Path(outpot_folder).exists():img.save(os.path.join(outpot_folder,path.name.split('.')[0]+".ico"))
    else:
        pathlib.Path.mkdir(outpot_folder)
        img.save(os.path.join(outpot_folder,path.name.split('.')[0]+".ico"))
print('Done!')
input('Press any key to continue . . . ')