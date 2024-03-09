import cv2
import pytesseract
import re
from pytesseract import Output
#from PIL import Image
from matplotlib import pyplot as plt
from fastapi import HTTPException, UploadFile, File


def getFechas(pathImage):
    if  not pathImage:
        raise HTTPException(status_code=500, detail=f"Error en la ruta de la imgen")
    
    invertImage = procesarImagen(pathImage)
    data_image = ocr(invertImage)
    
    data = re.findall('\w{2}-\w{3}-\w{4}', data_image)
    try: 
        output={
            'Fecha de nacimiento': data[0],
            'Fecha expedicion': data[1]}
    except:  #case both date were not identified 
        output={
            'Fecha de nacimiento': 'DD-MMM-YYYY',
            'Fecha expedicion': 'DD-MMM-YYYY'         
        }    
        
    return output
    
def getText(pathImage):
    if  not pathImage:
        raise HTTPException(status_code=500, detail=f"Error en la ruta de la imgen")
    
    img_color = cv2.imread(pathImage)
    invertImage = procesarImagen(pathImage)
    
    data_image= pytesseract.image_to_data(invertImage, output_type=Output.DICT)
    
    pathImage = boxText(data_image, img_color)
    
    return {'data' : pytesseract.image_to_string(invertImage), 'path' : pathImage}

def procesarImagen(pathImage):
    #Obtiene la imagen
    img_color = cv2.imread(pathImage)
    #Convierte a escala de grises
    img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    #Aplica filtro para eliminar ruido y mejorar el texto
    thresh_img = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    #Elimina los contornos de las letras
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,2))
    opening_image = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel,iterations=1)
    #Vuelve con la imagen invertida
    invert_image = 255 - opening_image
    
    return invert_image

def boxText(data_image, img_color):
    pathImage = 'temp/ImagenRectangulos.jpg'
    n_boxes = len(data_image['text'])
    
    for i in range(n_boxes):
        if int(data_image['conf'][i]) > 50:
            (x, y, w, h) = (data_image['left'][i], data_image['top'][i],data_image['width'][i], data_image['height'][i])
            img = cv2.rectangle(img_color, (x, y),(x + w, y + h),(255,0,0), 2)
    
    cv2.imwrite(pathImage, img)
    
    return  pathImage

def ocr(image):
    custom_config = r'-l spa  --psm 11'
    text = pytesseract.image_to_string(image,config=custom_config )
    return text