# src/config.py

import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "not_very_secret_key"

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") 

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URL")
  
class ProductionConfig(BaseConfig):
    url1 = os.environ.get("DATABASE_URL")
    
    if url1 is not None and url1.startswith("postgres://"):
        url = url1.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = url