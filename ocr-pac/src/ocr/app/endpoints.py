import os

from fastapi.responses import JSONResponse
from fastapi import APIRouter, File, UploadFile
from ocr.utils.functions import func_OCR, func_check
import shutil
import logging

logging.basicConfig(level=logging.INFO)

# Create an API router
router = APIRouter()


@router.post("/read_pdf/")
async def read_pdf(file: UploadFile = File(...)):
    # try:
    current_directory = os.getcwd()
    input_folder_path = os.path.join(current_directory,
                                     "input_papers/")
    output_folder_path = os.path.join(current_directory,
                                      "output_papers/")
    output_folder_path_ = os.path.join(current_directory,
                                       "output_papers_/")
    output_folder_path_prueba1 = os.path.join(current_directory,
                                              "output_papers_prueba1/")

    os.makedirs(input_folder_path, exist_ok=True)
    os.makedirs(output_folder_path, exist_ok=True)
    os.makedirs(output_folder_path_, exist_ok=True)
    os.makedirs(output_folder_path_prueba1, exist_ok=True)

    with open(os.path.join(input_folder_path, file.filename), "wb") as f:
        f.write(await file.read())
        logging.info('Escribio el archivo en la carpeta temporal')

    func_check(input_folder_path, output_folder_path)

    perfil = func_OCR(output_folder_path,
                      output_folder_path_prueba1, output_folder_path_)

    # Eliminar directorios
    shutil.rmtree(input_folder_path, ignore_errors=True)
    shutil.rmtree(output_folder_path, ignore_errors=True)
    shutil.rmtree(output_folder_path_, ignore_errors=True)
    shutil.rmtree(output_folder_path_prueba1, ignore_errors=True)
    return JSONResponse(content=perfil, status_code=200)
    # except Exception as e:
    # Handle exceptions and return an error response in case of issues
    #    return JSONResponse(content={"error": str(e)}, status_code=500)
