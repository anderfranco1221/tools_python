from fastapi import HTTPException, UploadFile, File
from app.helpers import tools
from app.negocio import Imagen

def getTextImage(image : UploadFile = File(...)):
    
    #if not image:
    #    raise HTTPException(status_code=404, detail= {"error" : "No se ingreso el nombre del documento"});
    
    if not tools.validate_extension(image.filename, ['.jpg', '.png']):
        raise HTTPException(status_code=404, detail= {"error" : "El formato del archivo no es valido"});
    
    return Imagen.procesarImage(image)