
#from datetime import datetime, timedelta
import uuid
from fastapi import HTTPException
import pandas as pd
from pandas.io.excel import ExcelWriter

    
def convertirJsontoExcel(json, nameFile: str):    
    ruta = 'temp/' + nameFile + "_" +str(uuid.uuid4()) + ".xlsx"

    try:
        df = pd.json_normalize(json)
        
        with ExcelWriter(ruta) as writer:
                df.to_excel(writer, sheet_name="Datos", index=False)
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while converting JSON to Excel: {str(e)}")
    
    
    return ruta
