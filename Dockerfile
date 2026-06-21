# Usamos uma imagem oficial do Python (versao slim para ser leve)
FROM python:3.12-slim

# Definimos o diretorio de trabalho dentro do container
WORKDIR /app

# Copiamos apenas o requirements para aproveitar o cache do Docker
COPY requirements.txt .

# Instalamos as dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos o restante do codigo
COPY . .

# Expomos a porta que o FastAPI usa
EXPOSE 8000

# Comando para rodar a API (sem o reload, pois em producao e fixo)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]