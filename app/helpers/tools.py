import json
import os
import time
import asyncio

def read_json(file_path: str):
    with file_path as file:
        data = json.load(file)
    return data

def validate_extension(file_path, valid_extensions):
    file_extension = os.path.splitext(file_path)[1]
    
    if file_extension.lower() in valid_extensions:
        return True
    else:
        return False
    

def limpiarArchivo(path: str):   
    try:
        os.remove(path)
    except FileNotFoundError:
        print("El archivo no pudo ser encontrado o eliminado.")
        
def eliminarDespues(segundos: int, path: str):
    print(path)
    time.sleep(segundos)
    limpiarArchivo(path)