import sys
sys.path.append("/home/master/.local/lib/python3.9/site-packages")
from sqlalchemy import select, create_engine, MetaData, Table
import re


DB_USER = "$DB_USER"
DB_PASSWORD = "$DB_PASSWORD"
DB_HOST = "$DB_HOST"
DB_NAME = "$DB_NAME"

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}")


metadata = MetaData(bind=None)
table = Table(
    'as_neighbors', 
    metadata, 
    autoload=True, 
    autoload_with=engine
)

stmt = select([
    table.columns.neighbors]
).where(table.columns.as_num == '1321')

connection = engine.connect()
results = connection.execute(stmt).fetchall()


find_all = re.findall(r"\d+", str(results[0]))
print(', '.join(find_all))



15133, 7046, 2830, 702, 701