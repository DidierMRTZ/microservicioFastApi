from sqlalchemy import create_engine, MetaData

# Configurar conexión a MySQL
DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/nudges"
engine = create_engine(DATABASE_URL)