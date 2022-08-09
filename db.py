import databases

DB_USER = "$DB_USER"
DB_PASSWORD = "$DB_PASSWORD"
DB_HOST = "$DB_HOST"
DB_NAME = "$DB_NAME"

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
)

database = databases.Database(SQLALCHEMY_DATABASE_URL)
