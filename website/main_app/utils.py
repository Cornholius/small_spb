import os


def rename_main_picture(instance, filename):
    upload_to = 'logo/'
    ext = filename.split('.')[-1]
    filename = 'logo.' + ext
    return os.path.join(upload_to, filename)
