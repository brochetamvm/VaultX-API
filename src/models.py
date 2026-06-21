from pydantic import BaseModel, Field

#Modelo Base: O que todo produto tem em comum
class ProdutoBase(BaseModel):
    nome: str = Field(..., description="Nome do produto")
    categoria: str = Field(..., description="Categoria (ex: Eletrônicos, Roupas)")
    preco: float = Field(..., gt=0, description="O preço deve ser maior que zero (gt = greater than)")
    quantidade: int = Field(0, ge=0, description="Quantidade no estoque (não pode ser negativa)")

#Modelo de Criação: O que o cliente envia para a API
class ProdutoCreate(ProdutoBase):
    pass # Para criar, precisamos exatamente das informações base, sem ID ainda.

#Modelo de Resposta: O que o Servidor devolve para o cliente
class ProdutoResponse(ProdutoBase):
    id: int # Quando o servidor responde, o produto já ganhou um ID no banco de dados

    class Config:
        from_attributes = True 