import os

API_KEY = os.getenv("API_KEY", "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c")
JWT_SECRET = os.getenv("JWT_SECRET", "mi_secret_seguro")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
