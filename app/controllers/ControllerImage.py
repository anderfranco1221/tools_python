import base64
import os
from fastapi import HTTPException, UploadFile, File
from app.helpers import tools
from app.negocio import Imagen

def getTextImage(image : UploadFile = File(...)):
    
    if not os.path.exists('./temp'):
        tools.create_directory()
    
    if not tools.validate_extension(image.filename, ['.jpg', '.png']):
        raise HTTPException(status_code=404, detail= {"error" : "El formato del archivo no es valido"});

    
    temp_file_path = f"temp/{image.filename}"
    
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(image.file.read())
    
    datos =  Imagen.getText(temp_file_path)
    
    #open binary file in read mode
    imagen = open(datos['path'], 'rb') 
    image_read = imagen.read()
    
    image_64_encode = base64.b64encode(image_read)
    
    return {'datos' : datos['data'], 'imagen' : image_64_encode}

def getInfoDocument(image : UploadFile = File(...)):

    if not os.path.exists('./temp'):
        tools.create_directory()
    
    if not tools.validate_extension(image.filename, ['.jpg', '.png']):
        raise HTTPException(status_code=404, detail= {"error" : "El formato del archivo no es valido"});

    temp_file_path = f"temp/{image.filename}"
    
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(image.file.read())

    return Imagen.getFechas(temp_file_path)