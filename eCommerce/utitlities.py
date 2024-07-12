import secrets
from flask import current_app

def renameAndSave(image_file):
    
    name = secrets.token_hex(8)
    extension = image_file.filename.split('.')[1]
    file_name = name + '.' + extension

    path = current_app.root_path + '/static/images/' + file_name
    image_file.save(path)

    return file_name