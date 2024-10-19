import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"

    # Connection string using Windows Authentication
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@DESKTOP-9832HEC/ECommerceDB?"
        "driver=ODBC+Driver+17+for+SQL+Server&"
        "Trusted_Connection=yes"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
