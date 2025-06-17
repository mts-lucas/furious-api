# Furious API - FastAPI Boilerplate Generator

O Furious API é um gerador de projetos FastAPI, projetado para acelerar seu fluxo de trabalho com uma estrutura bem organizada desde o início.

## 🚀 Como testar localmente

### Pré-requisitos
- Python 3.10+
- Poetry instalado
- Git

### 1. Clone o repositório
```bash
git clone https://github.com/mts-lucas/furious-api.git
cd furious-api
```

### 2. Configure o ambiente
```bash
poetry install  # Instala todas as dependências
poetry shell    # Ativa o ambiente virtual
```

### 3. Testando o comando `furious startapp`

Para testar o gerador localmente:

```bash
furious startapp meu_projeto
```

Isso criará uma nova pasta `meu_projeto` com toda a estrutura FastAPI pré-configurada.

## 🛠 Estrutura do Projeto Gerado

O comando `furious startapp` cria a seguinte estrutura:

```
seu_diretorio/
├── meu_projeto/
|  ├── core/          # Configurações centrais
|  ├── models/        # Modelos de banco de dados
|  ├── schemas/       # Schemas Pydantic
|  ├── api/           # Rotas da API
|  ├── crud/          # Operações de banco
|  └── main.py        # Ponto de entrada
├── alembic/           # Migrações de banco
├── alembic.ini
├── requirements.txt   # Dependências do projeto
├── .env.exemple       # Variáveis de ambiente
└── README.md          # Documentação do projeto
```

## 🤝 Como Contribuir

Quer ajudar a melhorar o Furious API? Siga estes passos:

### 1. Faça um fork do projeto

### 2. Crie uma branch para sua feature
```bash
git checkout -b feature/nova-feature
```

### 3. Desenvolva sua feature
- Adicione testes para novas funcionalidades
- Mantenha o código limpo e documentado


### 4. Envie um Pull Request
- Descreva claramente suas mudanças
- Referencie issues relacionadas (se aplicável)

## 📌 Diretrizes de Contribuição

1. **Padrão de Commits**: Siga o [Conventional Commits](https://www.conventionalcommits.org/)
2. **Documentação**: Atualize a documentação quando necessário

## 🐛 Reportando Bugs

Encontrou um problema? Por favor:
1. Verifique se já não foi reportado nas [Issues](https://github.com/mts-lucas/furious-api/issues)
2. Crie uma nova issue com:
   - Descrição detalhada
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Capturas de tela (se aplicável)

## 📄 Licença

[MIT](LICENSE)

---

✨ **Pronto para começar?** Clone o projeto e execute `furious startapp` para criar seu próximo projeto FastAPI em segundos!