import cv2
from matplotlib import pyplot as plt
from fastapi import HTTPException, UploadFile, File

def procesarImage(imagen : UploadFile = File(...)):
     # Guarda el archivo temporalmente
    temp_file_path = f"temp/{imagen.filename}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(imagen.file.read())


    img_color = cv2.imread(temp_file_path)
    
    img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    thresh_img = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,2))
    opening_image = cv2.morphologyEx(thresh_img, cv2.MORPH_OPEN, kernel,iterations=1)
    
    invert_image = 255 - opening_image
    plt.imshow(invert_image)
    plt.show()
    
    
def ocr(image):
    custom_config = r'-l spa - psm 11'
    text = pytesseract.image_to_string(image,config=custom_config )
    return text