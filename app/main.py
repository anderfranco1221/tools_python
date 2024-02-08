
from fastapi.middleware.cors import CORSMiddleware
from fastapi import  FastAPI, Request, BackgroundTasks, UploadFile, File, HTTPException #, Depends,  Response, status
from fastapi.responses import FileResponse #JSONResponse, PlainTextResponse, StreamingResponse
#from app.config import settings
from app.controllers import ControllerExcel
from app.helpers import tools

# from typing import Annotated

app = FastAPI()
#router = APIRouter()


origins = [
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    #Indica los headers que el navegador puede ver
    #expose_headers=["Token"]
)

#app.include_router(users.router, prefix="/users", tags=["Users"])
url = "/api/";

@app.get("/api/test")
def test():
    return {"Hello": "World"}


@app.post("/api/excel/jsonToXml")
async def convertirJsontoExcel(file: UploadFile = File(...), filename: str = None):
    try:
        path = ControllerExcel.convertirJsonExcel(filename, file)
        
        #task.add_task(tools.eliminarDespues, 15, path)
        
        return FileResponse(path)
    except Exception as e:
        raise HTTPException(status_code=404, detail={"error": f"No se pudo generar el archivo. Detalle del error: {str(e)}"})
    
@app.post("/api/image/imageToText")
async def convertirImagenText(filename, file : UploadFile = File(...)):
    try:
        return #
    except Exception:
        raise HTTPException(status_code=404, detail={"Error":"No se pudo procesar la imagen"})
    

#if __name__ == "__main__":
    #uvicorn.run(app, host="0.0.0.0", port=80)