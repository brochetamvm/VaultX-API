from sqlalchemy import Column, Integer, String, Float
from src.database import Base

# Aqui definimos a estrutura física da tabela no banco de dados
class ProdutoDB(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    categoria = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)