# FuriousAPI Project Template

Este projeto é um template para APIs RESTful usando FastAPI, SQLAlchemy e Alembic para migrações de banco de dados.

## Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual

**Linux/MacOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

### 1. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.exemple`:

```ini
# Para SQLite (padrão)
DB_ENGINE=sqlite

# Para PostgreSQL
# DB_ENGINE=postgresql
# DB_USER=seu_usuario
# DB_PASSWORD=sua_senha
# DB_HOST=localhost
# DB_PORT=5432
# DB_NAME=nome_do_banco
```

## Executando a Aplicação

### Rodar o servidor de desenvolvimento:

```bash
python main.py
```

A aplicação estará disponível em:
- http://localhost:8000
- Documentação interativa: http://localhost:8000/docs
- Documentação alternativa: http://localhost:8000/redoc

## Gerenciamento de Migrações com Alembic

### 1. Inicializar o Alembic (Com esse template pode pular essa etapa)

```bash
alembic init alembic
```

### 2. Configurar o Alembic

Edite `models/main.py` para importar seus modelos:

```python
from app.models.example import ItemExample
```

### 3. Criar uma nova migração

```bash
alembic revision --autogenerate -m "descrição das alterações"
```

### 4. Aplicar migrações

```bash
alembic upgrade head
```

## Estrutura do Projeto

```
meuprojeto/
├── core/               # Configurações centrais
│   ├── config.py       # Configurações da aplicação
│   └── database.py     # Configuração do banco de dados
├── models/             # Modelos do SQLAlchemy
├── schemas/            # Schemas do Pydantic
├── crud/               # Operações de banco de dados
├── api/                # Rotas da API
├── alembic/            # Migrações do banco de dados
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
└── .env                # Variáveis de ambiente
└── .env.exemple        # Modelo de Variáveis de ambiente
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`)
3. Commit suas mudanças (`git commit -am 'Add some fooBar'`)
4. Push para a branch (`git push origin feature/fooBar`)
5. Crie um novo Pull Request