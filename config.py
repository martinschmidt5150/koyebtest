import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    FRONTEND_DIR = os.path.join(BASE_DIR, '../../frontend')