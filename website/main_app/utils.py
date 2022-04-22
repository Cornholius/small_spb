import os
from pathlib import Path


def rename_main_picture(instance, filename):
    try:
        os.remove(str(Path(__file__).resolve().parent.parent) + '/' + str(os.path.join('media', 'logo', 'logo.jpg')))
    except Exception:
        print('nothing to delete')
    upload_to = 'logo/'
    ext = filename.split('.')[-1]
    filename = 'logo.' + ext
    return os.path.join(upload_to, filename)
