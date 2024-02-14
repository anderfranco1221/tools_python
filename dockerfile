# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY . .

RUN sudo apt install tesseract-ocr

# 
RUN pip install -r requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]
