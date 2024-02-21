from fastapi import HTTPException, UploadFile, File
from app.negocio import Excel
from app.helpers import tools
import os


async def convertirJsonExcel(filename, file : UploadFile = File(...)):
    if not filename:
        raise HTTPException(status_code=404, detail= {"error" : "No se ingreso el nombre del documento"});
    
    if not tools.validate_extension(file.filename, ['.json', '.JSON']):
        raise HTTPException(status_code=404, detail= {"error" : "El formato del archivo no es valido"});
    
    if not os.path.exists('./temp'):
        tools.create_directory()
    
    jsonData = tools.read_json(file.file)
    
    
    if not jsonData:
        raise HTTPException(status_code=404, detail= {"error" : "El archivo no contiene datos"});
    
    path = Excel.convertirJsontoExcel(jsonData, filename)
    
    tools.destroy_directory()
    
    return path