from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ocr.app import endpoints

# Create a FastAPI app instance
app = FastAPI()

# Configure CORS middleware
origins = ["*"]  # Update this list based on your security needs
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])


# Include the prediction router under the specified prefix
app.include_router(endpoints.router, prefix='/ocr/api/v1')
