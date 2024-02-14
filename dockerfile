# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY . .
# 
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-spa

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload" ]
