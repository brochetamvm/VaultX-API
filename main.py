from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models import ProdutoCreate, ProdutoResponse
from src.database import engine, Base, get_db
from src.db_models import ProdutoDB

#Cria vaultx.db e as tabelas fisicamente se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VaultX API",
    description="API Segura de Gestão de Estoque",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "VaultX API Online."}

#Rota POST: Para RECEBER e SALVAR um dado novo
#Injetamos o banco de dados na função usando: db: Session = Depends(get_db)
@app.post("/produtos/", response_model=ProdutoResponse, status_code=201)
async def cadastrar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    
    #Pegamos nos dados validados pelo Pydantic e convertemos para o modelo SQLAlchemy
    #**produto.model_dump() descompacta o dicionário diretamente para as colunas
    novo_produto = ProdutoDB(**produto.model_dump())
    
    #Adicionamos na sessão e guardamos (commit)
    db.add(novo_produto)
    db.commit()
    
    #Atualizamos o objeto para obter o ID gerado pelo banco
    db.refresh(novo_produto)
    
    return novo_produto

#Rota GET: Para DEVOLVER uma lista de dados
@app.get("/produtos/", response_model=list[ProdutoResponse])
async def listar_produtos(db: Session = Depends(get_db)):
    # Faz o equivalente a um SELECT * FROM produtos;
    produtos = db.query(ProdutoDB).all()
    return produtos

#Rota PUT: Para ATUALIZAR um produto existente
@app.put("/produtos/{produto_id}", response_model=ProdutoResponse)
async def atualizar_produto(produto_id: int, produto_atualizado: ProdutoCreate, db: Session = Depends(get_db)):
    #Procuramos o produto no banco
    produto_db = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    
    #Se não encontrar, devolvemos erro 404 (Not Found)
    if not produto_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    #Atualizamos os campos
    for chave, valor in produto_atualizado.model_dump().items():
        setattr(produto_db, chave, valor)
    
    #Salvamos no banco
    db.commit()
    db.refresh(produto_db)
    
    return produto_db

# Rota DELETE: Para REMOVER um produto
@app.delete("/produtos/{produto_id}")
async def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    #Procuramos o produto
    produto_db = db.query(ProdutoDB).filter(ProdutoDB.id == produto_id).first()
    
    if not produto_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    #Deletamos e salvamos
    db.delete(produto_db)
    db.commit()
    
    return {"message": f"Product {produto_id} successfully removed from VaultX"}