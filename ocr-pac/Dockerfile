FROM ubuntu
#python:3.10

RUN apt-get update && \
    apt-get install -y python3-pip libgl1-mesa-glx libglib2.0-0 tesseract-ocr ghostscript tesseract-ocr-spa pstotext poppler-utils pngquant libmagickwand-dev libtesseract-dev libxml2 antiword unrtf  flac ffmpeg lame libmad0 libsox-fmt-mp3 sox swig unpaper

WORKDIR /app
COPY requirements.txt /app/
COPY . /app/

RUN pip install -r requirements.txt
RUN pip install .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]