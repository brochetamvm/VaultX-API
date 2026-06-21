from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do nosso banco local (SQLite)
DATABASE_URL = "sqlite:///./vaultx.db"

#Motor de conexão com o banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#Onde fazemos os INSERTs, UPDATEs e SELECTs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base para criar as nossas tabelas
Base = declarative_base()

#Função que o FastAPI vai usar para "abrir e fechar" a conexão em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()