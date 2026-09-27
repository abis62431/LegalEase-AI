import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'legalease-secret-key-2026'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    UPLOAD_FOLDER = 'uploads'
